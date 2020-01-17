import click
from operation import Operation

operation=Operation()

# group all commands
@click.group()
def main():
    pass

# list files in any directory
@main.command()
@click.option('--path',prompt='Type desired path', required=True, type=str)
def readdir(path):
    operation.read(path)

# list files in choice
@main.command()
@click.option('--path', prompt='Type desired path', required=True, type=str)
def list(path):
    operation.listType(path)


if __name__=="__main__":
    main()