import csv
from django.urls import reverse
from django_tenants.test.client import TenantClient
from django_tenants.test.cases import SubfolderTenantTestCase, TestCase
from django.test import Client

from users.models import CustomUser


class PrintTestCases:
    def __init__(self):
        self.count = 0
        self.header = ["API", "TEST CASE", "STATUS", "MESSAGE"]
        self.data = list()

    def create_test_case_csv(self):
        open_file = open("testcases.csv", "w")
        writer = csv.writer(open_file)
        writer.writerow(self.header)
        writer.writerows(self.data)
        print("CSV FILE CREATED SUCCESSFULLY")
        return

    def print_terminal(self, api_name, test_case, test_status, msg):
        self.data.append([api_name, test_case, test_status, msg])
        self.count = self.count + 1
        print("-" * 100)
        print(f"{self.count} API : ", api_name, "|| TEST CASE : ", test_case, "|| STATUS :", test_status, "|| MESSAGE : ", msg)


print_test = PrintTestCases()


class SetUpTestData(SubfolderTenantTestCase):
    """
    Class to create dummy test data.
    """
    passed = "PASSED"
    failed = "FAILED"
    applicationJson = "application/json"

    @classmethod
    def get_test_tenant_domain(cls):
        return "tenant1"

    @classmethod
    def get_test_schema_name(cls):
        return "tenant1"

    def setUpInitialTenant1(self):
        """
        Initial set up method to create client_id, client_secret and superuser.
        """
        user = CustomUser.objects.create_user(
            email="rohit.ghule@yopmail.com",
            first_name="Rohit",
            last_name="Ghule",
            password="Qwerty@123"
        )
        user.save()
        payload = {
            "email": "rohit.ghule@yopmail.com",
            "password": "Qwerty@123"
        }
        path = "/api/tenant1" + reverse("login-user")
        c = TenantClient(self.tenant)
        response = c.post(path, data=payload, content_type="application/json")
        return response.data["data"]

