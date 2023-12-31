<!-- TOC -->

- [Disclaimer](#disclaimer)
- [VS Code and miniconda intergration](#vs-code-and-miniconda-intergration)
    - [Mac OS](#mac-os)
        - [Install the miniconda distro if it's needed](#install-the-miniconda-distro-if-its-needed)
        - [Prepare a separate env](#prepare-a-separate-env)
    - [vs code config](#vs-code-config)
- [How to run](#how-to-run)
    - [a test env](#a-test-env)
    - [tests](#tests)

<!-- /TOC -->

# Disclaimer
Originally I use MacOS for developing and write all scripts for Mac. Ispite of this there isn't any reason for not working on Linux systems but could get some difficulties on Windows.

# VS Code and miniconda intergration
## Mac OS
### Install the miniconda distro if it's needed 
```
# curl -o /tmp/m.sh -s https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-MacOSX-arm64.sh && bash /tmp/m.sh -b -p $HOME/miniconda
```
### Prepare a separate env
```
# ~/miniconda/bin/conda env create -f ./develop/miniconda-environment.yml
# ~/miniconda/envs/thvac/bin/pip list local| grep hvac
```
## vs code config
A workspace configuration into ./.vscode/settings.json. It contains the path for the miniconda env for syntax and methods highlighting.

# How to run 
## a test env
```
./develop/compose.sh
```
You need to run this command from root directory of the git repository. It uses docker and docker compose.

## tests
```
./tests/run.sh
```
The test env is needed!