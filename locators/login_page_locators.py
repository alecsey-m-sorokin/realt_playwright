from enum import Enum


class LoginPageLocators(Enum):
    """Локаторы для страницы логина на realt.by"""
    
    EMAIL_INPUT = "input[name='login']"
    PASSWORD_INPUT = "input[name='password']"
    SUBMIT_BUTTON = "button[type='button']"
