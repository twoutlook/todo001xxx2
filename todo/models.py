from django.db import models

class Todo(models.Model):
    seq = models.CharField(max_length=6)
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item