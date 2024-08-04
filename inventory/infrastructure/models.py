from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    purchase_date = models.DateField()
    supplier = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.CharField(max_length=255, blank=True, null=True)
    processor = models.CharField(max_length=255, blank=True, null=True)
    hard_drive_size = models.CharField(max_length=255, blank=True, null=True)
    installed_software = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

class EquipmentLog(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.equipment} - {self.action}"
    

class Inventory(models.Model):
    """
    Model representing an inventory record.
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipment} - {self.department} ({self.quantity})"
