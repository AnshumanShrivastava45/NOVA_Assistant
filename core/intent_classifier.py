import pickle

model = pickle.load(open("ml_models/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("ml_models/vectorizer.pkl", "rb"))

def predict_intent(text):

    text_vec = vectorizer.transform([text])
    probs = model.predict_proba(text_vec)[0]
    confidence = max(probs)
    
    intent = model.classes_[probs.argmax()]
    return intent, confidence