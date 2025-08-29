from models import Researcher, Funding_agency, Manager, Project, session


def add_project(researchers_name, title, description, start_date):
    researcher = session.query(Researcher).filter(
        Researcher.name == researchers_name).first()
    project = Project(
        title=title,
        researcher=researcher,
        description=description,
        start_date=start_date
    )
    session.add(project)
    session.commit()


def add_researcher(first_name, field_of_study, email):
    """Add a new researcher"""
    researcher = Researcher(first_name=first_name, field_of_study=field_of_study, email = email)
    session.add(researcher)
    session.commit()


def add_manager(first_name, email):
    """Add a new manager"""
    manager = Manager(first_name=first_name, email=email)
    session.add(manager)
    session.commit()


def add_funder(name, country, contact_email):
    """Add a new funding agency"""
    funder = Funding_agency(name=name, country=country, contact_email = contact_email)
    session.add(funder)
    session.commit()


def get_all_projects():
    """Return all projects as a list of tuples (id, title, description, start_date)"""
    projects = session.query(Project).all()
    return [(p.id, p.title, p.description, p.start_date) for p in projects]


def get_all_funders():
    """Return all funders as (id, name, budget)"""
    funders = session.query(Funding_agency).all()
    return [(f.id, f.name, f.country, f.contact_email) for f in funders]

def get_all_researchers():
    """Return all researchers as (id, first_name, last_name)"""
    researchers = session.query(Researcher).all()
    return [(r.id, r.first_name, r.field_of_study, r.email) for r in researchers]


def assign_researcher_to_project(project_id: int, researcher_id: int):
    """Assign a researcher to a project"""
    project = session.query(Project).get(project_id)
    researcher = session.query(Researcher).get(researcher_id)

    if not project or not researcher:
        return f"Project or Researcher not found."

    project.researchers.append(researcher)
    session.commit()
    return f"Researcher {researcher.first_name} assigned to project {project.title}."


def assign_funder_to_project(project_id: int, funder_id: int):
    """Assign a funding agency to a project"""
    project = session.query(Project).get(project_id)
    funder = session.query(Funding_agency).get(funder_id)

    if not project or not funder:
        return f"Project or Funding Agency not found."

    project.funders.append(funder)
    session.commit()
    return f"Funding Agency {funder.name} assigned to project {project.title}."
