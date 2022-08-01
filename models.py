import pickle
import os

abs_path = os.path.dirname(__file__)
classification_model_path = os.path.join(abs_path, "model", "classification_pipeline.pkl")
# regression_model_path = os.path.join(abs_path, "model", "regression_pipeline.pkl")
regression_model_path = rf"{abs_path}/model/regression_pipeline.pkl"

with open(classification_model_path, "rb") as f:
    classification_model = pickle.load(f)

with open(regression_model_path, "rb") as f:
    regression_model = pickle.load(f)
