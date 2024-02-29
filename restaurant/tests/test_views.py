from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemView

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="Salad", price=5.99, inventory = 534)
        self.menu2 = Menu.objects.create(title="Steak",price= 15.99, inventory = 324)

    def test_url_location(self):
        url = self.client.get('/restaurant/menu/')
        self.assertEqual(url.status_code, 200)

    def test_getall(self):
        url = self.client.get('/restaurant/menu/')
        # url = self.client.get('menu/')
        
        # response = self.client.get(url)
        self.assertEqual(url.status_code, 200)

        serialized_data = MenuSerializer([self.menu1, self.menu2], many=True).data
        self.assertEqual(url.data, serialized_data)


# class MenuViewTest(TestCase):
#     def setUp(self):
#         self.menu_view_test_data = [
#             {"title": "Test Item","price": '9.99',"inventory": 453},
#             {"title": "Test Item Two","price": '10.99',"inventory": 400}
#         ]

#         self.menu_view_test_data = Menu.objects.create(**self.menu_view_test_data)
    
#     def test_getall(self):
#         all_items = Menu.objects.all()
#         serialized_items = MenuSerializer(all_items, many=True).data
        
#         self.assertEqual(all_items, serialized_items)

    # def setUp(self):
    #     # self.client = APIClient()
        
    #     self.menu_item_data = {
    #     "title" : "Test Item",
    #     "price" : '9.99',
    #     "inventory" : 453
    #     }
        
    #     Menu.objects.create(**self.menu_item_data)

    # def test_getall(self):
    #     url = reverse("menu-items-list")
    #     response = self.client.get(url)
        
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    #     menu_items = Menu.objects.all()
    #     serialized_data = MenuSerializer(menu_items, many=True).data


    #     self.assertEqual(response.data, serialized_data)


# http://127.0.0.1:8000/api/menu/
# http://127.0.0.1:8000/api/menu/1