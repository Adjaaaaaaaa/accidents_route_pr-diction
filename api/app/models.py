from pydantic import BaseModel, Field

class InputData(BaseModel):
    # Variables de base
    age: int = Field(..., example=25)
    vma: int = Field(..., example=80)
    agg: int = Field(..., example=2)
    atm: int = Field(..., example=1)
    col: int = Field(..., example=1)
    catr: int = Field(..., example=3)
    lum: int = Field(..., example=1)
    surf: int = Field(..., example=1)
    situ: int = Field(..., example=1)
    nbv: str = Field(..., example="2")
    moment_journee: str = Field(..., example="jour")
    
    # Utilisation de l'alias pour la colonne 'int' requise par le modèle
    int_val: int = Field(..., alias="int", example=1) 
    is_weekend: int = Field(..., example=0)
    
    # Autres variables techniques
    motor: int = Field(..., example=1)
    plan: int = Field(..., example=1)
    mois: int = Field(..., example=6)
    obsm: int = Field(..., example=0)
    senc: int = Field(..., example=1)
    catv: int = Field(..., example=7)
    an_nais: int = Field(..., example=1994)
    circ: int = Field(..., example=2)
    manv: int = Field(..., example=1)
    secu1: int = Field(..., example=1)
    catu: int = Field(..., example=1)
    sexe: int = Field(..., example=1)
    an: int = Field(..., example=2024)
    place: int = Field(..., example=1)
    jour: int = Field(..., example=12)
    trajet: int = Field(..., example=1)
    is_work_trip: int = Field(..., example=0)
    prof: int = Field(..., example=1)
    meteo_degradee: int = Field(..., example=0)
    choc: int = Field(..., example=1)

    class Config:
        # Permet à FastAPI et Pydantic d'utiliser les alias dans les dictionnaires
        populate_by_name = True 

class OutputData(BaseModel):
    prediction: float