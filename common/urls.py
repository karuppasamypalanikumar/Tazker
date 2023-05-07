from django.urls import path
from . import views

urlpatterns=[
    path(
        route='',
        view=views.index_page,
        name='index'
    ),
    path(
        route='health_check/',
        view=views.health_check,
        name='health_check'
    )    
]