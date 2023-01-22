from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String, sql

from .database import Base


class DataDefinition(Base):
    __tablename__ = "data_definition"
    id = Column('data_def_id', Integer, primary_key=True)
    data_endpoint = Column(String)
    data_method = Column(String)
    data_schema = Column(JSON)


class DataIngestRecord(Base):
    __tablename__ = "data_ingest_records"
    id = Column('data_ing_id', Integer, primary_key=True)
    data_ingest = Column(String)
    data_def_id = Column(Integer, ForeignKey('data_definition.data_def_id'))
    created_time  = Column(DateTime(timezone=True), default=sql.func.now())
