from pydantic import BaseModel


class AccidentData(BaseModel):
    """Input data model for accident prediction.

    Contains user-friendly field names exposed in the API.
    """
    age_usager: float
    vitesse_max_autorisee: float
    nombre_de_voies: int
    ceinture_ou_casque_attache: bool
    en_agglomeration: bool
    collision_frontale: bool
    sexe_masculin: bool = True
    luminosite_pleine_nuit: bool = False
    meteo_normale: bool = True


class PredictionOutput(BaseModel):
    """Output data model for accident prediction results.

    Contains gravity code, French label and probability distribution.
    """
    gravite_code: int
    label_francais: str
    probabilites: dict[str, float]
