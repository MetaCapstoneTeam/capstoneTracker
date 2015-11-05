from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .views import index


class FrontendUrlsTests(TestCase):

    """Test the frontend urls."""

    def test_index_pattern_resolves_index_view(self):
        """Test index pattern resolves the correct view."""
        match = resolve('/')
        self.assertEqual(match.func, index)


class FrontendViewsTests(TestCase):

    """Test the frontend views."""

    def test_index_view_returns_correct_html(self):
        """Test that the index view returns correct html."""
        request = HttpRequest()
        response = index(request)
        expected_content = render_to_string('index.html')
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )
