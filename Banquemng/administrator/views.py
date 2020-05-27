from django.shortcuts import render

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
    
    return render(request,'admin/admin_add_users.html')

def viewproperties(request):
    return render(request,'admin/admin_view_delete_property.html')

def viewpropertiesd(request,property_id):
    return render(request,'admin/admin_viewd_property.html')
