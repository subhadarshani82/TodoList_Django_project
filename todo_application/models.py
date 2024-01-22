from django.db import models


# Create your models here.
class TodoList(models.Model):
    task = models.CharField(max_length=200)
    status = models.CharField(max_length=30, default='New', null=True)

    def __str__(self):
        return self.task
