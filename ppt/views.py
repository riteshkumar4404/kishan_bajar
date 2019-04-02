from django.contrib import messages
from .models import User_Detail,Product,Category,Purchase
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.mail import send_mail
#from django shortcuts import render_to_response,RequestContext 
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def home(request):
	a=''
	user=''
	#if request.method=='GET':
	uname=request.GET.get('uname')
	if uname=='None':
		uname=''
	if uname:
		user=User_Detail.objects.filter(username=uname)
	categories=Category.objects.filter(active='1')
	products=Product.objects.filter(active='1')
	return render(request,'home.html',{'a':a,'uname':uname,'categories':categories,'products':products,'userdetails':user})
def navcategory(request):
	#boards=Board.objects.all()
	cat=''
	if request.method=='GET':
		pk=request.GET['cpk']
		uname=request.GET['uname']
	user=User_Detail.objects.filter(username=uname)
	if uname=='None':
		uname=''
	categories=Category.objects.filter(active='1')
	catproduct=Product.objects.filter(pcategoryid=pk,active='1')
	k=Product.objects.filter(pcategoryid=pk,active='1')
	for mn in k:
		cat=mn.pcategoryid.categoryname
	
	return render(request,'navcategory.html',{'catproduct':catproduct,'cat':cat,'uname':uname,'categories':categories,'userdetail':user})
		
	
def changepassword(request,pk):
	msg="your old password donot match"
	msg1="newpassword and password confirm do not match"
	if request.method=='POST':
		oldpassword=request.POST['oldpassword']
		newpassword=request.POST['newpassword']
		newpconfirm=request.POST['newpconfirm']
		categories=Category.objects.filter(active='1')
		userdetail=User_Detail.objects.filter(id=pk)
		if userdetail[0].password==oldpassword and newpassword==newpconfirm:
			user=User_Detail.objects.get(id=pk)
			user.password=newpassword
			user.save()
			return render(request,'home.html',{'i':pk,'categories':categories})
		elif userdetail[0].password!=oldpassword: 
			return render(request,'changepassword.html',{'i':pk,'msg':msg})
		else:
			return render(request,'changepassword.html',{'i':pk,'msg':msg1})
	else:
		return render(request,'changepassword.html',{'i':pk})
		

def logout1(request):
	
	products=Product.objects.filter(active='1')
	categories=Category.objects.filter(active='1')
	return render(request,'home.html',{'categories':categories,'products':products})
"""def login(request):
	
	categories=Category.objects.filter(active='1')
	msg=" Sorry for the inconvineance but you have been blocked by the admin for more details please contact the admin"
	notfound="Username or password Incorrect"
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		userdetail=User_Detail.objects.filter(username=username,password=password)
		for j in userdetail:
			i=j.id
			break
		if userdetail.count()>0 and userdetail[0].active=='0':
			return render(request,'login.html',{'msg':msg})
		elif userdetail.count()>0 and userdetail[0].active!='0':
			
			return render(request,'home.html',{'uname':username,'categories':categories,'i':i})
		else:
			return render(request,'login.html',{'msg':notfound})
	else:
		return render(request,'login.html',{})
"""

def checking(request):
	if request.method=='GET':
		pk=request.GET.get('ipk')
		uname=request.GET.get('uname','')
	if uname=='None':
		uname=''
	user=User_Detail.objects.filter(username=uname)
	categories=Category.objects.filter(active='1')
	#category=Category.object.filter(pcategoryid=pk)
	catproduct1=Product.objects.filter(pname=pk,active='1')
	#if uname :
	return render(request,'productcategory.html',{'catproduct1':catproduct1,'userdetails':user,'uname':uname,'categories':categories})
	"""else:
		return redirect('login')"""



