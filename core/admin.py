from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Service,
    Gallery,
    Testimonial,
    Appointment,
    BusinessInfo,
    Statistic,
)


# ==========================
# SERVICE ADMIN
# ==========================

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "image_preview",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "is_active",
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px; object-fit:cover;">',
                obj.image.url
            )
        return "-"

    image_preview.short_description = "Image"


# ==========================
# GALLERY ADMIN
# ==========================

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "title",
        "category",
        "featured",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
    )

    search_fields = (
        "title",
    )

    list_editable = (
        "featured",
    )

    ordering = (
        "-created_at",
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="70" height="70" style="border-radius:8px; object-fit:cover;">',
                obj.image.url
            )
        return "-"

    image_preview.short_description = "Preview"


# ==========================
# TESTIMONIAL ADMIN
# ==========================

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "client_name",
        "profession",
        "rating",
        "is_active",
    )

    list_filter = (
        "rating",
        "is_active",
    )

    search_fields = (
        "client_name",
        "profession",
        "message",
    )

    list_editable = (
        "is_active",
    )


# ==========================
# APPOINTMENT ADMIN
# ==========================

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "phone",
        "service",
        "preferred_date",
        "status",
    )

    list_filter = (
        "status",
        "service",
        "preferred_date",
    )

    search_fields = (
        "full_name",
        "phone",
        "email",
    )

    list_editable = (
        "status",
    )

    ordering = (
        "-created_at",
    )


# ==========================
# BUSINESS INFO ADMIN
# ==========================

@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):

    list_display = (
        "business_name",
        "phone",
        "email",
        "image_preview",
    )

    search_fields = (
        "business_name",
        "phone",
        "email",
    )

    def image_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:50%; object-fit:cover;">',
                obj.logo.url
            )
        return "-"

    image_preview.short_description = "Logo"


admin.site.register(Statistic)



# ==========================
# CUSTOM ADMIN BRANDING
# ==========================

admin.site.site_header = "House of Busolami Administration"

admin.site.site_title = "House of Busolami Admin"

admin.site.index_title = "Welcome to the House of Busolami Dashboard"

