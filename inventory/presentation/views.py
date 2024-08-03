from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from ..infrastructure.models import Department, Equipment, EquipmentLog, Inventory
from .serializers import (
    DepartmentSerializer,
    EquipmentSerializer,
    EquipmentLogSerializer,
    InventorySerializer,
)


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Department instances.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request, *args, **kwargs):
        """
        List all departments with caching.
        """
        cache_key = "department_list"
        departments = cache.get(cache_key)

        if not departments:
            queryset = self.queryset
            serializer = self.get_serializer(queryset, many=True)
            departments = serializer.data
            cache.set(
                cache_key, departments, timeout=60 * 15
            )  # Cache timeout 15 minutes

        return Response(departments)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a department by its ID with caching.
        """
        department_id = kwargs.get("pk")
        cache_key = f"department_{department_id}"
        department = cache.get(cache_key)

        if not department:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            department = serializer.data
            cache.set(
                cache_key, department, timeout=60 * 15
            )  # Cache timeout 15 minutes

        return Response(department)

    def update(self, request, *args, **kwargs):
        """
        Update a department instance.
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Invalidate cache for updated department
        cache_key = f"department_{instance.pk}"
        cache.delete(cache_key)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a department instance.
        """
        instance = self.get_object()
        self.perform_destroy(instance)

        # Invalidate cache for department list and specific department
        cache.delete("department_list")
        cache_key = f"department_{instance.pk}"
        cache.delete(cache_key)

        return Response(status=status.HTTP_204_NO_CONTENT)


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Equipment instances.
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def list(self, request, *args, **kwargs):
        """
        List all equipment with caching.
        """
        cache_key = "equipment_list"
        equipment = cache.get(cache_key)

        if not equipment:
            queryset = self.queryset
            serializer = self.get_serializer(queryset, many=True)
            equipment = serializer.data
            cache.set(cache_key, equipment, timeout=60 * 15)  # Cache timeout 15 minutes

        return Response(equipment)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve equipment by its ID with caching.
        """
        equipment_id = kwargs.get("pk")
        cache_key = f"equipment_{equipment_id}"
        equipment = cache.get(cache_key)

        if not equipment:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            equipment = serializer.data
            cache.set(cache_key, equipment, timeout=60 * 15)  # Cache timeout 15 minutes

        return Response(equipment)

    def update(self, request, *args, **kwargs):
        """
        Update an equipment instance.
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Invalidate cache for updated equipment
        cache_key = f"equipment_{instance.pk}"
        cache.delete(cache_key)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an equipment instance.
        """
        instance = self.get_object()
        self.perform_destroy(instance)

        # Invalidate cache for equipment list and specific equipment
        cache.delete("equipment_list")
        cache_key = f"equipment_{instance.pk}"
        cache.delete(cache_key)

        return Response(status=status.HTTP_204_NO_CONTENT)


class EquipmentLogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing EquipmentLog instances.
    """

    queryset = EquipmentLog.objects.all()
    serializer_class = EquipmentLogSerializer

    def list(self, request, *args, **kwargs):
        """
        List all equipment logs with caching.
        """
        cache_key = "equipment_log_list"
        equipment_logs = cache.get(cache_key)

        if not equipment_logs:
            queryset = self.queryset
            serializer = self.get_serializer(queryset, many=True)
            equipment_logs = serializer.data
            cache.set(
                cache_key, equipment_logs, timeout=60 * 15
            )  # Cache timeout 15 minutes

        return Response(equipment_logs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve an equipment log by its ID with caching.
        """
        equipment_log_id = kwargs.get("pk")
        cache_key = f"equipment_log_{equipment_log_id}"
        equipment_log = cache.get(cache_key)

        if not equipment_log:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            equipment_log = serializer.data
            cache.set(
                cache_key, equipment_log, timeout=60 * 15
            )  # Cache timeout 15 minutes

        return Response(equipment_log)

    def update(self, request, *args, **kwargs):
        """
        Update an equipment log instance.
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Invalidate cache for updated equipment log
        cache_key = f"equipment_log_{instance.pk}"
        cache.delete(cache_key)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an equipment log instance.
        """
        instance = self.get_object()
        self.perform_destroy(instance)

        # Invalidate cache for equipment log list and specific equipment log
        cache.delete("equipment_log_list")
        cache_key = f"equipment_log_{instance.pk}"
        cache.delete(cache_key)

        return Response(status=status.HTTP_204_NO_CONTENT)


class InventoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Inventory instances.
    """

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def list(self, request, *args, **kwargs):
        """
        List all inventory records with caching.
        """
        cache_key = "inventory_list"
        inventory = cache.get(cache_key)

        if not inventory:
            queryset = self.queryset
            serializer = self.get_serializer(queryset, many=True)
            inventory = serializer.data
            cache.set(cache_key, inventory, timeout=60 * 15)  # Cache timeout 15 minutes

        return Response(inventory)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve an inventory record by its ID with caching.
        """
        inventory_id = kwargs.get("pk")
        cache_key = f"inventory_{inventory_id}"
        inventory = cache.get(cache_key)

        if not inventory:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            inventory = serializer.data
            cache.set(cache_key, inventory, timeout=60 * 15)  # Cache timeout 15 minutes

        return Response(inventory)

    def update(self, request, *args, **kwargs):
        """
        Update an inventory record.
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Invalidate cache for updated inventory record
        cache_key = f"inventory_{instance.pk}"
        cache.delete(cache_key)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an inventory record.
        """
        instance = self.get_object()
        self.perform_destroy(instance)

        # Invalidate cache for inventory list and specific inventory record
        cache.delete("inventory_list")
        cache_key = f"inventory_{instance.pk}"
        cache.delete(cache_key)

        return Response(status=status.HTTP_204_NO_CONTENT)