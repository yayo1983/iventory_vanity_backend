from rest_framework import serializers
from django.contrib.auth.models import User
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
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )
    department = serializers.SlugRelatedField(
        slug_field="name", queryset=Department.objects.all()
    )

    class Meta:
        model = Equipment
        fields = "__all__"


class EquipmentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentLog
        fields = "__all__"


class ReassignEquipmentSerializer(serializers.Serializer):
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), required=False
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
