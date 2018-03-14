import requests
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
import smtplib
from django.contrib.sessions.models import Session
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import datetime
#from datetime import timedelta


from .models import singleservice 
from .models import adduser 
from .models import fulliteservice 
from .models import hotelservice 
from .models import adminsignup 
from .models import employeedetail 
from .models import pricingplan 

#from datetime import datetime,timedelta
#from time import strftime
from django.conf.urls import include, url


from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.core.mail import EmailMessage

def send_complex_message(request):
    return requests.post(
					"https://api.mailgun.net/v3/sandbox8d00a0060a5c4befbd280ae759883df7.mailgun.org",
					auth=("api", "key-72442c5f7222d9e4ee790c61b0da37ba"),
					data={"from": "Excited User <YOU@YOUR_DOMAIN_NAME>",
						"to": "kalpana@codenomad.net",
						"subject": "Hello",
						"text": "Testing some Mailgun awesomness!",
					  "html": "HTML version of the body"
						}
					)
					
def abd(request):

	send_mail("It works!", "This will get sent through Mailgun",
          "Anymail Sender <kalpana@codenomad.net>", ["aman@codenomad.net"])


    # return requests.post(
        # "https://api.mailgun.net/v3/sandbox8d00a0060a5c4befbd280ae759883df7.mailgun.org/messages",
        # auth=("api", "key-72442c5f7222d9e4ee790c61b0da37ba"),
       # data={"from": "Excited User <excited@samples.mailgun.org>",
              # "to": ["aman@codenomad.net"],
              # "subject": "Hello",
              # "text": "Testing some Mailgun awesomeness!"})


# Create your views here.
def index(request):
    #return HttpResponse('Hefdd gfdgdf llo fddcccx xczfddvd x dddrom Python!')
	# services = Hotelservice.objects.all()
	 return render(request, 'index.html')
	 
##############Onze-prijzen//////////////////////////	 
def onzeprijzen(request):
    return render(request, 'onzeprijzen.html')


def login1(request):
	username = 'not logged in'
	first_name = ''
	password = ''
	existid = ''
	#return HttpResponse('hello')
	getsession = request.session.get('id')=='None'
	if request.session.get('id')=='None':
		redirect(login1)
	else:
	
		if request.method == 'POST':
			first_name = request.POST.get('first_name')
			password = request.POST.get('password')
			getw =  Signup.objects.filter(first_name=first_name,password=password).order_by('-id')[:1]
			#return HttpResponse("name")
			for i in getw:
				existid = i.id
				if existid: 
					request.session['id'] = existid
					return redirect(welcome)
				else:
					# #request.session['error'] = 'User not identified'
					return redirect(login1)
				
	return render(request, 'login.html') 
		
def welcome(request):
	getsession = request.session.get('id')
	if getsession:
		getrecord =  Signup.objects.get(id=getsession)
		return render(request, 'welcome.html',{'form':getrecord}) 
	else:
		return redirect(login1)


def logout1(request):
	try:
		del request.session['id']
	except KeyError:
		return HttpResponse("You're logged out.")
	return redirect(login1)



#backed login

def addadmindetails(request):

	adminsignup1 = adminsignup()
	adminsignup1.firstname='admin'
	#adminsignup1.lastname='admin'
	adminsignup1.email='admin@gmail.com'
	adminsignup1.password='admin@123' 
	adminsignup1.save()
	#contacts = adminsignup.objects.all()
	return HttpResponse("You're logged out.")
	#return render(request)
	
##################################backed login##############################################
def admin(request):
	username = ''
	password = ''
	existid = ''
	#request.session['error']=""
	#error = request.session.get('error')
	
	#return HttpResponse('hello')
	getsession = request.session.get('adminid')=='None'
	if request.session.get('adminid')=='None':
		redirect(admin)
	else:
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			getw =  adminsignup.objects.filter(firstname=username,password=password).order_by('-id')[:1]
			existid = 0
			for i in getw:
				existid = i.id
			
			if existid: 
				request.session['adminid'] = existid
				return redirect(home)
			else:
				error = 'Invalid Username and Password'
				#return HttpResponse(error)
					#return redirect(admin)
					
				return render(request, 'backend/admin.html',{'errors': error})
				
	return render(request, 'backend/admin.html') 

