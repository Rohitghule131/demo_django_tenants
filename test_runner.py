from django.test.runner import DiscoverRunner
from utilities.tests import print_test


class CustomTestRunner(DiscoverRunner):
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        result = super().run_tests(test_labels, extra_tests=extra_tests, **kwargs)

        print_test.create_test_case_csv()
        return result
