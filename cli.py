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
    if user_input == 1:
        click.secho("project options", fg='yellow')
        click.secho("Add project", fg='yellow')
        click.secho("view projects", fg='yellow')
        click.secho("Assign researchers", fg='yellow')
        click.secho("Assign funding agencies", fg='yellow')
        
        project_option = click.prompt("select option", type=int)

        if project_option == 1:
            click.secho("Adding a new project")
            title = click.prompt("Add project title")
            description = click.prompt("Add project description")
            start_date = click.prompt("Add project start_date")
            try:
                add_project(title, description)
                click.secho(f"{title}project has been added successfully")
            except Exception as e:
                click.secho(f"error adding project {e}")

        if project_option ==2:
            
        
          
