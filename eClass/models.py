from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.



class eClass(models.Model):
    name = models.CharField(max_length=50)
    monthlyFee = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    # teacher = models.ForeignKey()

    def __str__(self):
        return self.name