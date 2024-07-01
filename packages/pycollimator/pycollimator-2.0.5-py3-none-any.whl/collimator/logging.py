# Copyright (C) 2024 Collimator, Inc.
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, version 3. This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General
# Public License for more details.  You should have received a copy of the GNU
# Affero General Public License along with this program. If not, see
# <https://www.gnu.org/licenses/>.

# https://www.firedrakeproject.org/_modules/firedrake/logging.html
import logging

from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

__all__ = [
    "logger",
    "set_log_level",
    "set_file_handler",
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
]

packages = [__package__, "collimator_profiler"]


__fmt = "%(name)s:%(levelname)s %(message)s"
__formatter = logging.Formatter(fmt=__fmt)
__stream_handler = logging.StreamHandler()
__stream_handler.setFormatter(__formatter)


def set_file_handler(file, formatter=logging.Formatter(fmt=__fmt)):
    """Set a file handler to all packages."""
    fh = logging.FileHandler(file, mode="w")
    fh.setFormatter(formatter)
    for package in packages:
        logger_ = logging.getLogger(package)
        logger_.addHandler(fh)


def set_stream_handler(handler=None):
    """Set the stream handler to all packages."""
    for package in packages:
        logger_ = logging.getLogger(package)
        logger_.addHandler(handler if handler else __stream_handler)


def unset_stream_handler():
    """Remove the stream handler from all packages."""
    for package in packages:
        logger_ = logging.getLogger(package)
        logger_.removeHandler(__stream_handler)


def set_log_level(level, pkg: str | None = None):
    """Set the log level for the specified or all packages.

    Args:
        level: The log level to set.
        pkg: If set, apply the log level only to the specified package.
    """
    if pkg is not None:
        logger_ = logging.getLogger(pkg)
        logger_.setLevel(level)
        return

    for package in packages:
        logger_ = logging.getLogger(package)
        logger_.setLevel(level)


def scope_logging(func):
    """Decorator to log function entry and exit."""

    def wrapper(*args, **kwargs):
        logger_ = logging.getLogger(__package__)
        logger_.debug("*** Entering %s ***", func.__qualname__)
        result = func(*args, **kwargs)
        logger_.debug("*** Exiting %s ***", func.__qualname__)
        return result

    return wrapper


def _block_info(block) -> dict:
    """Returns info about a block as a fake Error object"""
    if not block or not hasattr(block, "name_path_str"):
        return {}

    name_path = block.name_path_str
    uuid_path = block.ui_id_path
    if not name_path or not uuid_path:
        return {}

    return {
        "__error__": {
            "kind": "NotAnError",
            "name_path": name_path,
            "uuid_path": uuid_path,
        }
    }


def logdata(*, block=None, **kwargs):
    """Use this in log.info() and other logging functions to include block info:

    log.info("message", **logdata(block=self))
    """
    if not block:
        return {}

    # "extra" is for python logging
    # "extras" is for our custom "api" for the frontend
    # "__errors__" is well understood by the frontend
    extras = kwargs or {}
    if block is not None:
        extras.update(_block_info(block))

    return {"extra": {"extras": extras}}


logger = logging.getLogger(__package__)
log = logger.log
debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
