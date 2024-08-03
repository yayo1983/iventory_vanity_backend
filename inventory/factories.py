from .infrastructure.models import Equipment

class EquipmentFactory:
    @staticmethod
    def create_equipment(data):
        return Equipment.objects.create(**data)
