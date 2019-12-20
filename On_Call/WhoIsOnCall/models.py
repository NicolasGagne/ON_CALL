from django.db import models

# Create your models here.


class Organisation(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    private = models.BooleanField(default=False)

    def _str_(self):
        return self.name