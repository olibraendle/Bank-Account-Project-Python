from app import app
from database import db_init

if __name__ == "__main__":

    db_init()
    app()
