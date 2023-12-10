from django.db import models

class Finch(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name