from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=128, null=False)
    passwd = models.CharField(max_length=128, null=False)
    addr = models.CharField(max_length=128, null=True)
    filename = models.CharField(max_length=256, null=True)

    class Meta:
        db_table="user"