from contextlib import suppress

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "uebusaito.users"
    verbose_name = _("Users")

    def ready(self) -> None:  # noqa: PLR6301
        with suppress(ImportError):
            import uebusaito.users.signals  # noqa: F401, PLC0415
