import jwt
SECRET_KEY = "$2y$10$fKFQh1xQRVfdjXt0aZOk3.heVLZoyLDuxprz2Z2KERV3mSzSXpxD."


def get_auth_token(username):
    return jwt.encode({"username": username, }, SECRET_KEY, algorithm='HS256')