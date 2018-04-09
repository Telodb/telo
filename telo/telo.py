import click
import hues
import os

from telo import init as initDB


@click.group()
def main():
    pass


@main.command()
@click.option('--name', prompt=True, help='Database name')
@click.option('--path', default='./', help='Database path')
def init(name, path):
    '''Create initial database'''
    newDB = initDB.init(name, path)
    newDB.init(name, path)

def echo(msg, priority=4):
    hues.log(msg)
