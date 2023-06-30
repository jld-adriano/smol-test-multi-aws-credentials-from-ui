# Multi AWS Credentials

Simple tool to manage multiple AWS credentials locally for when AWS CLI profiles are not enough.

Supports password encryption, and receiving values from stdin to prevent shell history leakage.

As a preferred mode of operation, it loads your credentials into your shell env instead, meaning there are no unencrypted credential files on disk.

## Installation

- npm: npm install -g multi-aws-credentials
- yarn: yarn global add multi-aws-credentials

## Usage:

Usage: multi-aws-credentials [options] [command]

For use cases where AWS CLI profiles are not sufficient

Options: 
- -V, --version output the version number 
- -h, --help display help for command

Commands: 
- add [options] [id] [secret] [region] Add a profile 
- change Change the current (default) profile 
- list list profiles 
- rename Rename a profile 
- upsert [options] [id] [secret] [region] Add a profile if it doesn't exist, otherwise replace it 
- env Outputs a profile as shell compatible variable exports, for use with eval 
- env-run [script...] Run a command with configured environment variables. Pass command after -- or through stdin 
- encrypt Encrypt a profile with a password 
- remove Remove a profile 
- help [command] display help for command

## How it works

It creates a file in ~/.aws/$NAME.creds for each profile. Upon changing to a profile, it replaces ~/.aws/credentials with the specific profile file. As a preferable mode of operation, you should instead load the credentials into your current shell with the `env` command like `eval $(multi-aws-credentials env my-profile)`