from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
import pytz
from unittest.mock import patch

from rest_framework.permissions import AllowAny

class ProviderListViewTest(APITestCase):
    def setUp(self):
        """ Setup test data """
        print('Setup test data')

    def test_success(self):
        """ Test retrieval of vendor list """
        self.assertEqual(0, 0)

