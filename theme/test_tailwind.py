import pytest
from django.template.loader import get_template


@pytest.mark.django_db
def test_tailwind_base_html():
    template = get_template("base.html")
    html = template.render({})
    assert 'class="bg-white text-gray-800 min-h-screen"' in html


@pytest.mark.django_db
def test_base_html_structure():
    template = get_template("base.html")
    html = template.render({})
    assert (
        "<aside class=\"fixed top-0 left-0 h-screen w-20 sidebar-pattern "
        "flex flex-col items-center py-4\">"
        in html
    )
    assert '<main class="ml-20 flex-1">' in html
