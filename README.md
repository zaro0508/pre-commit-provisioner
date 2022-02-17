This repo contains scripts for the purpose of pre-commit processing
(e.g. linting) of Sceptre config files.

## Installation 

The linter scripts can be installed by running `pip install .` 

The scripts can be run from the
[sceptre root directory](https://sceptre.cloudreach.com/2.3.0/docs/templates.html#templates).
It will process files ending in `.yaml` under the
`./config/prod/` & `./config/dev/`directories

## Linters

* `compare-stack-and-file-names`  Renders to
[Jinja2 templates](https://jinja.palletsprojects.com/en/2.11.x/), then
attempt to parse the result (as YAML files) and check that the value
of the `stack_name` matches the file name (minus `.yaml`).

* `check-stack-names` Checks for valid stack names in sceptre configs.  Valid
stack names are [constraints specified by
CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-parameters.html)

* `check-stack-tags` Checks for 'stack_tags' definition in sceptre configs.

Currently, no arguments or other parameters can be passed to these linters.

## Usage

### Stand Alone
Running scripts:
```shell script
➜ check-stack-names ./config/prod/*.yaml
- 'foo_ec2' is an invalid stack name (in './config/prod/ec2.yaml')
- 'bar bucket' is an invalid stack name (in './config/prod/s3.yaml')
```
__NOTE__: A stack name can contain only alphanumeric characters (case-sensitive) and hyphens.
It must start with an alphabetic character and can't be longer than 128 characters. For more
details refer to the [AWS documentation](
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-parameters.html)

```shell script
➜ compare-stack-and-file-names ./config/prod/*.yaml
- Stack name 'foo-stack' does not match file name 'foo_stack.yaml'
```

### Pre-commit hook
The scripts can also be [used as a pre-commit hook](https://pre-commit.com/#2-add-a-pre-commit-configuration),
by including the following in `.pre-commit-config.yaml`: 
```
-   repo: https://github.com/Sage-Bionetworks-IT/pre-commit-provisioner
    rev: INSERT_VERSION
    hooks:
    -    id: compare-stack-and-file-names
    -    id: check-stack-names
    -    id: check-stack-tags
```
replacing `INSERT_VERSION` with a version tag or commit SHA-1.


After adding the above to one's pre-commit config file, one can run this hook as follows:
```shell script
➜ pre-commit run --all-files
Stack name linter........................................................Failed
- hook id: check-stack-names
- exit code: 1

- 'foo_ec2' is an invalid stack name (in 'config/prod/ec2.yaml')
- 'bar bucket' is an invalid stack name (in 'config/prod/s3.yaml')
```
