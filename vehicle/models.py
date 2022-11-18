from django.db import models


VEHICLE_TYPES = [
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
]

class VehicleModel(models.Model):
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(
        max_length = 20, 
        choices=VEHICLE_TYPES, 
        default='2'
        )
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()
