from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    class Meta:
        db_table = "test1"
class Value(models.Model):
    name =models.ForeignKey(Test, on_delete=models.CASCADE)
    value = models.CharField(max_length=120)
    class Meta:
        db_table = "test2"
