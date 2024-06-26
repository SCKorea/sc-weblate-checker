from django.utils.translation import gettext_lazy
from weblate.addons.scripts import BaseScriptAddon


class CheckerAddon(BaseScriptAddon):
    """Pre commit script example addon."""
    name = gettext_lazy("StarCitizen Format check addon")
    description = gettext_lazy("If you see this, you can use the Custom quality check for Star Citizen.")