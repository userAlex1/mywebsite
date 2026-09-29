
from django.contrib import admin
from django.urls import path
from home import views



# django admin changes
admin.site.site_header = "Login to Alex"
admin.site.site_title = "Welocom to DashBord"
admin.site.index_title = "Welocom to Portal"



urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.project_index, name='project_index'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),
    path("journey/university/", views.journey_university, name="journey_university"),
    path("journey/python/", views.journey_python, name="journey_python"),
    path("journey/django/", views.journey_django, name="journey_django"),
    path("journey/projects/", views.journey_projects, name="journey_projects"),
    
]
