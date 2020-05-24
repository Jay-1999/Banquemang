from django.shortcuts import render,redirect
from users.models import User , City

# Create your views here.
def adminlogin(request):
    return render(request,'admin/admin_login.html')

def dashboard(request):
    return render(request,'admin/admin_dashboard.html')

def viewusers(request):
    return render(request,'admin/admin_add_view_delete_users.html')

def viewusersd(request,user_id):
    return render(request,'admin/admin_viewd_user.html')    

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

        return redirect('viewusers')
    cities = City.objects.all()
    return render(request,'admin/admin_add_users.html',{'City':cities})

def viewproperties(request):
    return render(request,'admin/admin_view_delete_property.html')

def viewpropertiesd(request,property_id):
    return render(request,'admin/admin_viewd_property.html')