def home(request):
	
	getsession = request.session.get('adminid')
	if getsession:
		getrecord =  adminsignup.objects.get(id=getsession)
		return render(request, 'backend/welcome.html',{'getadta':getrecord}) 
	else:
		return redirect(admin)
	return render(request, 'backend/welcome.html')
	


def services(request):
	getsession = request.session.get('adminid')
	if getsession:
		getrecord =  adminsignup.objects.get(id=getsession)
		error=""
		if request.method == 'POST':
			try:
				#filee = request.files['image_file']
				#filename = secure_filename(file.filename)
				filee = request.FILES.get('image_file')
				servicename = request.POST.get('servicename')
				description = request.POST.get('description') 
				data = Hotelservice(servicename=servicename,description=description,serviceimage=filee)
				data.save()
				error = "Service added successfully"
				return render(request, 'backend/hotelservices.html',{'getadta':getrecord, 'success':error})
			except KeyError:
				#return HttpResponse(str(e))
				error="Service not added."
				return render(request, 'backend/hotelservices.html',{'getadta':getrecord, 'success':error})
		else:
			error=""
			return render(request, 'backend/hotelservices.html',{'getadta':getrecord, 'success':error}) 
		
		
		
		
		#return render(request, 'backend/hotelservices.html',{'getadta':getrecord}) 
	else:
		return redirect(admin)
	#return render(request, 'backend/welcome.html')

############################ add users at backend ########################################

def adduser1(request):
	getsession = request.session.get('adminid')
	getrecord =  adminsignup.objects.get(id=getsession)
	error='';
	if getsession:
		if request.method== 'POST':
			try:
				firstname = request.POST.get('firstname')
				lastname = request.POST.get('lastname')
				username = request.POST.get('username')
				email = request.POST.get('email')
				contact1 = request.POST.get('contact')
				now = datetime.datetime.now()
				#print(request.POST)
			#	return HttpResponse(contact1)
				status = '0'
				data = adduser(firstname=firstname,lastname=lastname,username=username,contactnumber='3213232',dateofjoin=now,status=status,email=email)
				data.save()
				error = "Service added successfully"
				return render(request, 'backend/adduser1.html',{'getadta':getrecord,'success':error})
			except KeyError:
				#return HttpResponse(str(e))
				error="Service not added."
				return render(request, 'backend/adduser1.html',{ 'getadta':getrecord,'success':error})
		else:
			error=""
			return render(request, 'backend/adduser1.html',{'getadta':getrecord,'success':error}) 
					
				
			
		return render(request, 'backend/adduser1.html') 
	else:
		return redirect(admin)
	#return HttpResponse("dfdfdsfdsf")


def getuser(request):
	getsession = request.session.get('adminid')
	getrecord1 =  adminsignup.objects.get(id=getsession)
	getdata1 =  adduser.objects.all().order_by('id')[::-1]
	return render(request, 'backend/getuser.html',{'getadta':getrecord1,'getrecord':getdata1}) 

def deleteuser(request):
	
		try:
			deluser = request.POST.get('userid')
			adduser.objects.filter(id=deluser).delete()
			messages.success(request, 'User deleted successfully!')
			return redirect(getuser)
		except KeyError:
				#return HttpResponse(str(e))
				error="Due to error user not deleted."
				return render(request, 'backend/getuser.html',{ 'getadta':getrecord,'success':error})

				
				

def logoutadmin(request):
	#return HttpResponse(request.session['id'])
	try:
		del request.session['adminid']
	#except KeyError as e:
	except KeyError:
		#return HttpResponse(str(e))
		return HttpResponse("You're logged out.")
	return redirect(admin)
	
	
	
