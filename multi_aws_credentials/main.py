```python
import argparse
from multi_aws_credentials import command, constants, utils

def main():
    parser = argparse.ArgumentParser(prog='multi-aws-credentials', description='Manage multiple AWS credentials locally.')
    parser.add_argument('-V', '--version', action='version', version=constants.VERSION)
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a profile')
    add_parser.add_argument('id')
    add_parser.add_argument('secret')
    add_parser.add_argument('region')

    change_parser = subparsers.add_parser('change', help='Change the current (default) profile')

    list_parser = subparsers.add_parser('list', help='List profiles')

    rename_parser = subparsers.add_parser('rename', help='Rename a profile')

    upsert_parser = subparsers.add_parser('upsert', help='Add a profile if it doesn\'t exist, otherwise replace it')
    upsert_parser.add_argument('id')
    upsert_parser.add_argument('secret')
    upsert_parser.add_argument('region')

    env_parser = subparsers.add_parser('env', help='Outputs a profile as shell compatible variable exports, for use with eval')

    env_run_parser = subparsers.add_parser('env-run', help='Run a command with configured environment variables. Pass command after -- or through stdin')

    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a profile with a password')

    remove_parser = subparsers.add_parser('remove', help='Remove a profile')

    args = parser.parse_args()

    if args.command == 'add':
        command.add(args.id, args.secret, args.region)
    elif args.command == 'change':
        command.change()
    elif args.command == 'list':
        command.list()
    elif args.command == 'rename':
        command.rename()
    elif args.command == 'upsert':
        command.upsert(args.id, args.secret, args.region)
    elif args.command == 'env':
        command.env()
    elif args.command == 'env-run':
        command.env_run()
    elif args.command == 'encrypt':
        command.encrypt()
    elif args.command == 'remove':
        command.remove()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```