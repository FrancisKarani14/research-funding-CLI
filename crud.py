from models import Researcher, Funding_agency, Manager, Project, session


def add_researcher(first_name, last_name):
    """Add a new researcher"""
    researcher = Researcher(first_name=first_name, last_name=last_name)
    session.add(researcher)
    session.commit()


def add_project(researchers_name, title, description, start_date):
    researcher = session.query(Researcher).filter(Researcher.name == researchers_name).first()
    project = Project(title=title,researcher = researcher, description=description, start_date= start_date)
    session.add(project)
    session.commit()
# add_project("Morris", "AI", "how to dhfsdkn  ksdfbsdc m mksbcmsd  ksdcbic", "12-3-2025")





def add_manager(first_name, last_name):
    """Add a new manager"""
    manager = Manager(first_name=first_name, last_name=last_name)
    session.add(manager)
    session.commit()


def add_funder(name, budget):
    """Add a new funding agency"""
    funder = Funding_agency(name=name, budget=budget)
    session.add(funder)
    session.commit()