#################add employee and get employeeee###########
def addemployee(request):
	getsession = request.session.get('adminid')
	getrecord =  adminsignup.objects.get(id=getsession)
	error='';
	if getsession:
		if request.method== 'POST':
			try:
				employeename = request.POST.get('employeename')
				username = request.POST.get('username')
				email = request.POST.get('email')
				contactnumber = request.POST.get('contact')
				now = datetime.datetime.now()
				#print(request.POST)
				#return HttpResponse(employeename)
				data = employeedetail(employeename=employeename,contactnumber=contactnumber,username=username,dateofjoin=now,email=email)
				data.save()
				error = "New employee added successfully"
				return render(request, 'backend/addnewemployee.html',{'getadta':getrecord,'success':error})
			except KeyError:
				#return HttpResponse(str(e))
				error="New employee not added due to error."
				return render(request, 'backend/addnewemployee.html',{ 'getadta':getrecord,'success':error})
		else:
			error=""
			return render(request, 'backend/addnewemployee.html',{'getadta':getrecord,'success':error}) 
					
				
			
		return render(request, 'backend/addnewemployee.html') 
	else:
		return redirect(admin)
	#return render(request, 'backend/addnewemployee.html')
	
	
def getemployee(request):
	getsession = request.session.get('adminid')
	getrecord1 =  adminsignup.objects.get(id=getsession)
	getemployeedetails =  employeedetail.objects.all().order_by('id')[::-1]
	return render(request, 'backend/getemployee.html',{'getadta':getrecord1,'getemployeedetail':getemployeedetails}) 
	

def deleteemployee(request):
	
		try:
			delemp = request.POST.get('id')
			
			#return HttpResponse(delemp)
			#delemp = request.POST.get(id)
			employeedetail.objects.filter(id=delemp).delete()
			messages.success(request, 'Employee deleted successfully!')
			return redirect(getemployee)
		except KeyError:
				#return HttpResponse(str(e))
				error="Due to error employee not deleted."
				return render(request, 'backend/addnewemployee.html',{ 'getadta':getrecord,'success':error})
	
		
##########################frontend integrationnnnnnnnnnn#######################

##################################holoday page in dutchh.html integration######################################
def woningverhuur(request):
	return render(request, 'woning-verhuur.html')
	
##################################holiday.html for english integration###################################
def holiday(request):
	return render(request, 'en/holiday.html')
	
def fullliteserviceenglish(request):
	if request.method=='POST':
			try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					services = request.POST.get('services')
					#now1 = datetime.datetime.now()
					now = datetime.datetime.now()
					#return HttpResponse('hello12')
			 
					data = fulliteservice(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,services=services,currentdate=now) 
					data.save()
					# subject, from_email, to = 'New Request', 'from@example.com','hello@clubfred.nl'
					# text_content = 'New Request'
					# html_content = ' Hi Fred,<br/>'
					# html_content += ' You just received a holiday service request of<b> ['+firstname+']</b> with the following information:<br/><br/><br/>'
					# html_content += '<b> Name:'+firstname+'</b><br/>'
					# html_content += '<b> Address:'+address+'</b><br/>'
					# html_content += '<b> Phone number:'+mobilenumber+'</b><br/>'
					
					# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
					# msg.attach_alternative(html_content, "text/html")
					# msg.send()
					##########for user##############
					# subject1, from_email1, to1 = 'New Request', 'hello@clubfred.nl',email
					# text_content1 = 'Thanks for interest'
					
					# html_content1 = '<h2> Thank you for your interest in our services.</h2>'
					
					# msg1 = EmailMultiAlternatives(subject1, text_content1, from_email1, [to1])
					# msg1.attach_alternative(html_content1, "text/html")
					# msg1.send()
					messages.success(request, 'Thanks to select your service.')
					return redirect(holiday)
					
					
			except KeyError:
					return redirect(holiday)
	else:
			 return redirect(holiday)

