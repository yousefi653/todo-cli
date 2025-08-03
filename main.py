import click
import shlex

from Todo import Task
import helper, storage

@click.group()
def cli():
    pass


tsk = Task()

# command add 

@cli.command()
@click.argument("task")
@click.argument("deadline")
def add(task, deadline):
    if helper.check_date(deadline):
            
        tsk.add(task, deadline)
        click.echo(f">task {task} is append.\n")
    else:
        click.echo('>wrong format for date =>> yyyy/mm/dd')

#command remove

@cli.command()
@click.argument('id')
def remove(id):
    id = int(id)
    tsk.remove(id)
    click.echo(f'task {id} is removed')


#command edit

# @cli.command()
# @click.argument('id')
# def edit(id):
#     tsk.edit(id)


#command list

@cli.command()
@click.option('--desc', is_flag=True, help='this option descending tasks.')
def List(desc):

    tsk.List(desc)


#command complete

@cli.command()
@click.argument('id')
def complete(id):
    id = int(id)
    tsk.complete(id)
    click.echo(f'task {id} is complete.')


def shell():
    while(True):
        try:
            command = input('>>>').strip()
            if 'quit' in command:
                break
            args = shlex.split(command)
            cli(args, standalone_mode=False)
        except Exception as Error:
            print(f'had Error: {Error}.')


if __name__ == '__main__':
    shell()