# Provisioner Pre-Commit Hooks
This repo contains scripts for the purpose of pre-commit processing
(e.g. linting) of resource provision requests.

## Installation 

The scripts in this repo can currently be installed by running
`pip install .` with the working directory set to this repo's root
directory.

This can also be used as a pre-commit hook, by including the following
in `.pre-commit-config.yaml`: 
```
-   repo: https://github.com/Sage-Bionetworks-IT/pre-commit-provisioner
    rev: v0.0.1
    hooks:
    -    id: compare-stack-and-file-names
```

## Usage

The script `compare-stack-and-file-names` can be run from the root of
a Git repo. It will look for any files ending in `.yaml` under the
directory `./config/`, attempt to parse them (as YAML files) and check
that the value of the `stack_name` matches the file name (minus `.yaml`).

Currently, no arguments or other parameters can be passed to this linter.
