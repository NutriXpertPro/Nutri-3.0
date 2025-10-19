import pytest
from django.template.loader import get_template


@pytest.mark.django_db
def test_tailwind_base_html():
    template = get_template("base.html")
    html = template.render({})
    assert 'class="bg-gray-100"' in html


@pytest.mark.django_db
def test_base_html_layout_option_4():
    template = get_template("base.html")
    html = template.render({})
    assert (
        '<div id="layout-option-4" class="grid grid-cols-12 grid-rows-6 min-h-screen">'
        in html
    )
    assert (
        '<header class="col-span-12 row-span-1 bg-gray-800 text-white shadow p-4 '
        'flex justify-between items-center">' in html
    )
    assert '<aside class="col-span-2 row-span-5 bg-gray-700 text-white p-4">' in html
    assert '<main class="col-span-10 row-span-5 p-6">' in html
