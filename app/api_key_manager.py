from app.models import APIKey
from app import create_app
from app import db


def generate_new_key():
    key = APIKey()
    print key.str
    return key


def show_keys():
    for key in APIKey.query.all():
        print key.str


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.init_app(app)
        # generate_new_key().save_to_db()
        show_keys()
