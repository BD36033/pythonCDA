from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# # Configuration de la base de données MySQL
# DATABASE_URL = "mysql+pymysql://root@localhost:3306/ville"

# # Création de l'engine et de la session
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


# # Créez les tables dans la base de données (si nécessaire)
# Base.metadata.create_all(bind=engine)


# URL de connexion pour la base de données spam
DATABASE_URL_SPAM = "mysql+pymysql://root@localhost:3306/spam"
# URL de connexion pour la base de données ville
DATABASE_URL_VILLE = "mysql+pymysql://root@localhost:3306/ville"

# Création de l'engine et de la session pour la base spam
engine_spam = create_engine(DATABASE_URL_SPAM)
SessionLocalSpam = sessionmaker(autocommit=False, autoflush=False, bind=engine_spam)

# Création de l'engine et de la session pour la base ville
engine_ville = create_engine(DATABASE_URL_VILLE)
SessionLocalVille = sessionmaker(autocommit=False, autoflush=False, bind=engine_ville)


# Initialisation de FastAPI
app = FastAPI()

# Montée du répertoire static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuration des templates Jinja2
templates = Jinja2Templates(directory="templates")

# Dépendance pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    # Récupérer les villes de la base de données
    villes = db.query(Ville).all()
    return templates.TemplateResponse("index.html", {"request": request, "villes": villes})

# Si vous souhaitez accéder directement à index.html via /static
@app.get("/static/index", response_class=HTMLResponse)
async def get_static_index():
    with open("static/index.html") as f:
        return f.read()
