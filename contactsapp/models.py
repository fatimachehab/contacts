from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    profession = models.CharField(max_length=100)
    telnumber = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20, default="none")
    date_joined = models.DateTimeField(null=True, blank=True)  # Allow it to be nullable
    date_expired = models.DateTimeField(null=True, blank=True)  # Allow it to be nullable

    def __str__(self):
        return self.name

