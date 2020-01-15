from django.urls import path
from django.views.generic import TemplateView
from . import views

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/
# https://github.com/BlackrockDigital/startbootstrap-bare/blob/master/index.html
urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('starter/', TemplateView.as_view(template_name="starter.html")),
    path('add/', views.add, name='add'),
    path('', views.index, name='index'),
]