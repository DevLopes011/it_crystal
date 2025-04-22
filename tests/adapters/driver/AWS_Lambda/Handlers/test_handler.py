import pytest
from src.adapters.driver.AWS_Lambda.Handlers.get_asset_handler import get_asset_handler

@pytest.fixture
def mock_event():
    return {
        "resource": "/",
        "path": "/",
        "httpMethod": "GET",
        "pathParameters": {"id": "123"},  
        "body": None
    }

def test_register_asset_success(mock_event):
    response = get_asset_handler(mock_event, {})
    assert response["queryStringParameters"] is None
    assert response["pathParameters"] is None
    assert response["body"] is None

def test_register_asset_invalid_body():
    mock_event = {
        "queryStringParameters": {"key": "value"},
        "pathParameters": {"param": "123"},
        "body": "invalid body format"
    }

    response = get_asset_handler(mock_event)

    assert response["queryStringParameters"] == {"key": "value"}
    assert response["pathParameters"] == {"param": "123"}
    assert response["body"] == "invalid body format" 

def test_register_asset_missing_fields():
    mock_event = {
        "queryStringParameters": None,
        # "pathParameters"
        "body": None
    }

    response = get_asset_handler(mock_event)

    assert response["queryStringParameters"] is None
    assert response["pathParameters"] is None
    assert response["body"] is None

def test_register_asset_with_valid_fields():
    mock_event = {
        "queryStringParameters": {"key": "value"},
        "pathParameters": {"param": "123"},
        "body": {"data": "some data"},
    }

    response = get_asset_handler(mock_event)

def test_register_asset_missing_fields():
    mock_event = {
        "queryStringParameters": None,
        "pathParameters": None,  # Simula erro esperado
        "body": None
    }

    response = get_asset_handler(mock_event, {})  # Adicionado `{}`

    assert response["statusCode"] == 500  # Espera erro
    assert "Missing key" in response["body"] or "Argumento não encontrado" in response["body"]

    assert response["queryStringParameters"] == {"key": "value"}
    assert response["pathParameters"] == {"param": "123"}
    assert response["body"] == {"data": "some data"}