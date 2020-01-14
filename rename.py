import click
from operation import Operation



# group all commands
@click.group()
def main():
    pass

@main.command()
@click.option('--path',prompt='Type desired path', required=True, type=str)
def readdir(path):
    Operation.read(path)


if __name__=="__main__":
    main()