def login(request):
	products=Product.objects.filter(active='1')
	
	categories=Category.objects.filter(active='1')
	msg=" you have been blocked by the admin for more details please contact the admin"
	msg1="Enter correct details"
	notfound="Username or password Incorrect"
	if request.method=='POST':
		username=request.POST['Username']
		password=request.POST['Password']
		type=request.POST['sort']
		userdetail=User_Detail.objects.filter(username=username,password=password,utype=type)
		for j in userdetail:
			i=j.active
			a=j.id
			break
		if userdetail.count()>0 and i=='0':
			return render(request,'login.html',{'msg':msg})
		elif userdetail.count()>0 and i!='0' and j.utype=='Admin':
			return render(request,'admin1.html',{'uname':j,'categories':categories,'i':a})
		elif userdetail.count()>0 and i!='0' and j.utype=='User':
			return render(request,'home.html',{'uname':username,'categories':categories,'userdetails':userdetail,'i':a,'products':products,})
		elif userdetail.count()==0:
			return render(request,'login.html',{'msg':msg1})
		else:
			return render(request,'login.html',{'msg':notfound})
	else:
		return render(request,'login.html')
		
def signup(request):
	msg="Password and Confirm Password Do not match Please Retry"
	if request.method=='POST':
		username=request.POST.get('username','')
		password=request.POST.get('password1','')
		pconfirm=request.POST.get('confpass','')
		name=request.POST.get('name1','')
		phone=request.POST.get('phone')
		city=request.POST.get('city')
		state=request.POST.get('state')
		pin=request.POST.get('pin')
		address=request.POST.get('address')
		email=request.POST.get('email')
		if(password==pconfirm):
			user_detail=User_Detail.objects.create(
				username=username,
				email=email,
				password=password,
				utype="User",
				active='1',
				name=name,phone=phone,city=city,state=state,pin=pin,address=address,)
			return render(request,'login.html',{})	
		else:
			return render(request,'signup.html',{'msg':msg})
	return render(request,'signup.html',{})	

def myaccount(request,pk):
	categories=Category.objects.filter(active='1')
	productdetails=Product.objects.filter(user_detailid=pk)
	user=User_Detail.objects.filter(id=pk)
	purchase=Purchase.objects.filter(purchaseuid=pk)
	for u in user:
		uname=u.username
	
	return render(request,'myaccount.html',{'purchase':purchase,'productdetails':productdetails,'categories':categories,'uname':uname,'userdetails':user})
	
def contact(request):
	uname=request.GET['uname']
	if uname=='None':
		uname=''
	user=User_Detail.objects.filter(username=uname,active='1')
	categories=Category.objects.filter(active='1')
	
	return render(request,'meet_the_team.html',{'uname':uname,'categories':categories,'user':user})		

	
def info(request):
	#if request.method=='GET':
	user=''
	uname=request.GET.get('uname')
	if uname=='None':
		uname=''
	if uname:
		user=User_Detail.objects.filter(username=uname,active='1')
	categories=Category.objects.filter(active='1')
	
	return render(request,'information.html',{'uname':uname,'categories':categories,'userdetails':user})	

def insidehome(request):
	product=Products.objects.all()
	return render (request,'insidehome.html',{'product':product})
	
def admin1(request):
	return render(request,'admin1.html',)
def user(request):
	categories=Category.objects.filter(active='1')
	userdetails=User_Detail.objects.all()
	if request.method=='GET':
		uname=request.GET.get('uname','')
	user=User_Detail.objects.filter(username=uname)
	i=''
	for j in user:
		i=j.id
	return render(request,'user.html',{'userdetails':userdetails,'categories':categories,'uname':uname,'i':i})
def product(request):
	categories=Category.objects.filter(active='1')
	if request.method=='GET':
		uname=request.GET.get('uname')
	user=User_Detail.objects.filter(username=uname)
	i=''
	for j in user:
		i=j.id
	products=Product.objects.all()
	return render(request,'product.html',{'products':products,'categories':categories,'uname':uname,'i':i})
def category(request):
	categorie=Category.objects.filter(active='1')
	if request.method=='GET':
		uname=request.GET.get('uname')
	user=User_Detail.objects.filter(username=uname)
	#i=user.id
	i=''
	for j in user:
		i=j.id
	categories=Category.objects.all()
	return render(request,'category.html',{'categories':categories,'categorie':categorie,'uname':uname,'i':i})
def purchase(request):
	categories=Category.objects.filter(active='1')
	if request.method=='GET':
		uname=request.GET['uname']
	user=User_Detail.objects.get(username=uname)
	i=user.id
	purchased=Purchase.objects.all()
	return render(request,'purchased.html',{'purchased':purchased,'categories':categories,'uname':uname,'i':i})
