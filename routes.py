from flask import jsonify, request, Response, json
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User
from .serializers import UserSchema


@app.route('/', methods=['POST'])
def create_user():
    """Create a user."""
    username = request.json['user']
    email = request.json['email']
    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing_user:
            return jsonify({"error": 'user already created!'})
        new_user = User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                        admin=False)  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        schema = UserSchema()
    return jsonify({"status":201, "data":schema.dump(new_user)})

@app.route('/', methods=['GET'])
def retieve_users():
    schema = UserSchema(many=True)
    user_query = User.query.all()
    return jsonify({"status":200, "data":schema.dump(user_query)})
