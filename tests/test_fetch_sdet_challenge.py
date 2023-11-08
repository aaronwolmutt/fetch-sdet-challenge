import os

def test_sanity():
    assert True == True


def test_env_is_set_correctly():
    url = os.getenv("POETRY_CHALLENGE_URL")
    assert url is not None