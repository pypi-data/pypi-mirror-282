# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module defining commands in the 'qbraid jobs' namespace.

"""
import sys
from pathlib import Path

from jupyter_client.kernelspec import KernelSpecManager

from qbraid_core.system.executables import is_exe

from .paths import installed_envs_data


def _get_kernels_path(environment: str) -> Path:
    """Get the path to the kernels directory for the given environment."""
    slug_to_path, name_to_slug = installed_envs_data()

    if environment in name_to_slug:
        slug = name_to_slug.get(environment, None)
    else:
        slug = environment

    if slug not in slug_to_path:
        raise ValueError(f"Environment '{environment}' not found.")

    env_path = slug_to_path[slug]
    kernels_path = env_path / "kernels"
    return kernels_path


def list_kernels() -> list:
    """List all kernels.
    Returns:
        list: A list of all kernels and their resource directories.
    """
    kernel_spec_manager = KernelSpecManager()
    # Get the list of kernelspecs
    return kernel_spec_manager.get_all_specs()


def add_kernels(environment: str) -> tuple:
    """Add a kernel."""
    try:
        kernels_path = _get_kernels_path(environment)
    except ValueError as e:
        raise e

    is_local = str(kernels_path).startswith(str(Path.home()))
    resource_path = str(Path.home() / ".local") if is_local else sys.prefix

    kernel_spec_manager = KernelSpecManager()

    for kernel in kernels_path.iterdir():
        kernel_spec_manager.install_kernel_spec(source_dir=str(kernel), prefix=resource_path)


def remove_kernels(environment: str) -> None:
    """Remove a kernel."""
    try:
        kernels_path = _get_kernels_path(environment)
    except ValueError as e:
        raise e

    kernel_spec_manager = KernelSpecManager()
    for kernel in kernels_path.iterdir():
        kernel_spec_manager.remove_kernel_spec(kernel.name)