def fullliteservice(request):
	if request.method=='POST':
			try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					services = request.POST.get('services')
					#now1 = datetime.datetime.now()
					now = datetime.datetime.now()
					#return HttpResponse('hello12')
			 
					data = fulliteservice(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,services=services,currentdate=now) 
					data.save()
					# subject, from_email, to = 'New Request', 'from@example.com','hello@clubfred.nl'
					# text_content = 'New Request'
					# html_content = ' Hi Fred,<br/>'
					# html_content += ' You just received a holiday(woning-verhuur) service request of<b> ['+firstname+']</b> with the following information:<br/><br/><br/>'
					# html_content += '<b> Name:'+firstname+'</b><br/>'
					# html_content += '<b> Address:'+address+'</b><br/>'
					# html_content += '<b> Phone number:'+mobilenumber+'</b><br/>'
					
					# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
					# msg.attach_alternative(html_content, "text/html")
					# msg.send()
					##########for user##############
					# subject1, from_email1, to1 = 'New Rquest', 'hello@clubfred.nl',email
					# text_content1 = 'Thanks for interest'
					
					# html_content1 = '<h2> Thank you for your interest in our services.</h2>'
					
					# msg1 = EmailMultiAlternatives(subject1, text_content1, from_email1, [to1])
					# msg1.attach_alternative(html_content1, "text/html")
					# msg1.send()
					messages.success(request, 'Thanks to select your service.')
					return redirect(woningverhuur)
					
					
			except KeyError:
					return redirect(woningverhuur)
	else:
			 return redirect(woningverhuur)

	
##################################en.html for english integration###################################
def en(request):
	return render(request, 'en/index.html')


##################################hotel.html integration######################################
def hotel(request):
	return render(request, 'en/hotel.html')
	
	##################################en/pricing.html integration######################################
def pricing(request):
	return render(request, 'en/pricing.html')
	
	

#############singleservice from in pricing for english #####################e
def singleservice1(request):
	if request.method=='POST':
			try:
					name = request.POST.get('name')
					phonenumber = request.POST.get('phonenumber')
					email = request.POST.get('email')
					
			 
					data = singleservice(name=name,email=email,phonenumber=phonenumber) 
					data.save()
					# subject, from_email, to = 'New Request', 'from@example.com','hello@clubfred.nl'
					# text_content = 'New Request'
					# html_content = ' Hi Fred,<br/>'
					# html_content += ' You just received a Single service request of<b> ['+name+']</b> with the following information:<br/><br/><br/>'
					# html_content += '<b> Name:'+name+'</b><br/>'
					# html_content += '<b> Phone number:'+phonenumber+'</b><br/>'
					
					# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
					# msg.attach_alternative(html_content, "text/html")
					# msg.send()
					##########for user##############
					# subject1, from_email1, to1 = 'New Request', 'hello@clubfred.nl',email
					# text_content1 = 'Thanks for interest'
					
					# html_content1 = '<h2> Thank you for your interest in our services.</h2>'
					
					# msg1 = EmailMultiAlternatives(subject1, text_content1, from_email1, [to1])
					# msg1.attach_alternative(html_content1, "text/html")
					# msg1.send()
					messages.success(request, 'Thanks to select your service.')
					return redirect(pricing)
					
					
			except KeyError:
					return redirect(pricing)
	else:
			 return redirect(pricing)
