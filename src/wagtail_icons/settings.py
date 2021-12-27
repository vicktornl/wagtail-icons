from django.conf import settings


def get_setting(name: str, default=None):
    return getattr(settings, "WAGTAIL_ICONS_%s" % name, default)


BASE_PATH = get_setting("BASE_PATH", default="wagtail_icons")
SETS = get_setting("SETS", default=[])
