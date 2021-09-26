import pytest
import sys
import mock

sys.path.append("./register_user/")

valid_input_event = {}

valid_expected_response = {'statusCode': 400, 'body': 'invalid parameters'}

testdata = [
    (valid_input_event, valid_expected_response)

]

create_input_event = {'queryStringParameters':{'email':"sarthak@gmail.com"}}
success_response = {'statusCode': 200, 'body': "New User Registered"}
exit_user_success_response = {'statusCode': 200, 'body': "User already exists"}
error_response = {'statusCode': 500, 'body': "internal_server_error"}


@pytest.mark.parametrize("input_event,expected_response", [(valid_input_event, valid_expected_response)])
def test_register_user_invalid_param(monkeypatch, input_event, expected_response):
    # import register_user.app
    from app import lambda_handler
    return_value = lambda_handler(input_event, None)
    assert return_value == expected_response


@mock.patch("app.dynamodb_handler", mock.MagicMock(return_value="New User Registered"))
@pytest.mark.parametrize("input_event,expected_response", [(create_input_event, success_response)])
def test_register_new_user(monkeypatch, input_event, expected_response):
    sys.path.append("../../src/register_user")
    from app import lambda_handler
    return_value = lambda_handler(input_event, None)
    assert return_value == expected_response


@mock.patch("app.dynamodb_handler", mock.MagicMock(return_value="User already exists"))
@pytest.mark.parametrize("input_event,expected_response", [(create_input_event, exit_user_success_response)])
def test_register_user_exists(monkeypatch, input_event, expected_response):
    sys.path.append("../../src/register_user")
    from app import lambda_handler
    return_value = lambda_handler(input_event, None)
    assert return_value == expected_response


@pytest.mark.parametrize("input_event,expected_response", [(create_input_event, error_response)])
def test_register_user_error_handling(monkeypatch, input_event, expected_response):
    print(sys.path.append("../../src/register_user"))
    from app import lambda_handler
    return_value = lambda_handler(input_event, None)
    assert return_value == expected_response

# if __name__ == '__main__':
#     pytest.main()

# coverage report --omit=*/venv/* -m
# coverage run --omit=*/venv/* -m pytest test_app.py
