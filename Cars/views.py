from django.http import JsonResponse
from django.http import request
from .models import Showroom

# Function based Views without any serializers
def car_list(request):
    cars = Showroom.objects.all()
    # manually using dictionary and serializing the code

    data = {

        'cars': list(cars.values())
    }
    return JsonResponse(data)

def car_specific(request,pk):
    car = Showroom.objects.get(pk=pk)
    data = {
        'shopname':car.shopname ,
        'loction':car.loction,
        'zipcode':car.zipcode
    }
    return JsonResponse(data)

