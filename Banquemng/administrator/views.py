from django.shortcuts import render, redirect
from administrator.models import Admin
from users.models import User
from property.models import Property,Property_Category
from django.contrib import messages

# Create your views here.
def adminlogin(request):
    print("shgshghsghg")
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        result = Admin.objects.filter(admin_email_id = email,admin_password=password).exists()
        if result:
            return redirect('dashboard')
        else:
            messages.info(request,'Invalid credentials')
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
    userinfo = User.objects.filter(user_id=user_id)
    return render(request,'admin/admin_viewd_user.html',{'userinfo':userinfo})

def adduser(request):
    return render(request,'admin/admin_add_users.html')

def viewproperties(request):
    propertydata = Property.objects.all()
    return render(request,'admin/admin_view_delete_property.html',{'propertydata':propertydata})

def viewpropertiesd(request,property_id):
    propertyinfo = Property.objects.filter(property_id=property_id)
    return render(request,'admin/admin_viewd_property.html',{'propertyinfo':propertyinfo})
