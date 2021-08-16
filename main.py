from fastapi import FastAPI, Request
from algorithm import load_model
from celery_app.celery_tasks import train_task


app = FastAPI()


@app.get("/train")
def train():
    train_task.delay()
    return "Train islemi basarili"


@app.post("/predict")
async def predict(request: Request):
    model = load_model('model.pickle')
    vectorizer = load_model('vectorizer.pickle')
    user_text = await request.body()
    tdifd = vectorizer.transform([user_text])
    result = model.predict_proba(tdifd)
    return {"Predict Result": result}