#############singleservice from in pricing for ductchh #####################e
def singleservicefordutch(request):
	if request.method=='POST':
			try:
					name = request.POST.get('name')
					phonenumber = request.POST.get('phonenumber')
					email = request.POST.get('email')
					data = singleservice(name=name,email=email,phonenumber=phonenumber) 
					data.save()
					
					# subject, from_email, to = 'New Request', 'from@example.com','hello@clubfred.nl'
					# text_content = 'New Request'
					# html_content = ' Hi Fred,<br/>'
					# html_content += ' You just received a Single service request of<b> ['+name+']</b> with the following information:<br/><br/><br/>'
					# html_content += '<b> Name:'+name+'</b><br/>'
					# html_content += '<b> Phone number:'+phonenumber+'</b><br/>'
					
					# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
					# msg.attach_alternative(html_content, "text/html")
					# msg.send()
					##########for user##############
					# subject1, from_email1, to1 = 'New Request', 'hello@clubfred.nl',email
					# text_content1 = 'Thanks for interest'
					
					# html_content1 = '<h2> Thank you for your interest in our services.</h2>'
					
					# msg1 = EmailMultiAlternatives(subject1, text_content1, from_email1, [to1])
					# msg1.attach_alternative(html_content1, "text/html")
					# msg1.send()
					messages.success(request, 'Thanks to select your service.')
					return redirect(onzeprijzen)
					
					
			except KeyError:
					return redirect(onzeprijzen)
	else:
			 return redirect(onzeprijzen)
	
	
def help(request):
		
		if request.method=='POST':
			try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					services = request.POST.get('services')
					#now1 = datetime.datetime.now()
					now = datetime.datetime.now()
					#return HttpResponse('hello12')
			 
					data = hotelservice(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,services=services,currentdate=now) 
					data.save()
					# subject, from_email, to = 'New Request', 'from@example.com','hello@clubfred.nl'
					# text_content = 'New Request'
					# html_content = ' Hi Fred,<br/>'
					# html_content += ' You just received a service request of<b> ['+firstname+']</b> with the following information:<br/><br/><br/>'
					# html_content += '<b> Name:'+firstname+'</b><br/>'
					# html_content += '<b> Address:'+address+'</b><br/>'
					# html_content += '<b> Phone number:'+mobilenumber+'</b><br/>'
					
					# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
					# msg.attach_alternative(html_content, "text/html")
					# msg.send()
					##########for user##############
					# subject1, from_email1, to1 = 'New Request', 'hello@clubfred.nl',email
					# text_content1 = 'Thanks for interest'
					
					# html_content1 = '<h2> Thank you for your interest in our services.</h2>'
					
					# msg1 = EmailMultiAlternatives(subject1, text_content1, from_email1, [to1])
					# msg1.attach_alternative(html_content1, "text/html")
					# msg1.send()
					messages.success(request, 'Thanks to select your plan.')
					return redirect(hotel)
					
					
			except KeyError:
					return redirect(hotel)
					
					
					
		else:
			 return redirect(hotel)
			
			

##################################prize.html integration######################################

def priceperweek(request):
		if request.method== 'POST':
				try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					amount = request.POST.get('amount')
					#now = datetime.datetime.now().strftime('%H:%M')
					verify = '0'
					data = pricingplan(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,amount=amount,verify=verify) 
					data.save()
					# mail_subject = 'Confirmation mail'
					# message = render_to_string('acc_active_email.html', {
					# 'user': firstname,
					# 'domain': 'https://clubfred.herokuapp.com/',
					# 'uid':data.pk,
					# })
					# to_email = email
					# emails = EmailMessage(
					# mail_subject, message, to=[to_email] )
					# emails.send()
					# subject, from_email, to = 'New Private Client', 'from@example.com','hello@clubfred.nl'
					# text_content = 'New Private Client'
					# html_content = ' Hi Fred,<br/>'
					# html_content += ' You just received a service request of<b> ['+firstname+']</b> with the following information:<br/><br/><br/>'
					# html_content += '<b> Name:'+firstname+'</b><br/>'
					# html_content += '<b> Address:'+address+'</b><br/>'
					# html_content += '<b> Phone number:'+mobilenumber+'</b><br/>'
					# html_content += '<b> Price plan chosen:'+amount+'</b><br/>'
					# html_content += '<b> Date of visit:'+date+'</b><br/>'
					# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
					# msg.attach_alternative(html_content, "text/html")
					# msg.send()
					##########for user##############
					# subject1, from_email1, to1 = 'New Request', 'from@example.com',email
					# text_content1 = 'Thanks for interest'
					
					# html_content1 = '<h2> Thank you for your interest in our services.</h2>'
					
					# msg1 = EmailMultiAlternatives(subject1, text_content1, from_email1, [to1])
					# msg1.attach_alternative(html_content1, "text/html")
					# msg1.send()
					return redirect(onzeprijzen)
				except KeyError:
					#return HttpResponse(str(e))
					messages.success(request, 'There is some error due to select your plan.')
					
					return redirect(onzeprijzen)
		else:
			messages.success(request, 'Price data is nott added successfully!')
			return redirect(onzeprijzen)
			
	##################################prize.html for englinshintegration######################################

