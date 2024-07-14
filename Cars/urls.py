from django.urls import path
from .views import car_list,car_specific


urlpatterns = [
    path('functionbased/',car_list,name="Listall"),
    path('functionbased/<int:pk>',car_specific,name="Listone")
]


