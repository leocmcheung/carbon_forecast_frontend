
import streamlit as st
import pickle
import pandas as pd
import os
from xgboost import XGBRegressor, Booster
import xgboost as xgb
import numpy as np
import joblib

filepath = os.path.abspath("model/X_2.csv")
modelpath = os.path.abspath("model/test3.sav")
st.title("Another page")

## load pickle
# loaded = XGBRegressor()
# with open(modelpath,"rb") as f:
#     loaded = Booster.load_model(f)
model = XGBRegressor()
model.load_model("model/test.json")
# loaded = joblib.load(modelpath)
st.write(type(model))
## enter input as boxes ideally but can just use one line of our data first
X_test = pd.read_csv(filepath)
X_2 = np.array(X_test).reshape(1,468)
st.write(X_2)
## do predict
result = model.predict(X_2)
## print output
st.write(result)
