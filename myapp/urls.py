from django.urls import path
from . import views
urlpatterns = [
path('',views.user_list),
    path('Add/',views.adduser),
    path('Edit/<id>',views.Edituser),
    path('Delete/<eid>',views.Deleteuser),
    path('View/<eid>',views.Viewuser)


]