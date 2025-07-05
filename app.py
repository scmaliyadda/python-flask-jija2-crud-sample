from flask import Flask
from config import Config
from db import get_db_connection
from auth import auth_bp
from tasks import tasks_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)

# 404 error
@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page not found", 404

if __name__ == '__main__':
    app.run(debug=True)