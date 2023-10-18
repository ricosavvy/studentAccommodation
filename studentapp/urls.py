from django.urls import path
from . import views

urlspatterns = [
    path('', views.home, name='home'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('my_accommodation/', views.my_accommodation, name='my_accommodation'),
    path('my_application/', views.my_application, name='my_application'),
    path('notifications/', views.notifications, name='notifications'),
    path('stu_profile/', views.stu_profile, name='stu_profile'),
    path('logout/', views.logout, name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage_rooms/', views.manage_rooms, name='manage_rooms'),
    path('manage_students/', views.manage_students, name='manage_students'),
    path('manage_applications/', views.manage_applications, name='manage_applications'),
    path('manage_accommodation/', views.manage_accommodation, name='manage_accommodation'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('create_room/', views.create_room, name='create_room'),
    path('edit_room/<int:room_id>/', views.edit_room, name='edit_room'),
    path('delete_room/<int:room_id>/', views.delete_room, name='delete_room'),
]