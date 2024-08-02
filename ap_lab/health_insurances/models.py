from django.utils.translation import gettext_lazy as _
from django.db import models


class AuthorizerChoices(models.TextChoices):
    MANUAL = "MA", _("Manual")


# Create your models here.
class HealthInsurance(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_("Name"))
    code = models.CharField(max_length=100, unique=True, verbose_name=_("Code"))
    website = models.URLField(null=True, blank=True, verbose_name=_("Website"))
    authorizer = models.CharField(max_length=2, choices=AuthorizerChoices.choices, null=False, blank=False, verbose_name=_("Authorizer"))
    nbu_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name=_("NBU price"))

    def __str__(self):
        return f"{self.name} ({self.code})"
