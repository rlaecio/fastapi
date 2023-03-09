
from fastapi import FastAPI
from database import SessionLocal, engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,  Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

from starlette.responses import RedirectResponse
from model import Registo
import model

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}


@app.get("/registo")
async def lis_item(db: Session = Depends(get_database_session)):
    registos = db.query(Registo).all()
    return  registos 
    

@app.get("/principal", response_class=HTMLResponse)
async def lis_item(request: Request, db: Session = Depends(get_database_session)):
    registos = db.query(Registo).all()
    #return  records 
    return templates.TemplateResponse("principal.html", {"request": request, "data": registos })





