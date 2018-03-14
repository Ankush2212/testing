from django.db import models

# Create your models here.
#class Greeting(models.Model):
    #when = models.DateTimeField('date created', auto_now_add=True)
	
	

class Contact(models.Model):
   
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField(blank=True)
	description = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now= True)

class adminsignup(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	email = models.EmailField(blank=True)
	
class adduser(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	username = models.CharField(max_length=250)
	dateofjoin = models.CharField(max_length=250)
	contactnumber = models.CharField(max_length=250)
	status = models.IntegerField()
	email = models.EmailField(blank=True)

class pricingplan(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	email = models.EmailField(blank=True)
	zipcode = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	amount = models.CharField(max_length=250)
	currenttime = models.CharField(max_length=250)
	mobilenumber = models.CharField(max_length=250)
	unit = models.CharField(max_length=250)
	datetimee = models.CharField(max_length=250)
	verify = models.IntegerField()

class hotelservice(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	email = models.EmailField(blank=True)
	zipcode = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	services = models.CharField(max_length=250)
	currentdate = models.CharField(max_length=250)
	mobilenumber = models.CharField(max_length=250)
	unit = models.CharField(max_length=250)
	datetimee = models.CharField(max_length=250)

class fulliteservice(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	email = models.EmailField(blank=True)
	zipcode = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	services = models.CharField(max_length=250)
	currentdate = models.CharField(max_length=250)
	mobilenumber = models.CharField(max_length=250)
	unit = models.CharField(max_length=250)
	datetimee = models.CharField(max_length=250)
	
	
	########
	
	
class employeedetail(models.Model):
	employeename = models.CharField(max_length=250)
	username = models.CharField(max_length=250)
	dateofjoin = models.CharField(max_length=250)
	contactnumber = models.CharField(max_length=250)
	email = models.EmailField(blank=True)

class singleservice(models.Model):
	name = models.CharField(max_length=250)
	phonenumber = models.CharField(max_length=250)
	email = models.EmailField(blank=True)

