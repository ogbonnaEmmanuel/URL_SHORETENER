from django.urls import path

from ProfilePage import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('user_links_info/', views.get_all_user_data, name='link_info'),
    path('settings/', views.settings, name='settings')
]
