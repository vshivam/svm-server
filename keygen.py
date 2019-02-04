from app.models import APIKey
from app import create_app
from app import db

app = create_app()
db.init_app(app)

def generate_new_key():
    with app.app_context():
        key = APIKey()
        key.save_to_db()
        print key.str

def show_keys():
    with app.app_context():
        for key in APIKey.query.all():
            print key.str


if __name__ == '__main__':
   # generate_new_key()
   show_keys()
