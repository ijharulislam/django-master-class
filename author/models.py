from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300, default="")

    designation = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "My Author"

    def __str__(self):
        return f"{self.first_name}"

    # Model Method
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


