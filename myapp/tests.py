from django.urls import reverse
from rest_framework import status
from django_tenants.test.client import TenantClient
from django.test import TestCase, Client
from django_tenants.utils import schema_context

from .models import Book
from utilities.tests import (
    print_test,
    SetUpTestData
)
from customeuser.models import CustomUser
from tenant_model.models import ClientModel, DomainModel


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
            self.assertEqual("dkalsj", self.data["name"])
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
        book_obj = Book.objects.create(
            **{
            "name": "Atomic Habit",
            "author": "ABC",
            "price": 100
        }
        )
        book_obj.save()

        self.c = TenantClient(self.tenant)

    def test_list_book_api(self):
        """
        Method for test contact related to.
        """
        try:
            response_data = self.c.get(self.path, content_type=self.applicationJson, headers=self.headers)
            self.assertEqual(response_data.data["status_code"], status.HTTP_200_OK)
            self.assertEqual(1, len(response_data.data["data"]))
            self.assertIsInstance(response_data.data["data"], list)
            print_test.print_terminal(self.path, "LIST BOOK", self.passed, None)

        except AssertionError as e:
            print_test.print_terminal(self.path, "LIST BOOK", self.failed, e)


class UpdateBookTestCases(SetUpTestData):
    """
    Class for a test list related to api.
    """

    def setUp(self):
        self.login_response = self.setUpInitialTenant1()
        self.access_token = self.login_response["token"]["access"]
        self.headers = {"Authorization": "Bearer {}".format(self.access_token)}
        book_obj = Book.objects.create(
            name="Do Epic",
            author="jay",
            price=200
        )
        book_obj.save()
        self.path = "/api/tenant1" + reverse("update-book", kwargs={"pk": book_obj.id})

        self.data = {
            "name": "Do Epic Shit",
            "author": "Jayesh",
            "price": 250
        }

        self.c = TenantClient(self.tenant)

    def test_update_book_api(self):
        """
        Method for test contact related to.
        """
        try:
            response_data = self.c.patch(self.path, data=self.data, content_type=self.applicationJson, headers=self.headers)
            self.assertEqual(response_data.data["status_code"], status.HTTP_200_OK)
            # self.assertIsInstance(response_data.data["data"], list)
            print_test.print_terminal(self.path, "UPDATE BOOK", self.passed, None)

        except AssertionError as e:
            print_test.print_terminal(self.path, "UPDATE BOOK", self.failed, e)


class TestDemoTestCase(SetUpTestData):

    def setUp(self):
        with schema_context("public"):
            self.tenant2 = ClientModel(
                schema_name='tenant2',
                name='Tenant 2',
                paid_until='2014-12-05',
                on_trial=True
            )
            self.tenant2.save()

            # Add one or more domains for the tenant
            domain = DomainModel()
            domain.domain = 'tenant2'  # don't add your port or www here!
            domain.tenant = self.tenant2
            domain.is_primary = True
            domain.save()

            self.payload = {
                "email": "tenant2.user@yopmail.com",
                "password": "Qwerty@123"
            }

    def test_demo(self):
        path = "/api/tenant2" + reverse("login-user")
        c = TenantClient(self.tenant)

        with schema_context("tenant2"):
            self.user = CustomUser.objects.create_user(
                email="tenant2.user@yopmail.com",
                first_name="Tenant2",
                last_name="2",
                password="Qwerty@123"
            )
            self.user.save()

        response = c.post(path, data=self.payload, content_type="application/json")
        print_test.print_terminal(path, "Login", self.failed, None)
