from django.shortcuts import render, redirect
from django.contrib import messages

from .models import (
    Service,
    Gallery,
    Testimonial,
    BusinessInfo,
    Statistic,
)

from .forms import AppointmentForm


def home(request):

    services = (
        Service.objects
        .filter(is_active=True)
    )

    statistics = (
        Statistic.objects
        .filter(is_active=True)
        .order_by("id")
    )

    gallery = (
        Gallery.objects
        .order_by("-created_at")
    )

    testimonials = (
        Testimonial.objects
        .filter(is_active=True)
    )

    business = (
        BusinessInfo.objects
        .only(
            "business_name",
            "logo",
            "hero_image",
            "phone",
            "whatsapp",
            "email",
            "address",
            "instagram",
            "facebook",
            "tiktok",
        )
        .first()
    )

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "🎉 Your appointment request has been submitted successfully! We will contact you shortly."
            )

            return redirect("home")

    else:

        form = AppointmentForm()

    context = {
        "services": services,
        "gallery": gallery,
        "testimonials": testimonials,
        "statistics": statistics,
        "business": business,
        "form": form,
    }

    return render(request, "home.html", context)


def gallery_page(request):

    gallery = (
        Gallery.objects
        .order_by("-created_at")
    )

    business = (
        BusinessInfo.objects
        .only(
            "business_name",
            "logo",
            "phone",
            "whatsapp",
            "email",
            "address",
            "instagram",
            "facebook",
            "tiktok",
        )
        .first()
    )

    context = {
        "gallery": gallery,
        "gallery_categories": Gallery.CATEGORY_CHOICES,
        "business": business,
    }

    return render(request, "gallery.html", context)


