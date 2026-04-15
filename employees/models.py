from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=30)
    salary = models.IntegerField()

    def __str__(self):
        return self.name
