from django.urls import path

from . import views


urlpatterns = [
      path('adminlogin/',views.adminlogin,name='adminlogin'),
      path('dashboard/',views.dashboard,name='dashboard'),
      path('mngusers/viewusers/',views.viewusers,name='viewusers'),
      path('mngusers/viewusers/<int:user_id>',views.viewusersd,name='viewusersd'),
      path('mngusers/adduser',views.adduser,name='adduser'),
      path('mngproperties/viewproperties/',views.viewproperties,name='viewproperties'),
      path('mngproperties/viewproperties/<int:property_id>',views.viewpropertiesd,name='viewpropertiesd'),


]