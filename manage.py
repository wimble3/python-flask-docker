from flask_migrate import Migrate

from app import app, db

# Adding db migrate commands
migrate = Migrate(app, db, compare_type=True)

if __name__ == "__main__":
    app.cli()