def priceperweekenglish(request):
		if request.method== 'POST':
				try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					amount = request.POST.get('amount')
					now = datetime.datetime.now()
					verify = '0'
					#return HttpResponse(now)
					data = pricingplan(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,amount=amount,verify=verify,currenttime=now) 
					data.save()
					# mail_subject = 'Confirmation mail'
					
					# message = render_to_string('acc_active_email.html', {
					# 'user': firstname,
					# 'domain': 'https://clubfred.herokuapp.com/',
					# 'uid':data.pk,
					# })
					# to_email = email
					# emails = EmailMessage(
					# mail_subject, message, to=[to_email] )
					# emails.send()
					
					# subject, from_email, to = 'New Private Client', 'from@example.com','hello@clubfred.nl'
					# text_content = 'New Private Client'
					# html_content = ' Hi Fred,<br/>'
					# html_content += ' You just received a service request of<b> ['+firstname+']</b> with the following information:<br/><br/><br/>'
					# html_content += '<b> Name:'+firstname+'</b><br/>'
					# html_content += '<b> Address:'+address+'</b><br/>'
					# html_content += '<b> Phone number:'+mobilenumber+'</b><br/>'
					# html_content += '<b> Price plan chosen:'+amount+'</b><br/>'
					# html_content += '<b> Date of visit:'+date+'</b><br/>'
					# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
					# msg.attach_alternative(html_content, "text/html")
					# msg.send()
					##########for user##############
					# subject1, from_email1, to1 = 'New Request', 'from@example.com',email
					# text_content1 = 'Thanks for interest'
					
					# html_content1 = '<h2> Thank you for your interest in our services.</h2>'
					
					# msg1 = EmailMultiAlternatives(subject1, text_content1, from_email1, [to1])
					# msg1.attach_alternative(html_content1, "text/html")
					# msg1.send()
					return redirect(pricing)
				except KeyError:
					#return HttpResponse(str(e))
					messages.success(request, 'There is some error due to select your plan.')
					
					return redirect(pricing)
		else:
			messages.success(request, 'Price data is nott added successfully!')
			return redirect(pricing)

def abc(request):

	# date_time_newer = datetime.datetime.now()
	# user = pricingplan.objects.get(id=31)
	# cureentdatetime = datetime.datetime.strptime(user.currenttime,'%Y-%m-%d %H:%M:%S.%f')
	# date_time_difference = (date_time_newer-cureentdatetime).total_seconds()/60
	# return HttpResponse(date_time_difference)
	message1 = ('clientmail', 'thanks is the message', 'clubfred',['kd.kalpana13@gmail.com', 'other@example.com'])
	message2 = ('admin mail', 'Here is another message','clubfred', ['ankushpagrotra@gmail.com'])

	res  = send_mass_mail((message1, message2), fail_silently=False)
	if res:
		return HttpResponse('hesssllo')
	else:
		return HttpResponse('nhhv')
	# subject, from_email, to = 'New Private Client', 'from@example.com', 'kalpana@codenomad.net'
	# text_content = 'This is an important message.'
	# html_content = ' Hi Fred'
	# html_content += ' You just received a service request of [NAME CLIENT] with the following information:'
	# html_content += ' Name:kalpana'
	# html_content += ' calss:send'
	# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	# msg.attach_alternative(html_content, "text/html")
	# msg.send()
	

