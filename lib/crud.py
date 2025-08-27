from models.models import Researcher, Funding_agency, Manager, Project, session

def add_researcher(name, field_of_study, email):
    researcher = Researcher(name=name, field_of_study = field_of_study, email = email)
    session.add(researcher)
    session.commit()
# add_researcher("Morris", "se", "morris@gmail.com")

def add_project(researchers_name, title, description, start_date):
    researcher = session.query(Researcher).filter(Researcher.name == researchers_name).first()
    project = Project(title=title,researcher = researcher, description=description, start_date= start_date)
    session.add(project)
    session.commit()
# add_project("Morris", "AI", "how to dhfsdkn  ksdfbsdc m mksbcmsd  ksdcbic", "12-3-2025")
