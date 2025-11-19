import click
import shlex
from prettytable import PrettyTable

from Todo import Task
import helper, storage


@click.group()
def cli():
    pass


tsk = Task()

# command add
@cli.command(help="(run add --help) You can add task => add (-t, --task) 'task1' (-d, --deadline) 1404/08/24")
@click.option("--task", '-t', prompt="> Enter task name", required=True)
@click.option("--deadline", "-d", prompt="> Enter deadline for task(yyyy/mm/dd)", required=True)
def add(task, deadline):

    task = task.strip()
    deadline = deadline.strip()

    deadline = helper.check_date(deadline)
    if deadline:
        result = tsk.add(task, deadline)
        if result:
            click.echo("> Task successfuly added.")

# command remove
@cli.command(help="(run remove --help) You can remvoe a task => remove --id 1| run remove --help")
@click.option("--id",prompt="> Enter task's id",help="this option taken task's id for deleting the task.", type=int)
def remove(id):
    if id:
        result = tsk.remove(id)
        if result:
            return True


# command list
@cli.command(help="(run list --help) You can list of your task => list --options run | list --help")
@click.option("--desc", is_flag=True, help="this option descending tasks. list --desc")
@click.option("--complete", is_flag=True, help="this option show complete tasks. list --complete")
@click.option("--incomplete", is_flag=True, help="this option show incomplete tasks. list --incomplete")
@click.option("--deadline", is_flag=True, help="this option show task by deadline. list --deadline")
def List(desc, complete, incomplete, deadline):
    data = tsk.List(desc, complete, incomplete, deadline)

    mytable = PrettyTable(['ID', 'TASK', 'DEADLINE', 'TIME_LEFT', 'COMPLETE'])
    for item in data:
        time_left = helper.time_left(item['deadline'])

        mytable.add_row([item['id'], item['task'], item['deadline'], time_left if type(time_left) is str else f"{time_left} day is remains.", item['complete']])
    click.echo(mytable)


# command edit
@cli.command(help="(run edit --help) You can edit your task.")
@click.option("--id", prompt="> Enter task's id", type=int)
@click.option("--task", "-t", required=False, type=str)
@click.option("--deadline", '-d', required=False, type=str)
@click.option("--complete", '-c', required=False, type=bool)
def edit(id, task, deadline, complete):
    if tsk.edit(id, task, deadline, complete):
        click.echo("task is successfuly changed")




# command complete
@cli.command(help="(run complete --help) You can change the complete value to True => complete --id 1 run | complete --help")
@click.option("--id", prompt=">Enter task's id: ", type=int)
def complete(id):
    result = tsk.complete(id)
    if result:
        click.echo(f">task {id} is complete.\n")


def shell():
    click.clear()
    click.secho("Todo_cli".center(50, ' '), bold=True, fg="blue", bg='magenta')
    click.echo("""\nA simple command-line based todo application written in Python.\nIt supports task management features like add, edit, remove, complete, and list with Persian (Jalali) calendar support using `jdatetime`.
    """)
    click.secho("\nHelp: ", bold=True)
    cli(['--help'], standalone_mode=False)
    while True:

        try:
            command = input("\n>>> ").strip()
            args = shlex.split(command)

            if args[0] == "quit":
                break
            if args[0] == "clear":
                click.clear()
                continue

            cli(args, standalone_mode=False)
        except Exception as Error:
            click.secho(f"Had Error: {Error}", fg='red', bold=True)


if __name__ == "__main__":
    shell()
