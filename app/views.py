from django.http import JsonResponse


def fire_extinguishers(request):
    if request.method == 'GET':
        data = {}
        return JsonResponse(data=data)
