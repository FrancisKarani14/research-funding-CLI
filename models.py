from sqlalchemy import Integer, Column, String, Text, create_engine, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
# from lib.models.associations import Project_collaboration

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
session = sessionmaker(bind=engine)()

# cretes a base to inherit from


# creates the researchers class that inherits from base
class Researcher(Base):
    __tablename__ = "researchers"
    # entities needed are id, name, field of study and email.
    id = Column(Integer, primary_key= True)
    name= Column(String, nullable=False, unique= True)
    field_of_study = Column(String, nullable= False)
    email = Column(String, nullable = False, unique=True)
    project = relationship("Project", back_populates="researcher")

   

# creates the funding agency class that will be used to create a table for the funding agencies in the db
class Funding_agency(Base):
    __tablename__ = "funding_agencies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    contact_email= Column(String, nullable=False, unique=True)
    collaboration = relationship("Collaboration", back_populates="funding_agency")
    

    # creates the projects table, a project can have many sponsors and also many researchers
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    researchers_id = Column(Integer, ForeignKey("researchers.id"))
    title = Column(String, nullable=False, unique=True)
    description = Column(Text, nullable=False)
    start_date = Column(String, nullable=False)
    researcher = relationship("Researcher", back_populates="project")
    collaboration = relationship("Collaboration", back_populates="project")

    

   

    # create the manager table
class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable= False)
    email = Column(String, unique= True)
    collaboration = relationship("Collaboration", back_populates="manager")

class Collaboration(Base):
    __tablename__ ="collaborations"
    id = Column(Integer, primary_key= True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    funding_agency_id = Column(Integer, ForeignKey("funding_agencies.id"))
    manager_id = Column(Integer, ForeignKey("managers.id"))
    project = relationship("Project", back_populates="collaboration")
    funding_agency = relationship("Funding_agency", back_populates="collaboration")
    manager = relationship("Manager", back_populates="collaboration")









  