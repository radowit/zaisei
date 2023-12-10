import pytest

from tests.uebusaito.users.factories import UserFactory
from uebusaito.users.models import User


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:
    return UserFactory()
