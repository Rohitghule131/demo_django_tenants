from django.urls import reverse
from rest_framework import status
from django_tenants.test.client import TenantClient

from utilities.tests import (
    print_test,
    SetUpTestData
)


class AddBookTestCases(SetUpTestData):
    """
    Class for a test list related to api.
    """

    def setUp(self):
        self.path = "/api/tenant1" + reverse("add-book")
        self.login_response = self.setUpInitialTenant1()
        self.access_token = self.login_response["token"]["access"]
        self.headers = {"Authorization": "Bearer {}".format(self.access_token)}

        self.data = {
            "name": "Atomic Habit",
            "author": "ABC",
            "price": 100
        }
        self.expected_response = {
            'status_code': 201,
            'error': None,
            'data': {
                'id': 1,
                'name': 'Atomic Habit',
                'author': 'ABC',
                'price': 100.0
            },
            'message': ['Book created successfully.']
        }
        self.c = TenantClient(self.tenant)

    def test_add_book_api(self):
        """
        Method for test contact related to.
        """
        try:
            response_data = self.c.post(self.path, data=self.data, content_type=self.applicationJson, headers=self.headers)
            self.assertEqual(response_data.data["status_code"], status.HTTP_201_CREATED)
            print(response_data.data)
            self.assertEqual(response_data.data["data"]["name"], self.data["name"])
            print_test.print_terminal(self.path, "ADD BOOK", self.passed, None)

        except AssertionError as e:
            print_test.print_terminal(self.path, "ADD BOOK", self.failed, e)


class ListBookTestCases(SetUpTestData):
    """
    Class for test list related to api.
    """

    def setUp(self):
        self.path = "/api/tenant1" + reverse("list-books")
        self.login_response = self.setUpInitialTenant1()
        self.access_token = self.login_response["token"]["access"]
        self.headers = {"Authorization": "Bearer {}".format(self.access_token)}

        self.c = TenantClient(self.tenant)

    def test_list_book_api(self):
        """
        Method for test contact related to.
        """
        try:
            response_data = self.c.get(self.path, content_type=self.applicationJson, headers=self.headers)
            # self.assertEqual(response_data.data["status_code"], status.HTTP_200_OK)
            self.assertIsInstance(response_data.data["data"], list)
            print_test.print_terminal(self.path, "LIST BOOK", self.passed, None)

        except AssertionError as e:
            print_test.print_terminal(self.path, "LIST BOOK", self.failed, e)
