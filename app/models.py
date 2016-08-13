from django.db import models

class Menu_Item(models.Model):
    item_name = models.CharField(max_length=15)

    def publish(self):
        self.save()
    def __str__(self):
        return self.item_name

# Create your models here.
