from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .presentation.views import (
    DepartmentViewSet,
    EquipmentViewSet,
    EquipmentLogViewSet,
    InventoryViewSet,
)

router = DefaultRouter()
router.register(r"departments", DepartmentViewSet)
router.register(r"equipments", EquipmentViewSet)
router.register(r"equipment-logs", EquipmentLogViewSet)
router.register(r"inventories", InventoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
