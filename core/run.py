from core.main import app
from core.db import db

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

