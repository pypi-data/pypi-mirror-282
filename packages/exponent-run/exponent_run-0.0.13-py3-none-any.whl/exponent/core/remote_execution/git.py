import os

import pygit2
from exponent.core.remote_execution.types import (
    GetAllTrackedFilesRequest,
    GetAllTrackedFilesResponse,
    GitInfo,
    RemoteFile,
)


def get_all_tracked_files(
    request: GetAllTrackedFilesRequest,
    working_directory: str,
) -> GetAllTrackedFilesResponse:
    return GetAllTrackedFilesResponse(
        correlation_id=request.correlation_id,
        files=get_all_tracked_git_file_paths(working_directory),
    )


def get_all_tracked_git_file_paths(working_directory: str) -> list[RemoteFile]:
    repo = pygit2.Repository(working_directory)
    paths = sorted([entry.path for entry in repo.index])
    return [
        RemoteFile(file_path=path, working_directory=working_directory)
        for path in paths
    ]


def get_git_info(working_directory: str) -> GitInfo | None:
    try:
        repo = pygit2.Repository(working_directory)
    except pygit2.GitError:
        return None

    return GitInfo(
        branch=_get_git_branch(repo) or "<unknown branch>",
        remote=_get_git_remote(repo),
    )


def _get_git_remote(repo: pygit2.Repository) -> str | None:
    if repo.remotes:
        return str(repo.remotes[0].url)
    return None


def _get_git_branch(repo: pygit2.Repository) -> str | None:
    try:
        # Look for HEAD file in the .git directory
        head_path = os.path.join(repo.path, "HEAD")
        with open(head_path) as head_file:
            # The HEAD file content usually looks like: 'ref: refs/heads/branch_name'
            head_content = head_file.read().strip()
            if head_content.startswith("ref:"):
                return head_content.split("refs/heads/")[-1]
            else:
                return None
    except Exception:  # noqa: BLE001
        return None
