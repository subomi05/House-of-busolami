from django.shortcuts import render, redirect

from django.template.loader import render_to_string
from django.conf import settings

from .models import (
    Service,
    Gallery,
    Testimonial,
    BusinessInfo,
    Statistic,
)

from .forms import AppointmentForm

import requests


def send_brevo_email(to_email, to_name, subject, html_content):
    """
    Send an email using Brevo API
    """

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json",
    }

    payload = {
        "sender": {
            "name": "House of Busolami",
            "email": settings.DEFAULT_FROM_EMAIL,
        },
        "to": [
            {
                "email": to_email,
                "name": to_name,
            }
        ],
        "subject": subject,
        "htmlContent": html_content,
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30,
    )

    print("Brevo Status:", response.status_code)
    print("Brevo Response:", response.text)

    response.raise_for_status()


def home(request):

    services = Service.objects.filter(is_active=True)

    statistics = Statistic.objects.filter(
        is_active=True
    ).order_by("order")

    gallery = Gallery.objects.order_by("-created_at")

    testimonials = Testimonial.objects.filter(
        is_active=True
    )

    business = BusinessInfo.objects.first()

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save()

            website_url = request.build_absolute_uri("/")

            context = {
                "appointment": appointment,
                "business": business,
                "website_url": website_url,
            }

            # ===========================
            # CLIENT EMAIL
            # ===========================

            if appointment.email:

                client_html = render_to_string(
                    "emails/appointment_client.html",
                    context,
                )

                try:
                    send_brevo_email(
                        to_email=appointment.email,
                        to_name=appointment.full_name,
                        subject="Appointment Confirmation | House of Busolami",
                        html_content=client_html,
                    )
                except Exception as e:
                    print("CLIENT EMAIL ERROR:", e)

            # ===========================
            # BUSINESS EMAIL
            # ===========================

            if business and business.email:

                admin_html = render_to_string(
                    "emails/appointment_admin.html",
                    context,
                )

                try:
                    send_brevo_email(
                        to_email=business.email,
                        to_name=business.business_name,
                        subject="New Appointment Booking",
                        html_content=admin_html,
                    )
                except Exception as e:
                    print("ADMIN EMAIL ERROR:", e)

            return redirect("appointment_success")

    else:

        form = AppointmentForm()

    context = {
        "services": services,
        "statistics": statistics,
        "gallery": gallery,
        "testimonials": testimonials,
        "business": business,
        "form": form,
    }

    return render(request, "home.html", context)


def gallery_page(request):

    gallery = Gallery.objects.order_by("-created_at")

    business = (
        BusinessInfo.objects.only(
            "business_name",
            "logo",
            "phone",
            "whatsapp",
            "email",
            "address",
            "instagram",
            "facebook",
            "tiktok",
        ).first()
    )

    context = {
        "gallery": gallery,
        "gallery_categories": Gallery.CATEGORY_CHOICES,
        "business": business,
    }

    return render(request, "gallery.html", context)


def appointment_success(request):

    business = BusinessInfo.objects.first()

    return render(
        request,
        "appointment_success.html",
        {
            "business": business,
        },
    )