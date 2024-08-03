from rest_framework import serializers
from ..infrastructure.models import Department, Equipment, EquipmentLog, Inventory


class InventorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Inventory model.
    """

    class Meta:
        model = Inventory
        fields = ["id", "department", "equipment", "quantity", "date_added"]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class EquipmentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentLog
        fields = "__all__"
