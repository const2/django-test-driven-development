from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        # 브라우저에게 보낼 요청 객체를 생성한다.
        request = HttpRequest()
        # home_page 뷰에 전달하여 응답을 취득한다.
        response = home_page(request)

        # html로 시작하는지 확인
        self.assertTrue(response.content.startswith(b'<html>'))
        # 제목 일치하는지 확인
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        # html로 끝나는지 확인
        self.assertTrue(response.content.endswith(b'</html>'))
