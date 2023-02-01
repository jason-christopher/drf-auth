from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Home


class HomeTests(APITestCase):
    # In Python, the @classmethod decorator is used to declare a method in the class as a class method that can be called using ClassName.MethodName()
    # click the blue circle, this overrides a particular method
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_home = Home.objects.create(
            street_address="1234 Fake St.",
            owner=testuser1,
            city="Orlando",
            state="FL",
            description="Orlando house.",
        )
        test_home.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_homes_model(self):
        home = Home.objects.get(id=1)
        actual_owner = str(home.owner)
        actual_street_address = str(home.street_address)
        actual_description = str(home.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_street_address, "1234 Fake St.")
        self.assertEqual(
            actual_description, "Orlando house."
        )

    def test_get_home_list(self):
        url = reverse("home_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        homes = response.data
        self.assertEqual(len(homes), 1)
        self.assertEqual(homes[0]["street_address"], "1234 Fake St.")

    def test_get_home_by_id(self):
        url = reverse("home_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        home = response.data
        self.assertEqual(home["street_address"], "1234 Fake St.")

    def test_create_home(self):
        url = reverse("home_list")
        data = {
            "owner": 1,
            "street_address": "2345 Test Ave.",
            "city": "Seattle",
            "state": "WA",
            "description": "Seattle house."
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        homes = Home.objects.all()
        self.assertEqual(len(homes), 2)
        self.assertEqual(Home.objects.get(id=2).street_address, "2345 Test Ave.")

    def test_update_home(self):
        url = reverse("home_detail", args=(1,))
        data = {
            "owner": 1,
            "street_address": "3456 Update Ave.",
            "city": "Austin",
            "state": "TX",
            "description": "Austin house."
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        home = Home.objects.get(id=1)
        self.assertEqual(home.street_address, data["street_address"])
        self.assertEqual(home.owner.id, data["owner"])
        self.assertEqual(home.description, data["description"])

    def test_delete_home(self):
        url = reverse("home_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        homes = Home.objects.all()
        self.assertEqual(len(homes), 0)

    # New
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("home_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
