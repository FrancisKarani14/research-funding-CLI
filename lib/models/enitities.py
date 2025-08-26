from sqlalchemy import Integer, Column, String, VARCHAR, Text
from sqlalchemy.orm import declarative_base, relationship
from lib.models.associations import Project_collaborations

# cretes a base to inherit from
Base = declarative_base()

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
    )





