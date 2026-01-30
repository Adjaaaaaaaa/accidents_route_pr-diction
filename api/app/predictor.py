import joblib
import pandas as pd
import os
import logging
from .models import InputData

# Configuration du logging pour suivre le chargement
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Détermination du chemin vers le fichier de pipeline sauvegardé
current_dir = os.path.dirname(os.path.abspath(__file__))
# Assurez-vous que le nom correspond à ce que vous sauvegardez dans le notebook
model_path = os.path.join(current_dir, "..", "data_models", "model_xgb.joblib")

model = None

try:
    # On charge le pipeline complet (Preprocessing + XGBoost)
    model = joblib.load(model_path)
    logging.info(f"Pipeline chargé avec succès depuis : {model_path}")
except Exception as e:
    logging.error(f"ERREUR lors du chargement du pipeline : {e}")
    # Ne pas lever d'exception ici pour permettre au serveur de démarrer, 
    # mais predict() échouera proprement.
def predict(data: InputData):
    if model is None:
        raise RuntimeError("Modèle non chargé")

    try:
        # CRUCIAL : Utilisez model_dump(by_alias=True) pour que 'int_val' devienne 'int'
        # Si vous utilisez une ancienne version de Pydantic, utilisez data.dict(by_alias=True)
        data_dict = data.model_dump(by_alias=True)
        
        input_df = pd.DataFrame([data_dict])

        # Le pipeline trouvera maintenant la colonne 'int'
        prediction = model.predict(input_df)[0]
        return float(prediction)

    except Exception as e:
        raise RuntimeError(f"Échec de la prédiction : {str(e)}")