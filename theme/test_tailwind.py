import pytest
from django.template.loader import get_template


@pytest.mark.django_db
def test_tailwind_base_html():
    template = get_template("base.html")
    html = template.render({})
    assert 'class="bg-gray-100"' in html
