from django.db import models

class ManagedModule(models.Model):
    name = models.CharField(max_length=100, unique=True)
    label = models.CharField(max_length=200)
    installed = models.BooleanField(default=False)
    app_name = models.CharField(max_length=100)

    def __str__(self):
        return self.app_name