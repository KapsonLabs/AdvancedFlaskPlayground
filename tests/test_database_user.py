from flask import jsonify, json
import pytest
from ..models import User
from datetime import datetime as dt

try:
    from flask import _app_ctx_stack as ctx_stack
except ImportError:
    from flask import _request_ctx_stack as ctx_stack

class TestUserViews:

    # def __init__(self):
    #     self.data = {
    #         "email":"ga@gmail.com",
    #         "user":"Allan2"
    #     }

    def test_users_get(self, client, session):
        new_user1 = User(username="Name1",
                        email="Name1@gmail.com",
                        created=dt.now(),
                        bio="Am in love with the testing",
                        admin=False)  
        new_user2 = User(username="Name2",
                        email="Name2@gmail.com",
                        created=dt.now(),
                        bio="Am in love with the testing 2",
                        admin=False)

        session.add(new_user1)
        session.add(new_user2)
        session.commit()

        response = client.get('/', content_type="application/json")
        assert response.status_code == 200
        returned_data = json.loads(response.data.decode('utf-8'))
        assert returned_data["status"] == 200
        assert len(returned_data["data"]) == 2


    def test_database_user(self, client, session):
        """
        GIVEN a Flask application
        WHEN the '/' page is requested (GET)
        THEN check the response is valid
        """
        data = {
            "email":"ga@gmail.com",
            "user":"Allan2"
        }
        
        response = client.post('/', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 200
        #convert data to json
        returned_data = json.loads(response.data.decode('utf-8'))


    def test_bad_input(self, client, session):
        """
        GIVEN a Flask application
        WHEN the '/' page is requested (GET)
        THEN check the response is valid
        """

        data = {
            "email":"ga@gmail.com",
            "user":2
        }
        
        response = client.post('/', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 400
        assert b'Username should be a string' in response.data