import datetime
import json
from contextlib import suppress
from functools import cached_property

import attr
from dateutil.parser import isoparse

from git_pr_branch.config import conf

from .base import PullRequest, ServerRepo, APIError, NotFound


@attr.s(auto_attribs=True)
class GithubPR(PullRequest):
    @classmethod
    def from_server(cls, repo, data):
        return cls(
            number=data["number"],
            url=data["url"],
            title=data["title"],
            state=data["state"],
            html_url=data["html_url"],
            head_fullname=data["head"]["repo"]["full_name"],
            head_username=data["head"]["repo"]["owner"]["login"],
            head_branch=data["head"]["ref"],
            head_commit=data["head"]["sha"],
            head_git_url=data["head"]["repo"]["ssh_url"],
            username=data["user"]["login"],
            repo=repo,
        )

    def get_reviews(self):
        reviews = self.repo.call_api(f"/pulls/{self.number}/reviews")
        return [Review.from_github(review) for review in reviews]


@attr.s(auto_attribs=True)
class Review:
    id: int
    commit_id: str
    html_url: str
    username: str
    state: str
    datetime: datetime.datetime
    body: str

    @classmethod
    def from_github(cls, data):
        try:
            datetime = isoparse(data["submitted_at"])
        except KeyError:
            datetime = None
        return cls(
            id=data["id"],
            commit_id=data["commit_id"],
            html_url=data["html_url"],
            username=data["user"]["login"],
            state=data["state"],
            datetime=datetime,
            body=data["body"],
        )


class GithubRepo(ServerRepo):
    _clone_url_prefixes = (
        "git@github.com:",
        "https://github.com/",
    )
    _config_requires = ["github_token"]
    _pr_class = GithubPR

    @classmethod
    def from_path(cls, path):
        username, repo = path.split("/", 1)
        if repo.endswith(".git"):
            repo = repo[: -len(".git")]
        return cls(username=username, reponame=repo)

    @property
    def fullname(self):
        return f"{self.username}/{self.reponame}"

    @property
    def root_api_url(self):
        return "https://api.github.com"

    @property
    def api_url(self):
        return f"{self.root_api_url}/repos/{self.fullname}"

    @property
    def html_url(self):
        return f"https://github.com/{self.fullname}"

    @property
    def git_url(self):
        return f"git@github.com:{self.fullname}.git"

    def call_api(self, url, method="GET", **kwargs):
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"token {conf['github_token']}",
        }
        headers.update(kwargs.get("headers", {}))
        if "data" in kwargs:
            kwargs["data"] = json.dumps(kwargs["data"])
        return super().call_api(url, method=method, headers=headers, **kwargs)

    def _get_pull_ref(self, fork_repo, remote_ref):
        return f"{fork_repo.username}:{remote_ref}"

    def _get_pulls(self, pull_ref):
        return self.call_api(f"/pulls?state=all&head={pull_ref}")

    def _get_pull(self, number):
        try:
            return self.call_api(f"/pulls/{number}")
        except APIError as e:
            with suppress(KeyError, TypeError, AttributeError):
                if json.loads(e.message)["message"] == "Not Found":
                    raise NotFound(e.message) from e
            raise

    def get_default_branch_name(self):
        data = self.call_api("/")
        return data["default_branch"]

    @cached_property
    def current_username(self):
        response = self.call_api("/user", method="GET", project_url=False)
        return response["login"]

    def fork(self):
        # https://docs.github.com/en/rest/repos/forks?apiVersion=2022-11-28#create-a-fork
        self.call_api(
            "/forks",
            method="POST",
            data={
                "repo": self.reponame,
                "default_branch_only": "true",
            },
            timeout=300,
        )

    def ensure_fork(self):
        self.fork()
        return self.__class__(
            username=self.current_username,
            reponame=self.reponame,
        )
