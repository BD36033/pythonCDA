from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Configuration de la base de données MySQL
DATABASE_URL = "mysql+pymysql://root@localhost:3306/ville"

# Création de l'engine et de la session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(BaseModel):
    id: int
    name: str
    email: str


# Modèle SQLAlchemy correspondant à la table commune
class Commune(Base):
    __tablename__ = 'communes'
    
    code_commune = Column(Integer, primary_key=True)
    code_region = Column(String(10))
    nom_region = Column(String(100))
    code_departement = Column(String(10))
    code_arrondissement = Column(Integer)
    code_canton = Column(Integer)
    nom_commune = Column(String(255))  # Colonne à afficher
    population_municipale = Column(Integer)
    population_comptee_a_part = Column(Integer)
    population_totale = Column(Integer)
    annee_recensement = Column(Integer)
    annee_utilisation = Column(Integer)
    code_insee = Column(String(15))
    superficie = Column(Float)
    statut = Column(String(50))
    code_insee_commune = Column(String(15))
    nom_commune_ign = Column(String(255))
    nom_departement_ign = Column(String(255))
    nom_region_1 = Column(String(100))
    code_epci = Column(String(15))
    code_epci_1 = Column(String(15))
    epci = Column(String(100))

# Modèle SQLAlchemy correspondant à la table ville (si nécessaire)
class Ville(Base):
    __tablename__ = 'ville'
    
    code_commune = Column(Integer, primary_key=True)
    nom_commune = Column(String(255))
    population_municipale = Column(Integer)
    code_region = Column(String(10))
    nom_region = Column(String(100))
    code_departement = Column(String(10))
    superficie = Column(Float)

# Créez les tables dans la base de données (si nécessaire)
Base.metadata.create_all(bind=engine)

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

# Route principale pour récupérer les villes ou communes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    # Récupérer les villes de la base de données
    villes = db.query(Ville).all()  # Utilisez ici Ville
    communes = db.query(Commune).all()  # Vous pouvez également récupérer les communes
    return templates.TemplateResponse("index.html", {"request": request, "villes": villes, "communes": communes})

# Si vous souhaitez accéder directement à index.html via /static
@app.get("/static/index", response_class=HTMLResponse)
async def get_static_index():
    with open("static/index.html") as f:
        return f.read()

@app.post("/users/")
def create_user(user: User):
    return {
        "message": f"Utilisateur {user.name} créé avec succès !",
        "data": user.dict()
    }