def useractivate(request,pk):
	categories=Category.objects.filter(active='1')
	userdetails=User_Detail.objects.all()
	if request.method=='GET':
		uname=request.GET.get('uname','')
	user=User_Detail.objects.filter(username=uname)
	i=''
	for j in user:
		i=j.id
	user=User_Detail.objects.get(id=pk)
	user.active='1'
	user.save()
	#return redirect('user')	
	return render(request,'user.html',{'userdetails':userdetails,'categories':categories,'uname':uname,'i':i})
def userdeactivate(request,pk):
	categories=Category.objects.filter(active='1')
	userdetails=User_Detail.objects.all()
	if request.method=='GET':
		uname=request.GET.get('uname','')
	user=User_Detail.objects.filter(username=uname)
	i=''
	for j in user:
		i=j.id
	user=User_Detail.objects.get(id=pk)
	user.active='0'
	user.save()
	#return redirect('user')	
	return render(request,'user.html',{'userdetails':userdetails,'categories':categories,'uname':uname,'i':i})
def prodactivate(request,pk):
	categories=Category.objects.filter(active='1')
	if request.method=='GET':
		uname=request.GET.get('uname')
	user=User_Detail.objects.filter(username=uname)
	i=''
	for j in user:
		i=j.id
	products=Product.objects.all()
	prod=Product.objects.get(id=pk)
	prod.active='1'
	prod.save()
	#return redirect('product')	
	return render(request,'product.html',{'products':products,'categories':categories,'uname':uname,'i':i})
	#return redirect(request,'product.html',{'userdetail':user,'products':product,'categories':categories,'i':i})
def proddeactivate(request,pk):
	categories=Category.objects.filter(active='1')
	if request.method=='GET':
		uname=request.GET.get('uname')
	user=User_Detail.objects.filter(username=uname)
	i=''
	for j in user:
		i=j.id
	products=Product.objects.all()
	#return redirect('product')	
	prod=Product.objects.get(id=pk)
	prod.active='0'
	prod.save()
	return render(request,'product.html',{'products':products,'categories':categories,'uname':uname,'i':i})
def cateactivate(request,pk):
	categorie=Category.objects.filter(active='1')
	if request.method=='GET':
		uname=request.GET.get('uname')
	user=User_Detail.objects.filter(username=uname)
	#i=user.id
	i=''
	for j in user:
		i=j.id
	categories=Category.objects.all()
	cate=Category.objects.get(id=pk)
	cate.active='1'
	cate.save()
	#return redirect('categories')	
	return render(request,'category.html',{'categories':categories,'categorie':categorie,'uname':uname,'i':i})
def catedeactivate(request,pk):
	categorie=Category.objects.filter(active='1')
	if request.method=='GET':
		uname=request.GET.get('uname')
	user=User_Detail.objects.filter(username=uname)
	#i=user.id
	i=''
	for j in user:
		i=j.id
	categories=Category.objects.all()
	cate=Category.objects.get(id=pk)
	cate.active='0'
	cate.save()
	#return redirect('categories')	
	return render(request,'category.html',{'categories':categories,'categorie':categorie,'uname':uname,'i':i})
	
