```python
import click
from .profile import Profile
from .credentials import Credentials
from .encryption import encrypt, decrypt
from .utils import load_profile, save_profile, delete_profile

@click.group()
def cli():
    pass

@cli.command()
@click.option('--id', prompt=True)
@click.option('--secret', prompt=True, hide_input=True)
@click.option('--region', prompt=True)
def add(id, secret, region):
    profile = Profile(id, secret, region)
    save_profile(profile)

@cli.command()
@click.argument('profile_name')
def change(profile_name):
    profile = load_profile(profile_name)
    Credentials.set_default(profile)

@cli.command()
def list():
    for profile in Profile.list_all():
        click.echo(profile.name)

@cli.command()
@click.argument('old_name')
@click.argument('new_name')
def rename(old_name, new_name):
    profile = load_profile(old_name)
    profile.rename(new_name)

@cli.command()
@click.option('--id', prompt=True)
@click.option('--secret', prompt=True, hide_input=True)
@click.option('--region', prompt=True)
def upsert(id, secret, region):
    profile = Profile(id, secret, region)
    save_profile(profile, overwrite=True)

@cli.command()
@click.argument('profile_name')
def env(profile_name):
    profile = load_profile(profile_name)
    click.echo(profile.to_env())

@cli.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('command', nargs=-1, type=click.UNPROCESSED)
def env_run(command):
    exec(' '.join(command))

@cli.command()
@click.argument('profile_name')
@click.option('--password', prompt=True, hide_input=True)
def encrypt(profile_name, password):
    profile = load_profile(profile_name)
    encrypted_profile = encrypt(profile, password)
    save_profile(encrypted_profile)

@cli.command()
@click.argument('profile_name')
def remove(profile_name):
    delete_profile(profile_name)

if __name__ == '__main__':
    cli()
```