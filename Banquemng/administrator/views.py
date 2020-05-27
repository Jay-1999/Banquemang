from django.shortcuts import render, redirect
from administrator.models import Admin
from users.models import User, City
from property.models import Property, Property_Category
from django.contrib import messages

# Create your views here.
def adminlogin(request):
    print("shgshghsghg")
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        result = Admin.objects.filter(admin_email_id = email,admin_password=password).exists()
        if result:
            messages.success(request,'Login successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return render(request, 'admin/admin_login.html')
    else:
        return render(request, 'admin/admin_login.html')

def dashboard(request):
    custcount = User.objects.filter(user_type='Customer').count()
    ownercount = User.objects.filter(user_type='Owner').count()
    ppcount = Property.objects.filter(property_category_id=Property_Category.objects.get(property_category_name='Party Plot')).count()
    bcount = Property.objects.filter(property_category_id=Property_Category.objects.get(property_category_name='Banquet')).count()
    return render(request,'admin/admin_dashboard.html',{ 'custcount':custcount,'ownercount':ownercount,'ppcount':ppcount,'bcount':bcount})

def viewusers(request):
    userdata = User.objects.all()
    return render(request,'admin/admin_add_view_delete_users.html',{'userdata':userdata})
    

def viewusersd(request,user_id):
    userinfo = User.objects.get(user_id=user_id)
    return render(request,'admin/admin_viewd_user.html',{'userinfo':userinfo})


def adduser(request):
    if request.method == 'POST':
        user_type=request.POST['user_type']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        city=int(request.POST['city'])
        pincode=request.POST['pincode']
        email=request.POST['email']
        mobileno=request.POST['mobileno']
        password=request.POST['password']

        city_instance = City.objects.get(city_id=int(city))
        u1 = None
        if user_type == 'Owner':
            idproof=request.FILES['idproof']
            u1=User(user_type=user_type,first_name=firstname,last_name=lastname,email_id=email,mobile_no=mobileno,address=address, city_id=city_instance,pincode=pincode, id_proof_doc_path=idproof,password=password)

        else:
            u1 = User.objects.create(user_type=user_type, first_name=firstname, last_name=lastname, email_id=email, mobile_no=mobileno,
                      address=address, city_id=city_instance, pincode=pincode, password=password)

        u1.save()
        messages.success(request,'New user added successfully')
        return redirect('viewusers')
    cities = City.objects.all()
    return render(request,'admin/admin_add_users.html',{'City':cities})

def viewproperties(request):
    propertydata = Property.objects.all()
    return render(request,'admin/admin_view_delete_property.html',{'propertydata':propertydata})

def viewpropertiesd(request,property_id):
    propertyinfo = Property.objects.filter(property_id=property_id)
    return render(request,'admin/admin_viewd_property.html',{'propertyinfo':propertyinfo})
