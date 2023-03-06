from sqlalchemy import Date, Time
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base


# class Movie(Base):
    # __tablename__ = "Movie"
    # id = Column(Integer, primary_key=True, index=True)
    # name = Column(String(20), unique=True)
    # desc = Column(Text())
    # type = Column(String(20))
    # url = Column(String(100))
    # rating = Column(Integer)


class Registo(Base):
    __tablename__ = 'registos'

    id_r = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    id_e = Column(Integer, nullable=False)
    id_ur = Column(Integer, nullable=False)
    obse = Column(Text, nullable=False)
    id_u = Column(Integer, nullable=False)
    nomep = Column(String(100))
    telef = Column(String(50))
    nomeoc = Column(String(100), nullable=False)
    telefoc = Column(String(50), nullable=False)
    id_b = Column(Integer, nullable=False)
    bloco = Column(String(6), nullable=False)
    entrada = Column(String(6), nullable=False)
    casa = Column(String(6), nullable=False)
    id_t = Column(Integer, nullable=False)
    obs = Column(Text)
