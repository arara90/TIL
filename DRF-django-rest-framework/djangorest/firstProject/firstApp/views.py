from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
# Create your views here.


def employeeView(request):
    # emp = {
    #     'id': 123,
    #     'name': 'John',
    #     'sal': 10000
    # }

    data = Employee.objects.all()
    response = {'employee': list(data.values('name', 'sal'))}
    #
    # {"employee": [
    # {"name": "ara", "sal": "100000.000"},
    # {"name": "ara2", "sal": "100000.000"}
    # ]}
    #

    return JsonResponse(response)  # dictionary를 json형태로
