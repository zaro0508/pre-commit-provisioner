# Provisioner Pre-Commit Hooks
This repo contains scripts for the purpose of pre-commit processing
(e.g. linting) of resource provision requests.

## Installation 

The scripts in this repo can currently be installed by running
`pip install --editable .` with the working directory set to this
repo's root directory. For some reason, `pip install .` does not
seem to work yet, which is delaying the deployment of this package
as a pre-commit hook.

## Usage

The script `compare-stack-and-file-names` can be run from the root of
a Git repo. It will look for any files ending in `.yaml` under the
directory `./config/`, attempt to parse them (as YAML files) and check
that the value of the `stack_name` 
