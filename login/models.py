from django.db import models

class StudentCreds(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
