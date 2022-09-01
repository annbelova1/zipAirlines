from django.conf import settings
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from airplane.models import Airplane


class AirplaneAPITestCase(APITestCase):

    def setUp(self):
        self.list_request_data = [
            {
                "airplane_id": 1,
                "passengers_count": 100
            },
            {
                "airplane_id": 2,
                "passengers_count": 200
            },
            {
                "airplane_id": 3,
                "passengers_count": 300
            },
        ]

        self.single_model_request_data = {
                "airplane_id": 1,
                "passengers_count": 100
            }

        self.over_limit_request_data = list(
            {'airplane_id': id, 'passengers_count': 100} for id in range(1, 122)
        )

    def _subject(self, data={}):
        modified_url = reverse('airplanes-list')
        return self.client.post(modified_url, data, format='json')

    def test_create_multiple_airplanes_success(self):
        response = self._subject(data=self.list_request_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), len(self.list_request_data))

    def test_create_single_airplane_success(self):
        response = self._subject(data=self.single_model_request_data)
        single_airplane = Airplane.objects.first()
        expected_data = {
            **self.single_model_request_data,
            "user_id": None,
            "fuel_consumption_per_minute": single_airplane.fuel_consumption_per_minute,
            "flight_limit_minutes": single_airplane.flight_limit_minutes,
        }

        self.assertEqual(Airplane.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), expected_data)

    def test_create_airplane_more_than_allowed(self):
        """
        Try to create more planes for user than AIRPLANES_LIMIT
        raise ValueError
        """
        response = self._subject(data=self.over_limit_request_data)
        expected_error = {
            'error': f'ValueError: You can create only {settings.AIRPLANES_LIMIT} planes'
        }

        self.assertEqual(Airplane.objects.count(), 0)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.data, expected_error)
