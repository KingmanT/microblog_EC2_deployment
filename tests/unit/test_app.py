import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    # Create an instance of the app with the 'testing' configuration
    app = create_app('testing')
    
    with app.app_context():
        # Create the database
        db.create_all()
        yield app
        # Drop the database
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    # Send a GET request to the home page
    response = client.get('/')
    assert response.status_code == 200
    assert b'Microblog' in response.data

def test_login_page(client):
    # Send a GET request to the login page
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Sign In' in response.data
