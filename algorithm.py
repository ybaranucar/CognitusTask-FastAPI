import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn import cross_validation
from sklearn.svm import SVC
from sklearn.metrics import precision_score, accuracy_score, recall_score

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session 

from sqlalchemy import select

from pydantic import BaseModel

from typing import List
from databases import Database
from pydantic import BaseModel

  

def create_data():
    
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/postgres"
    database = Database(SQLALCHEMY_DATABASE_URI)
    cnx = create_engine(SQLALCHEMY_DATABASE_URI)    
    database.connect()
    df = pd.read_sql_query("SELECT * FROM app_data", con=cnx)
    return df['text'].tolist(), df['label'].tolist()


        
def get_places(db: Session):
    return db.query("app_data").all()


#feature extraction - creating a tf-idf matrix
def tfidf(data, ma = 0.6, mi = 0.0001):
    tfidf_vectorize = TfidfVectorizer()
    tfidf_data = tfidf_vectorize.fit_transform(data)
    return tfidf_data, tfidf_vectorize


#SVM classifier
def test_SVM(x_train, x_test, y_train, y_test):
    SVM = SVC(kernel = 'linear', probability=True)
    SVMClassifier = SVM.fit(x_train, y_train)
    predictions = SVMClassifier.predict(x_test)
    a = accuracy_score(y_test, predictions)
    p = precision_score(y_test, predictions, average = 'weighted')
    r = recall_score(y_test, predictions, average = 'weighted')
    return SVMClassifier, a, p, r



def dump_model(model, file_output):
    pickle.dump(model, open(file_output, 'wb'))

def load_model(file_input):
    return pickle.load(open(file_input, 'rb'))
	
	
# GET DATA
# file = "test_data.xlsx"
# text, label = create_data(file)

# # TRAIN
# training, vtraining, vectorizer = tfidf(text)
# x_train, x_test, y_train, y_test = cross_validation.train_test_split(training, label, test_size = 0.25, random_state = 0)
# model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
# dump_model(model, 'model.pickle')
# dump_model(vectorizer, 'vectorizer.pickle')

# # PREDICTION
# model = load_model('model.pickle')
# vectorizer = load_model('vectorizer.pickle')
# user_text = "whereafter"
# tdifd = vectorizer.transform([user_text])
# result = model.predict_proba(tfidf)
# print(result)
