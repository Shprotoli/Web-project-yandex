import pytest
from unittest.mock import Mock

from backend.web.service.user_service import UserService, TypeUserError


@pytest.fixture
def user_repository():
    repo = Mock()
    repo.get_by_email.return_value = None
    repo.get_by_username.return_value = None
    return repo


@pytest.fixture
def user_service(user_repository):
    return UserService(user_repository)


def test_validate_registration_success(user_service, user_repository):
    data = {
        "password": "strongpass123",
        "confirm_password": "strongpass123",
        "email": "test@example.com",
        "username": "testuser",
    }

    result = user_service.validate_registration(data)

    assert result.is_valid() is True
    assert result.get_errors() == []
    user_repository.get_by_email.assert_called_once_with("test@example.com")
    user_repository.get_by_username.assert_called_once_with("testuser")


def test_validate_registration_password_required(user_service, user_repository):
    data = {
        "password": "",
        "confirm_password": "",
        "email": "test@example.com",
        "username": "testuser",
    }

    result = user_service.validate_registration(data)
    errors = result.get_errors()

    assert result.is_valid() is False
    assert len(errors) == 1
    assert errors[0] == {
        "type": TypeUserError.PASSWORD.value,
        "message": "Пароль обязателен",
    }


def test_validate_registration_password_too_short(user_service):
    data = {
        "password": "1234567",
        "confirm_password": "1234567",
        "email": "test@example.com",
        "username": "testuser",
    }

    result = user_service.validate_registration(data)
    errors = result.get_errors()

    assert result.is_valid() is False
    assert len(errors) == 1
    assert errors[0] == {
        "type": TypeUserError.PASSWORD.value,
        "message": "Пароль должен быть не менее 8 символов",
    }


def test_validate_registration_passwords_do_not_match(user_service):
    data = {
        "password": "strongpass123",
        "confirm_password": "wrongpass123",
        "email": "test@example.com",
        "username": "testuser",
    }

    result = user_service.validate_registration(data)
    errors = result.get_errors()

    assert result.is_valid() is False
    assert len(errors) == 1
    assert errors[0] == {
        "type": TypeUserError.PASSWORD.value,
        "message": "Пароли не совпадают",
    }


def test_validate_registration_email_already_exists(user_service, user_repository):
    user_repository.get_by_email.return_value = {"id": 1, "email": "test@example.com"}

    data = {
        "password": "strongpass123",
        "confirm_password": "strongpass123",
        "email": "test@example.com",
        "username": "testuser",
    }

    result = user_service.validate_registration(data)
    errors = result.get_errors()

    assert result.is_valid() is False
    assert len(errors) == 1
    assert errors[0] == {
        "type": TypeUserError.EMAIL.value,
        "message": "Email уже используется",
    }


def test_validate_registration_username_already_exists(user_service, user_repository):
    user_repository.get_by_username.return_value = {"id": 1, "username": "testuser"}

    data = {
        "password": "strongpass123",
        "confirm_password": "strongpass123",
        "email": "test@example.com",
        "username": "testuser",
    }

    result = user_service.validate_registration(data)
    errors = result.get_errors()

    assert result.is_valid() is False
    assert len(errors) == 1
    assert errors[0] == {
        "type": TypeUserError.USERNAME.value,
        "message": "Username уже занят",
    }


def test_validate_registration_multiple_errors(user_service, user_repository):
    user_repository.get_by_email.return_value = {"id": 1, "email": "test@example.com"}
    user_repository.get_by_username.return_value = {"id": 1, "username": "testuser"}

    data = {
        "password": "123",
        "confirm_password": "456",
        "email": "test@example.com",
        "username": "testuser",
    }

    result = user_service.validate_registration(data)
    errors = result.get_errors()

    assert result.is_valid() is False
    assert len(errors) == 4

    assert {
               "type": TypeUserError.PASSWORD.value,
               "message": "Пароль должен быть не менее 8 символов",
           } in errors

    assert {
               "type": TypeUserError.PASSWORD.value,
               "message": "Пароли не совпадают",
           } in errors

    assert {
               "type": TypeUserError.EMAIL.value,
               "message": "Email уже используется",
           } in errors

    assert {
               "type": TypeUserError.USERNAME.value,
               "message": "Username уже занят",
           } in errors
