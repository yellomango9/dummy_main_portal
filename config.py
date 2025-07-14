import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", "mysql://test:Adrde07%40@localhost/dummy_main_portal_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
