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
    email = Column(Text, nullable = False, unique=True)
    # relationship and backpopulate

    projects = relationship(
        "Project",
        secondary= Project_collaborations,
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
        "Project",
        secondary=Project_collaborations,
        back_populates="funding_agencies"
    )

    # creates the projects table, a project can have many sponsors and also many researchers
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(Text, nullable=False)
    start_date = Column(String, nullable=False)
    # relationships since both agency and researcher table relly on project fpr relationship, the project will have relationship for both
    researchers = relationship(
        "Researcher",
        secondary=Project_collaborations,
        back_populates="projects"

    )
    funding_agencies = relationship(
        "Funding_agency",
        secondary=Project_collaborations,
        back_populates="projects"

    )









  