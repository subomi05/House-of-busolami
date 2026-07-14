from django.shortcuts import render, redirect
from django.contrib import messages

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings

from .models import (
    Service,
    Gallery,
    Testimonial,
    BusinessInfo,
    Statistic,
)

from .forms import AppointmentForm


def home(request):

    services = Service.objects.filter(
        is_active=True
    )

    statistics = Statistic.objects.filter(
        is_active=True
    ).order_by("order")

    gallery = Gallery.objects.order_by(
        "-created_at"
    )

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

            # ==========================
            # EMAIL TO CLIENT
            # ==========================

            if appointment.email:

                client_html = render_to_string(
                    "emails/appointment_client.html",
                    context
                )

                client_email = EmailMultiAlternatives(
                    subject="Appointment Confirmation | House of Busolami",
                    body=strip_tags(client_html),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[appointment.email],
                )

                client_email.attach_alternative(
                    client_html,
                    "text/html",
                )

                print("EMAIL_HOST:", settings.EMAIL_HOST)
                print("EMAIL_PORT:", settings.EMAIL_PORT)
                print("EMAIL_USE_TLS:", settings.EMAIL_USE_TLS)
                print("EMAIL_HOST_USER:", settings.EMAIL_HOST_USER)
                print("DEFAULT_FROM_EMAIL:", settings.DEFAULT_FROM_EMAIL)

                try:
                    client_email.send()
                    print("Client email sent successfully.")
                except Exception as e:
                    print("Client email error:", repr(e))

            # ==========================
            # EMAIL TO BUSINESS
            # ==========================

            admin_html = render_to_string(
                "emails/appointment_admin.html",
                context
            )

            admin_email = EmailMultiAlternatives(
                subject="New Appointment Booking",
                body=strip_tags(admin_html),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[business.email],
            )

            admin_email.attach_alternative(
                admin_html,
                "text/html",
            )

            try:
                admin_email.send()
                print("Admin email sent successfully.")
            except Exception as e:
                print("Admin email error:", repr(e))

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

    return render(
        request,
        "home.html",
        context,
    )


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


def appointment_success(request):

    business = BusinessInfo.objects.first()

    context = {
        "business": business,
    }

    return render(
        request,
        "appointment_success.html",
        context,
    )