############activate confirmation#####################
			
def activate(request, uidb64):
	try:
		error=''
		uid = uidb64
		user = pricingplan.objects.get(pk=uid)
		date_time_newer = datetime.datetime.now()
		#user = pricingplan.objects.get(id=31)
		cureentdatetime = datetime.datetime.strptime(user.currenttime,'%Y-%m-%d %H:%M:%S.%f')
		date_time_difference = (date_time_newer-cureentdatetime).total_seconds()/60
		if date_time_difference < 30:
			user.verify = 1
			user.save()
			error=1
			return render(request, 'activate.html',{'success':error})
			#return HttpResponse('Thank you for your  confirmation.')
		else:
			return render(request, 'activate.html',{'success':error})
			#return HttpResponse('Your time is out')
		#return HttpResponse(date_time_difference)
		# user.verify = 1
		# user.save()
		# return HttpResponse('Thank you for your  confirmation.')
	except(TypeError, ValueError, OverflowError, pricingplan.DoesNotExist):
			# user = None
			# user.verify = 1
			# user.save()
			#login(request, user)
			# return redirect('home')
			return HttpResponse('Due to some error not working')
			

		
def airbnb(request):
	getsession = request.session.get('adminid')
	if getsession:
		getrecord1 =  adminsignup.objects.get(id=getsession)
		getdata1 =  fulliteservice.objects.all().order_by('id')[::-1]
		return render(request, 'backend/airbnb.html',{'getadta':getrecord1,'getrecord':getdata1})
	else:
			return render(request, 'backend/admin.html', {})

def hotels(request):
	getsession = request.session.get('adminid')
	if getsession:
		getrecord1 =  adminsignup.objects.get(id=getsession)
		getdata1 =  hotelservice.objects.all().order_by('id')[::-1]
		return render(request, 'backend/hotelservice.html',{'getadta':getrecord1,'getrecord':getdata1})
	else:
			return render(request, 'backend/admin.html', {})

def getsingleservices(request):
	getsession = request.session.get('adminid')
	if getsession:
		getrecord1 =  adminsignup.objects.get(id=getsession)
		getdata1 =  singleservice.objects.all().order_by('id')[::-1]
		return render(request, 'backend/singleservice.html',{'getadta':getrecord1,'getrecord':getdata1})
	else:
			return render(request, 'backend/admin.html', {})
	
	##########################edit and delete single service page####################
def editsingleservice(request,userid):
	getsession = request.session.get('adminid')
	if getsession:
		getrecord1 =  adminsignup.objects.get(id=getsession)
		getparticularrecord =  singleservice.objects.get(id=userid)
		return render(request, 'backend/getsingleservice.html',{'getadta':getrecord1,'getsingleservice':getparticularrecord})
	else:
			return render(request, 'backend/admin.html', {})
	 
