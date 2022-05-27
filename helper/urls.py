from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('add_tender', views.add_tender, name='add_tender'),
    path('edit_tender/<int:id>', views.edit_tender, name='edit_tender'),
    path('my_tenders', views.my_tenders, name='my_tenders'),
    path('tenders', views.tenders, name='tenders'),
    path('apply_to_tender/<int:tender_id>', views.apply_to_tender, name='apply_to_tender'),
    path('applied_to_tender/<int:tender_id>', views.applied_to_tender, name='applied_to_tender'),
    path('give_tender/<int:tender_id>/<int:id>', views.give_tender, name='give_tender'),
    path('companies', views.companies, name='companies'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
