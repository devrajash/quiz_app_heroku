
from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views


admin.site.site_header='Quiz App Admin Page'
admin.site.site_title='Quiz App Admin Page'
admin.site.index_title='Quiz App Admin Page'

urlpatterns = [
    path('quiz_admin/', admin.site.urls),
    path('quiz/', views.home, name='home'),
    path('login_n/', auth_views.LogoutView.as_view(template_name='login_m.html'), name='login_m'),
    path('logout_n/', auth_views.LogoutView.as_view(template_name='logout_m.html'), name='logout_m'),
    path('', include('quiz_login.urls')),

]
