from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    icon = models.CharField(
        max_length=50,
        help_text="Bootstrap Icon name (e.g. scissors, gem, handbag)"
    )

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Gallery(models.Model):

    CATEGORY_CHOICES = [
        ("clothes", "Clothes"),
        ("beads", "Bead Accessories"),
        ("bead_bags", "Bead Bags"),
        ("fascinators", "Fascinators"),
        ("tailoring_materials", "Tailoring Materials"),
        ("bridal", "Bridal Outfits"),
        ("traditional", "Traditional Wear"),
        ("ready_to_wear", "Ready-to-Wear"),
    ]

    title = models.CharField(max_length=100)

    image = models.ImageField(upload_to="gallery/")

    category = models.CharField(
        max_length=25,
        choices=CATEGORY_CHOICES,
        db_index=True,
    )

    featured = models.BooleanField(default=False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.title


class Testimonial(models.Model):

    client_name = models.CharField(max_length=100)

    profession = models.CharField(max_length=100, blank=True)

    message = models.TextField()

    image = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    rating = models.PositiveSmallIntegerField(default=5)

    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.client_name


class Appointment(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField(blank=True)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    preferred_date = models.DateField(db_index=True)

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        db_index=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.service.title}"


class BusinessInfo(models.Model):

    business_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    whatsapp = models.CharField(max_length=20)

    email = models.EmailField()

    address = models.TextField()

    instagram = models.URLField(blank=True)

    facebook = models.URLField(blank=True)

    tiktok = models.URLField(blank=True)

    logo = models.ImageField(upload_to="business/")

    hero_image = models.ImageField(upload_to="business/")

    class Meta:
        verbose_name = "Business Information"
        verbose_name_plural = "Business Information"

    def __str__(self):
        return self.business_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Statistic(models.Model):

    title = models.CharField(max_length=100)

    value = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True, db_index=True)

    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Bootstrap icon name (optional)"
    )

    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title