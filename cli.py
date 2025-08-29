import click
from crud import add_funder, add_project, add_manager, add_researcher

# cli creation

while True:
    click.secho("Welcome to project research APP", fg='yellow')
    click.secho("To proceed, select option", fg="green")
    click.secho("1project", fg="red")
    click.secho("1project", fg="red")
    click.secho("1project", fg="red")
    click.secho("1project", fg="red")

    user_input = click.prompt("select option", type=int)
    