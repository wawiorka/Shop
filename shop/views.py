from django.http import JsonResponse


def ping(request):
    return  JsonResponse({
        "message" : "Представляю вам Json-формат электронного магазина"
    })