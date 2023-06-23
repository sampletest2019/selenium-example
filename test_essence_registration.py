import pytest


@pytest.mark.smoketest
def test_essence_registration(browser):
    browser.get("https://theessence.app")