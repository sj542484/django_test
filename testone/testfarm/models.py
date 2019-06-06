from django.db import models

# Create your models here.
class EquipmentList(models.Model):
    equipment_name = models.CharField(max_length=50)
    equipment_model = models.CharField(max_length=50)
    equipment_uuid = models.CharField(max_length=50,unique=True)
    platform_verion = models.CharField(max_length=50)
    start_but_statue = models.IntegerField(default=0)
    statue_statue = models.IntegerField(default=0)
    gid = models.IntegerField(null=True)

    def __str__(self):
        return self.equipment_name