def updatesingleservice(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	phonenumber = request.POST.get('phonenumber')
	#return HttpResponse(name + email + phonenumber)
	userid = request.POST.get('userid')
	to_update = singleservice.objects.filter(id=userid).update(name=name,email=email,phonenumber=phonenumber)
	messages.success(request, 'Update single service request successfully.')
	return redirect(getsingleservices)
	
	
def deletesingleservice(request):

	file_info = request.POST.get('userid').split(',')
	for  i in file_info:
		singleservice.objects.filter(id=i).delete()
	messages.success(request, 'Service deleted successfully!')
	return redirect(getsingleservices)
	
	
#############################update and delete particular pricing plan#####################
def pricingplans(request):
		getsession = request.session.get('adminid')
		if getsession:
			getrecord1 =  adminsignup.objects.get(id=getsession)
			#getpricing =  pricingplan.objects.filter(verify=1).order_by('id')[::-1]
			getpricing =  pricingplan.objects.all().order_by('id')[::-1]
			return render(request, 'backend/pricingplan.html',{'getadta':getrecord1,'getpricingdetail':getpricing}) 
		else:
			return render(request, 'backend/admin.html', {})
		
def editpricingplan(request,userid):
	getsession = request.session.get('adminid')
	if getsession:
		getrecord1 =  adminsignup.objects.get(id=getsession)
		getparticularrecord =  pricingplan.objects.get(id=userid)
		return render(request, 'backend/getpricingplan.html',{'getadta':getrecord1,'getpricingservice':getparticularrecord})
	else:
			return render(request, 'backend/admin.html', {})

def updateprice(request):
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	zipcode = request.POST.get('zipcode')
	mobilenumber = request.POST.get('mobilenumber')
	address = request.POST.get('address')
	unit = request.POST.get('unit')
	#return HttpResponse(name + email + phonenumber)
	userid = request.POST.get('userid')
	to_update = pricingplan.objects.filter(id=userid).update(firstname=firstname,lastname=lastname,email=email,zipcode=zipcode,mobilenumber=mobilenumber,address=address,unit=unit)
	messages.success(request, 'Update Pricing plan request successfully.')
	return redirect(pricingplans)

def deletepriceservice(request):
	#file_info=[]
	
	
	file_info = request.POST.get('userid').split(',')
	
	for  i in file_info:
		pricingplan.objects.filter(id=i).delete()

	messages.success(request, 'Service deleted successfully!')
	return redirect(pricingplans)
		
	#thumbnail_list.append(file_info)
	
	
	
	
	
	
#######################edit and delete airbnb#############################
def editairbnb(request,userid):
	getsession = request.session.get('adminid')
	if getsession:
		
		getrecord1 =  adminsignup.objects.get(id=getsession)
		getparticularrecord =  fulliteservice.objects.get(id=userid)
		return render(request, 'backend/getairbnb.html',{'getadta':getrecord1,'getairbnb':getparticularrecord})
	else:
			return render(request, 'backend/admin.html', {})

def updateairbnb(request):
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	zipcode = request.POST.get('zipcode')
	mobilenumber = request.POST.get('mobilenumber')
	address = request.POST.get('address')
	unit = request.POST.get('unit')
	userid = request.POST.get('userid')
	to_update = fulliteservice.objects.filter(id=userid).update(firstname=firstname,lastname=lastname,email=email,zipcode=zipcode,mobilenumber=mobilenumber,address=address,unit=unit)
	messages.success(request, 'Update service request successfully.')
	return redirect(airbnb)

def deleteairbnb(request):
	file_info = request.POST.get('userid').split(',')
	for  i in file_info:
		fulliteservice.objects.filter(id=i).delete()
	messages.success(request, 'Service deleted successfully!')
	return redirect(airbnb)

#######################edit and delete hotel service#############################
def edithotelservice(request,userid):
	getsession = request.session.get('adminid')
	if getsession:
		getrecord1 =  adminsignup.objects.get(id=getsession)
		getparticularrecord =  hotelservice.objects.get(id=userid)
		return render(request, 'backend/gethotelservice.html',{'getadta':getrecord1,'gethotelservice':getparticularrecord})
	else:
			return render(request, 'backend/admin.html', {})

def updatehotelservice(request):
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	zipcode = request.POST.get('zipcode')
	mobilenumber = request.POST.get('mobilenumber')
	address = request.POST.get('address')
	unit = request.POST.get('unit')
	userid = request.POST.get('userid')
	to_update = hotelservice.objects.filter(id=userid).update(firstname=firstname,lastname=lastname,email=email,zipcode=zipcode,mobilenumber=mobilenumber,address=address,unit=unit)
	messages.success(request, 'Service updated  request successfully.')
	return redirect(hotels)

def deletehotelservice(request):
	file_info = request.POST.get('userid').split(',')
	for  i in file_info:
		hotelservice.objects.filter(id=i).delete()
	messages.success(request, 'Service deleted successfully!')
	return redirect(hotels)

def testing(request):
	return render(request,'backend/test.html')
	
def ajaxdata(request):
	return render(request,'testing.html')