#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import toml
import sys
import requests
import subprocess

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Check if the current version is published on PyPI.')
    parser.add_argument('toml_path', help='Path to the pyproject.toml file')
    args = parser.parse_args()

    # Load the pyproject.toml file
    data = toml.load(open(args.toml_path))

    # Get the current version
    current_version = data["project"]["version"]

    # Get the package name
    package_name = data["project"]["name"]
    # Check if the version is already published
    response = requests.get(f"https://pypi.org/pypi/{package_name}/{current_version}/json")

    if response.status_code == 200:
        print("This version is already published. Please bump the version in pyproject.toml.")
        sys.exit(1)

    # Check if pyproject.toml has been modified but not committed
    modified_files = subprocess.check_output(["git", "diff", "--name-only"]).decode().splitlines()

    if "pyproject.toml" in modified_files:
        print("The version in pyproject.toml has been changed but not committed. Please commit your changes.")
        sys.exit(1)

if __name__ == "__main__":
    main()