def userdetails(request):
	#if request.method=='GET':
	global catdetails
	uname=request.GET['uname']
	if uname=='None':
		uname=''
	if uname:
		user=User_Detail.objects.filter(username=uname)
		categories=Category.objects.filter(active='1')
		if request.method=='POST' and request.FILES['image']:
			pname=request.POST['pname']
			pdescription=request.POST['pdesc']
			pcategory=request.POST['pcategory']
			pquantity=request.POST['pquantity']
			pprice=request.POST['pprice']
			image= request.FILES['image']
			fs = FileSystemStorage()
			filename = fs.save(image.name,image)
			uploaded_file_url = fs.url(filename)
			
			catalreadypresent=Category.objects.filter(categoryname=pcategory,active='1')
			if catalreadypresent.count()<=0:
				catdetails=Category.objects.create(
				categoryname=pcategory,
				active='1',)
			else:
				catdetails=Category.objects.get(categoryname=pcategory)
			user=User_Detail.objects.get(username=uname)
			user1=User_Detail.objects.filter(username=uname)
		#user=User.objects.first() #TODO:get the currently logged in user
			productalready=Product.objects.filter(pname=pname,user_detailid=user)
			if productalready.count()>0:
				productquanupdate=Product.objects.get(pname=pname,user_detailid=user)
				productquanupdate.pquantity=(productquanupdate.pquantity)+float(pquantity)
				oldprice=productquanupdate.pprice
				if float(pprice)>(oldprice):
					productquanupdate.pprice=pprice
				else:
					productquanupdate.pprice=oldprice
				productquanupdate.save()
			else:
				productdetails=Product.objects.create(
				pname=pname,
				pdescription=pdescription,
				pquantity=pquantity,
				pprice=pprice,
				pimg=image,
				pcategoryid=catdetails,
				user_detailid=user,
				active='1',
		)
			pro=Product.objects.all()
		
				
			return render(request,'home.html',{'uname':uname,'userdetails':user1,'categories':categories,'products':pro})
		return render(request,'userdetails.html',{'uname':uname,'userdetails':user,'categories':categories})
	else:
		return redirect('login')

def buynow(request):
	if request.method=='GET':
		pk=request.GET['cpk1']
		uname=request.GET.get('uname','')
	if uname=='None':
		uname=''
	if uname:
		categories=Category.objects.filter(active='1')
		userdetail=User_Detail.objects.filter(username=uname)
		buy_product=Product.objects.filter(id=pk,active='1')
		return render(request,'payNow.html',{'buy_product':buy_product,'userdetail':userdetail,'categories':categories,'uname':uname})
	else:
		return redirect('login')



