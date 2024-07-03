import click


@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', default='Dinar', help='Please write your name')
def hi(name):
    """Hi command dimed_2"""
    click.echo(f'Hi, {name}! Dimed_2')

if __name__ == '__main__':
    cli()
