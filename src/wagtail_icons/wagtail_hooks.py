import os

from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.module_loading import import_string
from wagtail.core import hooks

from wagtail_icons.settings import BASE_PATH, SETS


@hooks.register("insert_global_admin_css")
def global_admin_css():
    stylesheets = []
    for set in SETS:
        iconset_class = import_string(set)
        iconset_instance = iconset_class()
        stylesheets += iconset_instance.get_css_files()
    html = "".join(
        '<link rel="stylesheet" href="%s">'
        % static(os.path.join(BASE_PATH, stylesheet))
        for stylesheet in stylesheets
    )
    return format_html(html)