def invoice(request):
	categories=Category.objects.filter(active='1')
	if request.method=='GET':
		ppk=request.GET['ppk']
		upk=request.GET['upk']
		cpk=request.GET['cpk']
		userdetails=User_Detail.objects.filter(id=upk)
		buy_product=Product.objects.filter(id=ppk,active='1')
	if request.method=='POST':
		ppk=request.GET['ppk']
		upk=request.GET['upk']
		cpk=request.GET['cpk']
		userdetails=User_Detail.objects.filter(id=upk)
		userdetail=User_Detail.objects.get(id=upk,active='1')
		buy_product=Product.objects.get(id=ppk,active='1')
		Quantity=int(request.POST.get('Quantity'))
		MAdress=request.POST.get('MAdress')
		purchase=Purchase.objects.create(
		pid=buy_product,
		purchaseprice=buy_product.pprice,
		tax=6.0,
		pquantity=Quantity,
		Tcost=(buy_product.pprice*Quantity*106)/100,
		purchaseuid=userdetail
		)
		invoice_detail=Purchase.objects.filter(purchaseuid=upk,pid=ppk,pquantity=Quantity)
		for inv in invoice_detail:
			uname=inv.purchaseuid.username
			name=inv.purchaseuid.name
			date=inv.purchase_date
			suname=inv.pid.user_detailid.username
			sname=inv.pid.user_detailid.name
			phone=inv.pid.user_detailid.phone
			pname=inv.pid.pname
			categoryname=inv.pid.pcategoryid.categoryname
			pquantity=inv.pquantity
			pprice=inv.pid.pprice
			tcost=inv.Tcost
		subjectk="Hi ! Your product has been sold."
		subject="Thank you ! For buying"
		sendtoList=Purchase.objects.filter(purchaseuid=upk,pid=ppk,pquantity=Quantity)
		from_email=settings.EMAIL_HOST_USER
		for i in sendtoList:
			j=i.purchaseuid.email
			k=i.pid.user_detailid.email
			q=i.pquantity
			rate=i.purchaseprice
			tc=i.Tcost
			pn=i.pid.pname
			ph=i.purchaseuid.phone
			phk=i.pid.user_detailid.phone
			cname=i.purchaseuid.name
			fname=i.pid.user_detailid.name
		#to_list=[j,settings.EMAIL_HOST_USER]
		text_content ='This is to inform you to that you bought the product:  '+ str(pn) +'  Qty: '+ str(q) +'  Rate: '+str(rate)+'	 Total : '+str(tc)+'  The product will be delivered by : '+str(fname)+'  Contact:'+str(phk)+'  to address: '+str(MAdress)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [j])
		msg.attach_alternative(text_content, "text/html")
		msg.send()
		#to_listk=[k,settings.EMAIL_HOST_USER]
		invoice_detail=Purchase.objects.filter(purchaseuid=upk,pid=ppk,pquantity=Quantity)
		#template = get_template('invoice.html')
		#context = Context({'invoice_detail':invoice_detail,'MAdress':MAdress,'category':cpk})
		#content =render_to_string('invoice.html',{'invoice_detail':invoice_detail,'MAdress':MAdress,'category':cpk})
		#send_mail(subject,content,from_email,to_list,fail_silently=True)
		#send_mail(subjectk,content,from_email,to_list,fail_silently=True)
		
		#text = "Subject: %s\n\n%s" % (email.subject, email.plain)
		text_contentk ='This is to inform you to that you have to deliver the product:  '+str(pn)+'  to address : '+ str(MAdress) +'  Customer Phone no. : '+str(ph)+'  Quantity : '+ str(q) +'  Totalcost: '+ str(tc)
		#html_content = '<p>This is to inform you to that you have to <strong>deliver</strong> product.</p>'
		msg = EmailMultiAlternatives(subjectk, text_contentk, from_email, [k])
		msg.attach_alternative(text_contentk, "text/html")
		msg.send()
		subjectH='Hello Host'
		text_contentH=' The email was sent to the Customer : '+str(cname)+' as well as the farmer: '+str(fname)+' successfully !'
		msg = EmailMultiAlternatives(subjectH, text_contentH, from_email, [from_email])
		msg.attach_alternative(text_contentH, "text/html")
		msg.send()
		return render(request,'invoice.html',{'userdetails':userdetails,'invoice_detail':invoice_detail,'uname':uname,'MAdress':MAdress,'category':cpk,'categories':categories,'name':name,'date':date,'suname':suname,'sname':sname,'phone':phone,'userdetails':userdetails,'pname':pname,'categoryname':categoryname,'pquantity':pquantity,'pprice':pprice,'tcost':tcost})
	#return render(request,'invoice.html',{'invoice_detail':invoice_detail,'MAdress':MAdress,'category':cpk,'categories':categories,'userdetails':userdetails})
	#return render(request,'invoice.html',{'invoice_detail':invoice_detail,'userdetail':userdetail,'buy_product':buy_product,'Quantity':Quantity,'MAdress':MAdress})
		#return render(request,'invoice.html',{'invoice_detail':invoice_detail,'MAdress':MAdress})
	#return render(request,'invoice.html',{'invoice_detail':invoice_detail,'MAdress':MAdress})
"""def search(request):
	q=request.GET.get('q')
	'''msg='Search not found'
	try:
		posts=''
		posts=Product.objects.filter(pname__search=q)
	except KeyError:
		return render(request,'search.html',{'msg':msg})'''
	results=Product.objects.filter(pname__icontains=q)
	return render(request,'search.html',{'posts':results})
# Create your views here."""
def search(request):
	q=''
	uname=''
	user=''
	if request.method=='POST':
		q=request.POST['q']
		uname=request.GET['uname']
	if uname=='None':
		uname=''
	if uname:
		user=User_Detail.objects.filter(username=uname)
		
	categories=Category.objects.filter(active='1')
	
	msg1=''
	l=[]

	'''
	try:
		posts=''
		posts=Product.objects.filter(pname__search=q)
	except KeyError:
		return render(request,'search.html',{'msg':msg})'''
	results=Product.objects.filter(pname__icontains=q)
	length=len(results)
	if results.count()==0:
		msg='Search not found'
		return render(request,'search.html',{'uname':uname,'userdetails':user,'posts':results,'l':l,'msg':msg})
	
	else:
		for i in results:
			msg1=''
			p=Product.objects.filter(pname=i)
			l.append(p)
		return render(request,'search.html',{'uname':uname,'userdetails':user,'posts':results,'l':l,'msg':msg1,'length':length,'categories':categories})
