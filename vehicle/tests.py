from django.test import TestCase
from .models import VehicleModel
from django.urls import reverse


class VehicleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        VehicleModel.objects.create(
            vehicle_number='KL 10H 1234',
            vehicle_type='2',
            vehicle_model='Swift',
            vehicle_description='Good'
        )

    def test_vehicle_number_label(self):
        vehicle_details = VehicleModel.objects.get(id=1)
        field_label = vehicle_details._meta.get_field(
            'vehicle_number').verbose_name
        self.assertEqual(field_label, 'vehicle number')

    def test_vehicle_type_label(self):
        vehicle_details = VehicleModel.objects.get(id=1)
        field_label = vehicle_details._meta.get_field(
            'vehicle_type').verbose_name
        self.assertEqual(field_label, 'vehicle type')

    def test_vehicle_model_label(self):
        vehicle_details = VehicleModel.objects.get(id=1)
        field_label = vehicle_details._meta.get_field(
            'vehicle_model').verbose_name
        self.assertEqual(field_label, 'vehicle model')

    def test_vehicle_description_label(self):
        vehicle_details = VehicleModel.objects.get(id=1)
        field_label = vehicle_details._meta.get_field(
            'vehicle_description').verbose_name
        self.assertEqual(field_label, 'vehicle description')
