# Provisioner Pre-Commit Hooks
This repo contains scripts for the purpose of pre-commit processing
(e.g. linting) of resource provision requests.

## Installation 

The scripts in this repo can currently be installed by running
`pip install .` while this repo's root is the working directory.

## Usage

The script `compare-stack-and-file-names` can be run from the root of
a Git repo. It will look for any files ending in `.yaml` under the
directory `./config/`, attempt to parse them (as YAML files) and check
that the value of the `stack_name` 
