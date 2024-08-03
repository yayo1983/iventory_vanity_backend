# inventory/tests.py
from django.test import TestCase
from .infrastructure.models import Department, Equipment, EquipmentLog
from django.contrib.auth.models import User

class EquipmentTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="IT")
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.equipment = Equipment.objects.create(
            brand="Dell",
            model="XPS 13",
            purchase_date="2022-01-01",
            supplier="Dell Supplier",
            cost=1000.00,
            ram="16GB",
            processor="Intel i7",
            hard_drive_size="512GB",
            installed_software="Windows 10",
            user=self.user,
            department=self.department
        )

    def test_equipment_creation(self):
        self.assertEqual(self.equipment.brand, "Dell")

    def test_assign_to_user(self):
        new_user = User.objects.create_user(username='newuser', password='12345')
        self.equipment.user = new_user
        self.equipment.save()
        self.assertEqual(self.equipment.user, new_user)
