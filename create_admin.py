from app import app, db, User
from werkzeug.security import generate_password_hash

# Ensure you've properly created your Flask app instance in the 'app' module

# Create the database tables
with app.app_context():
    db.create_all()

    # Create an admin user
    admin1 = User(
        username="admin",
        password=generate_password_hash("admin"),
        email="admin@scc.net")

    # Add the admin user to the session and commit to the database
    db.session.add(admin1)
    db.session.commit()