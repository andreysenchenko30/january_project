from django.db import models


class Congratulation(models.Model):
    congratulation = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.congratulation}'
# Create your models here.
