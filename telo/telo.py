import click
import hues
import os


@click.group()
def main():
    pass


@main.command()
@click.option('--name', prompt=True, help='Database name')
@click.option('--path', default='./', help='Database path')
def init(name, path):
    '''Create initial database'''
    abspath = os.path.abspath(path) + '/.telo'
    echo('Initialize empty telo database named {} in {} '.format(
        name, abspath))
    os.mkdir(abspath)




def echo(msg, priority=4):
    hues.log(msg)
