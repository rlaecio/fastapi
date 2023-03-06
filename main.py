
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

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/registo")
async def lis_item(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(Registo).all()
    #return  records 
    return templates.TemplateResponse("index.html", {"request": request, "data": records})







