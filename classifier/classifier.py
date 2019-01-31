import numpy as np
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

from utils.utils import analyzer

TRAIN_SET_PATH = "data.txt"

encoding = "utf-8"

X, y = [], []
with open(TRAIN_SET_PATH, "r") as infile:
    for line in infile:
        label, text = line.lower().split(" ", 1)  # split input at first space
        X.append(text.split())
        y.append(label)
X, y = np.array(X), np.array(y)
print ("total examples %s" % len(y))

svc_tfidf = Pipeline(
    [("tfidf_vectorizer", TfidfVectorizer(analyzer=analyzer)), ("linear svc", SVC(kernel="linear", probability=True))])

# creating the model with the training data
svc_tfidf.fit(X, y)
joblib.dump(svc_tfidf, 'model.joblib')

model = joblib.load('model.joblib')
scores = cross_val_score(model, X, y, cv=5)
print(scores.mean(), scores.std())


'''
print(model.classes_)
print(model.predict_proba([
    ["how", "is", "the", "weather", "in", "israel"],
    ["how", "is", "the", "rain", "situation"],
    ["is", "it", "cold"],
    ["sunrise", "berlin"],
    ["dawn"],
    ["when", "does", "the", "moon", "come", "out"],
    ["when", "does", "the", "sun", "come", "out"]
]))

print(model.predict([
    ["how", "is", "the", "weather", "in", "israel"],
    ["how", "is", "the", "rain", "situation"],
    ["is", "it", "cold"],
    ["sunrise", "berlin"],
    ["dawn"]
]))
'''
