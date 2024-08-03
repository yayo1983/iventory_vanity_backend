from ..infrastructure.models import Equipment

class EquipmentService:
    def assign_to_user(self, equipment_id, user):
        equipment = Equipment.objects.get(id=equipment_id)
        equipment.user = user
        equipment.save()

    def assign_to_department(self, equipment_id, department):
        equipment = Equipment.objects.get(id=equipment_id)
        equipment.department = department
        equipment.save()
