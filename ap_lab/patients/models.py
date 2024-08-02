from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class Gender(models.TextChoices):
    MALE = "MA", _("Male")
    FEMALE = "FE", _("Female")
    UNKNOWN = "UN", _("Unknown")


class Patient(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("Last Name"))
    identification_number = models.CharField(max_length=20, unique=True, verbose_name=_("Identification Number"))
    date_of_birth = models.DateField(null=False, blank=False, verbose_name=_("Date of Birth"))
    gender = models.CharField(null=False, blank=False, default=Gender.UNKNOWN, max_length=2, choices=Gender.choices, verbose_name=_("Gender"))
    address = models.CharField(max_length=100, verbose_name=_("Address"))
    phone_number = PhoneNumberField(blank=False, null=False, verbose_name=_("Phone Number"))
    has_whatsapp = models.BooleanField(default=False, verbose_name=_("Has Whatsapp?"))
    whatsapp_notification = models.BooleanField(default=False, verbose_name=_("Whatsapp Notification?"))
    email = models.EmailField(verbose_name=_("Email"))
    email_notification = models.BooleanField(default=False, verbose_name=_("Email Notification?"))
    health_insurances = models.ManyToManyField("health_insurances.HealthInsurance", through="patients.Membership", verbose_name=_("Health Insurances"), related_name="patients")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.identification_number})"


class Membership(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, verbose_name=_("Patient"), related_name="memberships")
    health_insurance = models.ForeignKey("health_insurances.HealthInsurance", on_delete=models.CASCADE, verbose_name=_("Patient"), related_name="memberships")
    identification = models.CharField(max_length=50, verbose_name=_("Identification"), null=True, blank=True)
    plan = models.CharField(max_length=50, verbose_name=_("Plan"), null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name=_("Active"))

    def __str__(self):
        return f"{self.identification or self.patient} - {self.health_insurance}"
