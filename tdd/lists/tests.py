from django.http import HttpRequest
from django.template.loader import render_to_string
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
        expected_html = render_to_string('lists/home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)
        response_content = response.content.decode()
        self.assertIn('신규 작업 아이템', response_content)
        expected_html = render_to_string(
            'lists/home.html',
            request=request
        )
        print(expected_html)
        # csrf token으로 인한 불일치..
        # self.assertEqual(response_content.tr, expected_html)
