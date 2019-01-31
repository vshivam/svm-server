import os

from flask import request
from flask_api import FlaskAPI, status
from flask_sqlalchemy import SQLAlchemy
from sklearn.externals import joblib

db = SQLAlchemy()


def pre_process(text):
    # convert multiple space to a single space
    return (' '.join(text.split())).split(' ')


def create_app():
    from app.models import APIKey

    db_path = os.path.join(os.path.dirname(__file__), 'app.db')
    db_uri = 'sqlite:///{}'.format(db_path)

    model_path = "../classifier/model.joblib"
    model_path = os.path.join(os.path.dirname(__file__), model_path)
    model = joblib.load(model_path)

    app = FlaskAPI(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route("/", methods=['GET'])
    def hello():
        return {
                   'success': True
               }, status.HTTP_200_OK

    @app.route("/classify", methods=['POST'])
    def classify():
        if request.method == "POST":
            request_key = request.args.get("api_key")
            api_key = APIKey.query.filter(APIKey.str == request_key).first()
            if api_key is None:
                return {
                           'success': False,
                           'message': 'Invalid or missing api_key'
                       }, status.HTTP_401_UNAUTHORIZED
            utterance = request.args.get("utterance")
            need_probs = request.args.get("needProbs")
            need_probs = need_probs == "True" or need_probs == "true"
            if utterance is None:
                return {
                    'success': False,
                    'message': 'missing POST param: utterance'
                }
            text = pre_process(utterance.strip())
            predict = model.predict([input])
            output = {
                'success': True,
                'utterance': utterance,
                'class': predict[0],
            }
            if need_probs:
                probs = model.predict_proba([text])
                output['probs'] = {}
                for i, class_ in enumerate(model.classes_):
                    output['probs'][class_] = probs[0][i] * 100
            return output, status.HTTP_200_OK

    return app
