from app import app, db

with app.app_context():
    try:
        db.engine.connect()
        print("Connection successful!")
    except Exception as e:
        print(f"Connection failed: {e}")
