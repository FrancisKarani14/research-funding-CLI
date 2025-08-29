import click
from crud import (
    add_project,
    add_manager,
    add_funder,
    add_researcher,
    get_all_projects,
    get_all_researchers,
    get_all_funders,
    assign_researcher_to_project,
    assign_funder_to_project
)

# main loop
while True:
    click.secho("\n=== Welcome to Project Research APP ===", fg='yellow')
    click.secho("To proceed, select option", fg="green")
    click.secho("1. Project", fg="red")
    click.secho("2. Researcher", fg="red")
    click.secho("3. Funding Agency", fg="red")
    click.secho("4. Manager", fg="red")
    click.secho("5. Exit", fg="red")

    user_input = click.prompt("Select option", type=int)

    # ----------------- PROJECT MENU -----------------
    if user_input == 1:
        click.secho("\nProject Options", fg='yellow')
        click.secho("1. Add project", fg='yellow')
        click.secho("2. View projects", fg='yellow')
        click.secho("3. Assign researchers", fg='yellow')
        click.secho("4. Assign funding agencies", fg='yellow')

        project_option = click.prompt("Select option", type=int)

        if project_option == 1:
            title = click.prompt("Add project title")
            description = click.prompt("Add project description")
            start_date = click.prompt("Add project start_date")
            try:
                add_project(title, description, start_date)
                click.secho(f"{title} project has been added successfully")
            except Exception as e:
                click.secho(f"Error adding project {e}")

        if project_option == 2:
            click.secho("View projects", fg='yellow')
            projects = get_all_projects()
            for proj in projects:
                click.secho(
                    f"({proj[0]}) {proj[1]} - {proj[2]} ({proj[3]})", fg="green")

        if project_option == 3:
            click.secho("Assign Researcher to Project", fg="yellow")
            project_id = click.prompt("Enter Project ID", type=int)
            researcher_id = click.prompt("Enter Researcher ID", type=int)
            result = assign_researcher_to_project(project_id, researcher_id)
            click.secho(result, fg="green")

        if project_option == 4:
            click.secho("Assign Funding Agency to Project", fg="yellow")
            project_id = click.prompt("Enter Project ID", type=int)
            funder_id = click.prompt("Enter Funder ID", type=int)
            result = assign_funder_to_project(project_id, funder_id)
            click.secho(result, fg="green")

    # ----------------- RESEARCHER MENU -----------------
    if user_input == 2:
        click.secho("\nResearcher Options", fg="yellow")
        click.secho("1. Add researcher", fg="yellow")
        click.secho("2. View researchers", fg="yellow")

        researcher_option = click.prompt("Select option", type=int)

        if researcher_option == 1:
            name = click.prompt("Enter name")
            field_of_study = click.prompt("Enter the field_of_study")
            email = click.prompt("Enter researcher's email")
            add_researcher(name, field_of_study, email)
            click.secho("Researcher added successfully!", fg="green")

        if researcher_option == 2:
            click.secho("View researchers", fg="yellow")
            researchers = get_all_researchers()
            for r in researchers:
                click.secho(f"({r[0]}) {r[1]} {r[2]}", fg="green")

    # ----------------- FUNDER MENU -----------------
    if user_input == 3:
        click.secho("\nFunder Options", fg="yellow")
        click.secho("1. Add funder", fg="yellow")
        click.secho("2. View funders", fg="yellow")

        funder_option = click.prompt("Select option", type=int)

        if funder_option == 1:
            name = click.prompt("Enter funder name")
            country = click.prompt("Enter funder country", type=str)
            contact_email = click.prompt("Enter funder's email", type=str)
            add_funder(name, country, contact_email)
            click.secho("Funder added successfully!", fg="green")

        if funder_option == 2:
            click.secho("View funders", fg="yellow")
            funders = get_all_funders()
            for f in funders:
                click.secho(f"({f[0]}) {f[1]} - Budget: {f[2]}", fg="green")

    # ----------------- MANAGER MENU -----------------
    if user_input == 4:
        click.secho("\nManager Options", fg="yellow")
        click.secho("1. Add manager", fg="yellow")

        manager_option = click.prompt("Select option", type=int)

        if manager_option == 1:
            first_name = click.prompt("Enter first name")
            email = click.prompt("Enter email")
            add_manager(first_name, email)
            click.secho("Manager added successfully!", fg="green")

    # ----------------- EXIT -----------------
    if user_input == 5:
        click.secho("Exiting Project Research APP... Goodbye!", fg="cyan")
        break
