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
    rev: INSERT_VERSION
    hooks:
    -    id: compare-stack-and-file-names
    -    id: check-stack-names
```
replacing `INSERT_VERSION` with a version tag or commit SHA-1.

## Usage

The hook `compare-stack-and-file-names` can be run from the root of
a Git repo. It will look for any files ending in `.yaml` under the
directories `./config/prod/` & `./config/dev/`, render them as Jinja2
templates, then attempt to parse the result (as YAML files) and check
that the value of `stack_name` matches the file name (minus `.yaml`).

The hook `check-stack-names` behaves similarly, but instead of checking
that a given file name matches the stack name, it will just check that
a stack name matches the [constraints specified by
CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-parameters.html)

Currently, no arguments or other parameters can be passed to these linters.
