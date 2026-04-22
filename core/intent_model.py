import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# load dataset
data = pd.read_csv("data/intent_dataset.csv")

X = data["text"]
y = data["intent"]


vectorizer = TfidfVectorizer()

X_vec = vectorizer.fit_transform(X)


model = LogisticRegression()

model.fit(X_vec, y)


pickle.dump(model, open("ml_models/intent_model.pkl", "wb"))
pickle.dump(vectorizer, open("ml_models/vectorizer.pkl", "wb"))

print("Model trained and saved!")