from django.core.exceptions import ValidationError
from django.db import models

class Item(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    def clean(self):
        # Check if any of the fields are empty
        if not self.name or not self.description or not self.price:
            raise ValidationError('All fields must be filled.')

    def save(self, *args, **kwargs):
        # Call clean method to validate fields
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
