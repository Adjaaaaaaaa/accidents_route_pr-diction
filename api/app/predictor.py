import os

import joblib
import pandas as pd


class AccidentPredictor:
    """Predict accident gravity using XGBoost model."""

    def __init__(self):
        """Initialize the predictor with the pre-trained model."""
        # Path to the multi-class model
        model_path = os.path.join(
            os.path.dirname(__file__), "..", "data_models", "model_multi_xgb.joblib"
        )
        self.pipeline = joblib.load(model_path)
        self.labels = {1: "Indemne", 2: "Tué", 3: "Grave", 4: "Léger"}

    def predict(self, user_data: dict):
        """Predict accident gravity from user input data.

        Args:
            user_data (dict): Dictionary containing user input features

        Returns:
            dict: Prediction results with gravity code, label and probabilities
        """
        # 1. Calculate internal variables expected by the model
        internal_data = {
            "age": user_data["age_usager"],
            "vma": user_data["vitesse_max_autorisee"],
            "nbv": user_data["nombre_de_voies"],
            # Recalculate important features identified during Feature Engineering
            "vitesse_x_collision": user_data["vitesse_max_autorisee"]
            if user_data["collision_frontale"]
            else 0,
            "age_x_securite": user_data["age_usager"]
            if user_data["ceinture_ou_casque_attache"]
            else 0,
            "agglo_x_vitesse": user_data["vitesse_max_autorisee"]
            if user_data["en_agglomeration"]
            else 0,
            # Dummy mapping
            "sexe_2": 0 if user_data["sexe_masculin"] else 1,
            "agg_2": 1 if user_data["en_agglomeration"] else 0,
            "lum_3": 1 if user_data["luminosite_pleine_nuit"] else 0,
        }

        # 2. Create DataFrame and align columns
        df = pd.DataFrame([internal_data])
        expected_columns = self.pipeline.feature_names_in_
        for col in expected_columns:
            if col not in df.columns:
                df[col] = 0
        df = df[expected_columns]

        # 3. Prediction and index conversion (0-3 -> 1-4)
        prediction_idx = self.pipeline.predict(df)[0]
        real_gravity = int(prediction_idx + 1)

        # 4. Calculate probabilities by modality
        probs = self.pipeline.predict_proba(df).tolist()[0]

        return {
            "gravite_code": real_gravity,
            "label_francais": self.labels.get(real_gravity, "Inconnu"),
            "probabilites": {
                self.labels[i + 1]: round(probs[i], 4) for i in range(len(probs))
            },
        }


predictor = AccidentPredictor()
