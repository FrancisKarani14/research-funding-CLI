from sqlalchemy import Integer, Text, Column, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.base import Base


# create an association table

class Project_collaboration(Base):
    __tablename__ = "project_collaborations"
    # id = Column(Integer, primary_key=True)
    researchers_id = Column(Integer, ForeignKey("researchers.id"), primary_key = True)
    agency_id = Column(Integer, ForeignKey(
        "funding_agencies.id"), primary_key=True)
    project_id = Column(Integer, ForeignKey(
        "projects.id"), primary_key=True)


   