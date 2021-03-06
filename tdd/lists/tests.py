from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
from .views import home_page
from .models import Item


class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': '신규 작업 아이템'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': '신규 작업 아이템'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_home_page_display_all_list_items(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "첫 번째 아이템"
        first_item.save()

        second_item = Item()
        second_item.text = "두 번째 아이템"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_saved_item.text, '두 번째 아이템')


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # csrf_token 다름
    # def test_home_page_return_correct_html(self):
    # 브라우저에게 보낼 요청 객체를 생성한다.
    # request = HttpRequest()
    # home_page 뷰에 전달하여 응답을 취득한다.
    # response = home_page(request)
    # expected_html = render_to_string('lists/home.html')
    # self.assertEqual(response.content.decode(), expected_html)
