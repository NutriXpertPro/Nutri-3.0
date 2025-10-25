import pytest
from django.template.loader import get_template


@pytest.mark.django_db
def test_tailwind_base_html():
    template = get_template("base.html")
    html = template.render({})
    assert 'class="bg-gray-50 bg-pattern min-h-screen"' in html


@pytest.mark.django_db
def test_base_html_structure():
    template = get_template("base.html")
    html = template.render({})
    expected_header = (
        '<header class="text-white bg-gradient-to-b from-blue-500 to-blue-900 '
        'shadow-lg shadow-blue-500/20 fixed w-full top-0 z-50">'
    )
    assert expected_header in html
    assert '<aside id="sidebar"' in html
    assert '<main class="flex-1 md:ml-0 p-4 md:p-6 lg:p-8">' in html
