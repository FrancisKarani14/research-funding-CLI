from sqlalchemy import create_engine
from lib.models.base import Base
from lib.models.associations import Project_collaboration
from lib.models.entities import Researcher, Project, Funding_agency

# Create engine
engine = create_engine("sqlite:///research.db", echo=True)
Base.metadata.create_all(engine)