"""
CRC Tool

Tool to insert CRCs into ELF files or generate binary for programming
ccfg user region

Copyright (C) 2024 Texas Instruments Incorporated


 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:

   Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

   Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.

   Neither the name of Texas Instruments Incorporated nor the names of
   its contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import os
import re
import logging
import setuptools
import subprocess


def get_version():
    """Use git to get latest version from most recent tag."""
    try:
        git_version_call = subprocess.run(
            [
                "git",
                "describe",
                # Without this flag it only looks for annotated tags
                "--tags"
            ],
            capture_output=True,
            encoding="utf-8"
        )
        describe_output = git_version_call.stdout.strip()
        # Match major, minor, patch, build to align with fwtools version matching
        version_regex = re.search("^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", describe_output)
        if version_regex:
            return version_regex.group(0)
        else:
            logging.warning(
                "Git describe did not give valid version number %s, returning 0.00.00.00",
                describe_output
            )
            return "0.00.00.00"
    except FileNotFoundError as exc:
        logging.warning("Got Error when trying to check latest tag with git: %s", exc)
        return "0.00.00.00"


setuptools.setup(
    name="crc_tool",
    version=get_version(),
    author="Oslo Tools team",
    author_email="i.hovind@ti.com",
    packages=setuptools.find_packages(),
    package_data={
        "crc_tool": ["py.typed"],
    },
    entry_points={
        "console_scripts": [
            "crc_tool = crc_tool.main:app",
        ]
    },
    install_requires=[
        # DEPENDENCIES LAST UPDATED AT:
        # 2024-02-09, Ingebrigt Hovind
        # Key dependencies, install latest minor version
        "lief == 0.12.3",
        # Development dependencies
        # Using 6.4.0 caused it to be flagged as a virus by symantec
        # Downgrading to this (arbitrarily chosen) value fixed it
        "pyinstaller == 5.6.2",
        "cffi == 1.15.1",
        "pywin32-ctypes",
        "mypy",
        "pylint",
        "pytest",
    ],
)
