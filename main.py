import click
import shlex
import re

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
        deadline = helper.change_format(deadline)
        tsk.add(task, deadline)
        click.echo(f">task {task} is append.\n")

    else:
        click.echo('>>wrong format for date =>> yyyy/mm/dd')


#command remove

@cli.command()
@click.option('--id', prompt=">Enter task's id: ", help='this option taken task\'s id for deleting the task.', type=int)
def remove(id):
    result = tsk.remove(id)
    if result:
        click.echo(f'task {id} is removed\n')


#command edit

@cli.command()
@click.option('--id', prompt=">Enter task's id: ", help='this option taken task\'s id for deleting the task.', type=int)
@click.option('--task', required=False, help='use it for rename task.', type=str)
@click.option('--deadline', required=False, help='use it for changing deadline.', type=str)
@click.option('--complete', required=False, help='use it for complete the task.', type=bool)
def edit(id, task=None, deadline=None, complete=None):
    result = tsk.edit(id, task, deadline, complete)
    if result:
        click.echo(f'task {id} is edited.\n')


#command list

@cli.command()
@click.option('--desc', is_flag=True, help='this option descending tasks.')
def List(desc):

    tsk.List(desc)


#command complete

@cli.command()
@click.option('--id', prompt=">Enter task's id: ", type=int)
def complete(id):
    result = tsk.complete(id)
    if result:
        click.echo(f'>task {id} is complete.\n')

#command today

@cli.command()
def today():
    tsk.today() 



def shell():
    while(True):
        try:
            command = input('>>>').strip()
            args = shlex.split(command)

            if args[0] == 'quit':
                break
            if args[0] == 'clear':
                click.clear()
                continue

            cli(args, standalone_mode=False)
        except Exception as Error:
            print(f'>>had Error: {Error}.')


if __name__ == '__main__':
    shell()