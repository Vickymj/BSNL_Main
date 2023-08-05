from django.db import models
from datetime import datetime,date
# Create your models here.
class Newbooking(models.Model):
	membername = models.CharField(max_length=120)
	fathername = models.CharField(max_length=120)
	dob = models.DateField()
	age = models.CharField(max_length=100)
	moblieno = models.CharField(max_length=100)
	alternateno = models.CharField(max_length=100)
	emailid = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	panno = models.CharField(max_length=100)
	aadhhaarno = models.CharField(max_length=100)
	nomieename = models.CharField(max_length=100)
	nomieeage = models.CharField(max_length=100)
	nomieerelationship = models.CharField(max_length=100)
	nomieeaddress = models.CharField(max_length=100)
	project = models.CharField(max_length=100)
	dimension = models.CharField(max_length=100)
	total= models.CharField(max_length=100)
	downpayment = models.CharField(max_length=100)
	siterefer = models.CharField(max_length=100)
	modeofpay = models.CharField(max_length=100)
	bank = models.CharField(max_length=100)
	branch = models.CharField(max_length=100)
	chequeno = models.CharField(max_length=100)
	paydate = models.DateField(max_length=100)
	amount = models.CharField(max_length=100)
	seniorityno = models.CharField(max_length=100)
	amno = models.CharField(max_length=100)
	receiptno = models.CharField(max_length=100)
	class Meta:
		db_table='newbook'