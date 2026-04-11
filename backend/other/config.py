from os import path, makedirs


def build_sqlite_uri() -> str:
    base_dir = path.abspath(path.dirname(__file__))
    db_dir = path.abspath(path.join(base_dir, "../db"))
    instance_dir = path.join(db_dir, "instance")

    makedirs(instance_dir, exist_ok=True)

    db_file = path.join(instance_dir, "app.db")
    return f"sqlite:///{db_file}"


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = build_sqlite_uri()


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
