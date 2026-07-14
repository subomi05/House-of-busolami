from .models import BusinessInfo


def business_info(request):
    return {
        "business": BusinessInfo.objects.first()
    }