import os
from pathlib import Path
from typing import TYPE_CHECKING, Optional, Sequence, Union

from dagster import DagsterInvariantViolationError
from dagster._annotations import experimental
from dagster._core.definitions.metadata import link_to_source_control
from dagster._core.types.loadable_target_origin import LoadableTargetOrigin

if TYPE_CHECKING:
    from dagster import AssetsDefinition, SourceAsset
    from dagster._core.definitions.cacheable_assets import CacheableAssetsDefinition

import sys


def _locate_git_root() -> Optional[Path]:
    try:
        code_origin = LoadableTargetOrigin.get()
    except DagsterInvariantViolationError:
        return None

    # get module matching code_origin.module_name
    module_or_pkg_name = code_origin.module_name or code_origin.package_name
    if module_or_pkg_name:
        module = sys.modules.get(module_or_pkg_name)
        if module:
            code_origin_filepath = module.__file__
    elif code_origin.python_file:
        code_origin_filepath = code_origin.python_file

    if not code_origin_filepath:
        return None
    current_dir = Path(code_origin_filepath)
    for parent in current_dir.parents:
        if (parent / ".git").exists():
            return parent
    return None


@experimental
def link_to_git_if_cloud(
    assets_defs: Sequence[Union["AssetsDefinition", "SourceAsset", "CacheableAssetsDefinition"]],
    source_control_url: Optional[str] = None,
    source_control_branch: Optional[str] = None,
    repository_root_absolute_path: Optional[Union[Path, str]] = None,
) -> Sequence[Union["AssetsDefinition", "SourceAsset", "CacheableAssetsDefinition"]]:
    """Wrapper function which converts local file path code references to hosted git URLs
    if running in a Dagster Plus cloud environment. This is determined by the presence of
    the `DAGSTER_CLOUD_DEPLOYMENT_NAME` environment variable. When running in any other context,
    the local file references are left as is.

    Args:
        assets_defs (Sequence[Union[AssetsDefinition, SourceAsset, CacheableAssetsDefinition]]):
            The asset definitions to which source control metadata should be attached.
            Only assets with local file code references (such as those created by
            `with_source_code_references`) will be converted.
        source_control_url (Optional[str]): Override base URL for the source control system. By default,
            inferred from the `DAGSTER_CLOUD_GIT_URL` environment variable provided by cloud.
            For example, "https://github.com/dagster-io/dagster".
        source_control_branch (str): Override branch in the source control system, such as "master".
            Defaults to the `DAGSTER_CLOUD_GIT_SHA` or `DAGSTER_CLOUD_GIT_BRANCH` environment variable.
        repository_root_absolute_path (Union[Path, str]): Override path to the root of the
            repository on disk. This is used to calculate the relative path to the source file
            from the repository root and append it to the source control URL. By default, inferred
            from walking up the directory tree from the code location entrypoint until the git root
            is found.
    """
    is_dagster_cloud = os.getenv("DAGSTER_CLOUD_DEPLOYMENT_NAME") is not None

    if not is_dagster_cloud:
        return assets_defs

    source_control_url = source_control_url or os.getenv("DAGSTER_CLOUD_GIT_URL")
    source_control_branch = (
        source_control_branch
        or os.getenv("DAGSTER_CLOUD_GIT_SHA")
        or os.getenv("DAGSTER_CLOUD_GIT_BRANCH")
    )
    repository_root_absolute_path = repository_root_absolute_path or _locate_git_root()

    if not source_control_url or not source_control_branch:
        raise ValueError(
            "Detected that this is a Dagster Cloud deployment, but"
            " could not infer source control information for this repository. Please provide"
            " values for `source_control_url` and `source_control_branch`."
        )

    if not repository_root_absolute_path:
        raise ValueError(
            "Detected that this is a Dagster Cloud deployment, but"
            " could not infer the git root for the repository. Please provide a value for "
            "`repository_root_absolute_path`."
        )

    return link_to_source_control(
        assets_defs=assets_defs,
        source_control_url=source_control_url,
        source_control_branch=source_control_branch,
        repository_root_absolute_path=repository_root_absolute_path,
    )
