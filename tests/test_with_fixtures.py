"""
Разные фикстуры для каждого (десктопный и мобильный размер) теста, переданные в параметры:
- для десктопного экрана
- для мобильного экрана
"""

import pytest
from selene.support.shared import browser
from selene import have


@pytest.fixture(scope='function')
def desktop_fixture():
    browser.config.window_height = 1080
    browser.config.window_width = 1920


@pytest.fixture(scope='function')
def mobile_fixture():
    browser.config.window_height = 800
    browser.config.window_width = 500


def test_github_desktop(desktop_fixture):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(mobile_fixture):
    browser.open('https://github.com')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))