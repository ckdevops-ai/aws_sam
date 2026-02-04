from src.app import lambda_handler

def test_hello_world():
    event = {"httpMethod": "GET", "path": "/hello"}
    result = lambda_handler(event, {})
    assert result["statusCode"] == 200
    assert "hello world" in result["body"]
