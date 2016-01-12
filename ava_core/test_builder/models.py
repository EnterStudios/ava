from django.db import models


class TestDataFieldReference(models.Model):
    field_type = models.CharField(max_length=100, unique=True)
    standard_value = models.CharField(max_length=1000, null=True)
    modified_value = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.field_type
