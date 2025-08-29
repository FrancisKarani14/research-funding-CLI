from sqlalchemy import Integer, Column, String, Text, create_engine, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
session = sessionmaker(bind=engine)()

# ---------------- Association Tables ---------------- #

# Projects <-> Researchers
project_researcher = Table(
    "project_researcher",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("researcher_id", Integer, ForeignKey(
        "researchers.id"), primary_key=True)
)

# Projects <-> Funding Agencies
project_funder = Table(
    "project_funder",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("funder_id", Integer, ForeignKey(
        "funding_agencies.id"), primary_key=True)
)

# ---------------- Models ---------------- #

# Researchers table


class Researcher(Base):
    __tablename__ = "researchers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    field_of_study = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    # many-to-many with projects
    projects = relationship(
        "Project", secondary=project_researcher, back_populates="researchers")


# Funding agencies table
class Funding_agency(Base):
    __tablename__ = "funding_agencies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    contact_email = Column(String, nullable=False, unique=True)

    # many-to-many with projects
    projects = relationship(
        "Project", secondary=project_funder, back_populates="funders")

    # still link through collaborations if you want manager involvement
    collaboration = relationship(
        "Collaboration", back_populates="funding_agency")


# Projects table
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(Text, nullable=False)
    start_date = Column(String, nullable=False)

    # many-to-many links
    researchers = relationship(
        "Researcher", secondary=project_researcher, back_populates="projects")
    funders = relationship(
        "Funding_agency", secondary=project_funder, back_populates="projects")

    # still support collaborations
    collaboration = relationship("Collaboration", back_populates="project")


# Managers table
class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

    collaboration = relationship("Collaboration", back_populates="manager")


# Collaboration table (links project <-> funder <-> manager)
class Collaboration(Base):
    __tablename__ = "collaborations"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    funding_agency_id = Column(Integer, ForeignKey("funding_agencies.id"))
    manager_id = Column(Integer, ForeignKey("managers.id"))

    project = relationship("Project", back_populates="collaboration")
    funding_agency = relationship(
        "Funding_agency", back_populates="collaboration")
    manager = relationship("Manager", back_populates="collaboration")
