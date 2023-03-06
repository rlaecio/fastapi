from datetime import date, time
from pydantic import BaseModel
from sqlalchemy import text


# class Movie(BaseModel):
#     id = int
#     name = str
#     desc = str
#     type = str
#     url = str
#     rating = str

#     class Config:
#         orm_mode = True


class Registo(BaseModel):
    
    id_r    = int
    data    = date
    hora    = time
    id_e    = int
    id_ur   = int
    obse    = text
    id_u    = int 
    nomep   = str
    telef   = str
    nomeoc  = str 
    telefoc = str 
    id_b    = int 
    bloco   = str
    entrada = str
    casa    = str 
    id_t    = int 
    obs     = text


    class Config:
        orm_mode = True

