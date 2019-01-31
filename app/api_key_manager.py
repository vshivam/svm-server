from app.models import APIKey


def generate_new_key():
    key = APIKey()
    print key.str
    return key


def show_keys():
    for key in APIKey.query.all():
        print key.str


if __name__ == '__main__':
    # generate_new_key().save_to_db()
    show_keys()
