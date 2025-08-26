from sqlalchemy import Integer, Column, String, VARCHAR, Text
from sqlalchemy.orm import relationship
from lib.models.associations import Project_collaborations
from lib.models.base import Base

# cretes a base to inherit from


# creates the researchers class that inherits from base
class Researcher(Base):
    __tablename__ = "researchers"
    # entities needed are id, name, field of study and email.
    id = Column(Integer, primary_key= True)
    name= Column(String, nullable=False, unique= True)
    field_of_study = Column(Text, nullable= False)
    email = Column(Text, nullable = False)
    # relationship and backpopulate

    projects = relationship(
        "Project",
        secondary= "project_collaborations",
        back_populates="researchers"
    )

# creates the funding agency class that will be used to create a table for the funding agencies in the db
class Funding_agency(Base):
    __tablename__ = "funding_agencies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    contact_email= Column(String, nullable=False, unique=True)
    # relationships an agency funds a project
    projects = relationship(
        "project",
        secondary="project_collaborations",
        back_populates="funding_agencies"
    )







