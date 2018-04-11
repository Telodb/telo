import click
import hues
import os

from telo import init as initDB
from telo import conf as confDB


@click.group()
def main():
    pass


@main.command()
@click.option('--name', prompt=True, help='Database name')
@click.option('--path', default='./', help='Database path')
def init(name, path):
    '''Create initial database'''
    newDB = initDB.init(name=name, path=path)
    newDB.init()


@main.command()
@click.option(
    '-g', '--global', 'place', flag_value='global', help='use global config file'
)
@click.option(
    '-l', '--local', 'place', flag_value='local', help='use database config file'
)
@click.argument('key', nargs=1)
@click.argument('value', nargs=1)
def config(place, key, value):
    '''Set or get config'''
    confDB.put(place, key, value)


def echo(msg, priority=4):
    hues.log(msg)
