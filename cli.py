import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# adjust names if needed
from lib.models.models import Base, Project, Researcher, Manager, FundingAgency

# Use the existing Alembic database
DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


@click.group()
def cli():
    """Research Funding CLI"""


# ---------------- Projects ----------------
@cli.command("add-project")
@click.option("--title", prompt="Project title", help="Title of the project")
@click.option("--description", prompt="Project description", help="Description of the project")
def add_project(title, description):
    """Add a new project"""
    project = Project(title=title, description=description)
    session.add(project)
    session.commit()
    click.echo(f"✅ Project '{title}' added successfully!")


# ---------------- Researchers ----------------
@cli.command("add-researcher")
@click.option("--first-name", prompt="First name")
@click.option("--last-name", prompt="Last name")
def add_researcher(first_name, last_name):
    """Add a new researcher"""
    researcher = Researcher(first_name=first_name, last_name=last_name)
    session.add(researcher)
    session.commit()
    click.echo(f"✅ Researcher {first_name} {last_name} added successfully!")


# ---------------- Managers ----------------
@cli.command("add-manager")
@click.option("--first-name", prompt="First name")
@click.option("--last-name", prompt="Last name")
def add_manager(first_name, last_name):
    """Add a new manager"""
    manager = Manager(first_name=first_name, last_name=last_name)
    session.add(manager)
    session.commit()
    click.echo(f"✅ Manager {first_name} {last_name} added successfully!")


# ---------------- Funders ----------------
@cli.command("add-funder")
@click.option("--name", prompt="Funder name")
@click.option("--budget", prompt="Funder budget", type=float)
def add_funder(name, budget):
    """Add a new funding agency"""
    funder = FundingAgency(name=name, budget=budget)
    session.add(funder)
    session.commit()
    click.echo(
        f"✅ Funding agency '{name}' with budget {budget} added successfully!")


if __name__ == "__main__":
    cli()
