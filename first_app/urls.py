from django.urls import path, re_path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    # re_path(r'^$',views.index,name='index'),
    re_path(r'^index/',views.index,name='index'),
    re_path(r'^users/',views.users,name= 'users'),
    re_path(r'^forms/',views.form,name='forms'),
    re_path(r'^authoreg/',views.authoreg,name='authoreg'),
    re_path(r'^logout/', views.user_logout, name='logout'),
    re_path(r'^special/', views.special, name='special'),
    re_path(r'^user_login/',views.user_login, name = 'user_login')
]