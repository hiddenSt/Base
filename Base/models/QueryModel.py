from django.db import models


class QueryModel(models.Model):
    user_id = models.IntegerField()
    params = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    created = models.TimeField()