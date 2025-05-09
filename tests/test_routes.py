import pytest
from app import app, db
from models import Country

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Select a Country" in response.data

def test_valid_country_page(client):
    """Test a valid country route returns 200."""
    # Assuming country with ID 1 exists
    response = client.get('/country/1')
    assert response.status_code in [200, 302]

def test_invalid_country_page(client):
    """Test an invalid country route returns 404."""
    response = client.get('/country/999999')  # unlikely to exist
    assert response.status_code == 404

def test_404_page(client):
    """Test non-existent route returns 404."""
    response = client.get('/nonexistentpage')
    assert response.status_code == 404
