from sql_app import crud
from sql_app.database import SessionLocal
from algorithm import tfidf, test_SVM, dump_model
from sklearn import cross_validation
from .celery_worker import celery


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@celery.task
def train_task(skip: int = 0, limit: int = 100):
    db = SessionLocal()
    users = crud.get_all_data(db, skip=skip, limit=limit)
    # text = crud.get_text(db)[0][0]
    text_list = []
    label_list = []
    for i in range (len(users)):
        text_list.append(users[i].text)
        label_list.append(users[i].label)     
    training, vectorizer = tfidf(text_list)
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(training, label_list, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    dump_model(model, 'model.pickle')
    dump_model(vectorizer, 'vectorizer.pickle')
    return "Train islemi basarilii"