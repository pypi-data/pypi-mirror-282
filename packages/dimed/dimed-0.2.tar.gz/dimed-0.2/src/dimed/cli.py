import click
import cookiecutter.main
import pkg_resources

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', default='Dinar', help='Please write your name')
def hi(name):
    """Hi command"""
    click.echo(f'Hi, {name}!')

@cli.command()
@click.option('--age', default=36, help='Please provide your age')
def retired(age):
    """When will you be retired"""
    click.echo(f'You will be retired in {60-age} years')

@cli.command()
def template():
    """Generate a project from template."""
    template_path = pkg_resources.resource_filename(__name__, "template")
    cookiecutter.main.cookiecutter(template_path)

if __name__ == '__main__':
    cli()
