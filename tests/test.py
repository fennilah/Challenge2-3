import pytest
import app

@pytest.fixture

def app():
    app = .create_app()
    app.debug = True
    return app.test_client()

def test_get_home_page(app):
    response = app.get('/')
    assert response.status_code == 200
    assert "Home page" in response.data

def test_gets_all_entries(app):
    response = app.get('api/v1/entries/') 
    assert response.status_code == 200
    assert len(response.data) > 0

def test_lists_of_entries(app):
    response = app.get('/api/v1/entries/list')  
    assert response.status_code == 200
    assert len(response.data) > 0

def test_edit_entries(app):
    response = app.put('/api/v1/entries/edit')
    assert response.status_code == 200
    assert "updated_entries" in response.data  
