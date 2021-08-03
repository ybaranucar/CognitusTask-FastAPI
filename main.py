from fastapi import FastAPI, Request
from numpy.lib.function_base import i0
from algorithm import *

app = FastAPI()



@app.get("/train")
async def train():
    text, label = create_data()
    training, vectorizer = tfidf(text)
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(training, label, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    dump_model(model, 'model.pickle')
    dump_model(vectorizer, 'vectorizer.pickle')
    return "Train islemi basarili"


@app.post("/predict")
async def predict(request: Request):
    model = load_model('model.pickle')
    vectorizer = load_model('vectorizer.pickle')
    user_text = await request.body()
    tdifd = vectorizer.transform([user_text])
    result = model.predict_proba(tdifd)
    return {"Predict Result": result}
