import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class ReportStatus(models.TextChoices):
    DRAFT = "DR", _('Draft')
    CREATED = "CR", _('Created')
    VERIFIED = "VE", _('Verified')


class ReportPraxisStatus(models.TextChoices):
    PENDING = "PE", _('Pending')
    REJECTED = "R", _('Rejected')
    APPROVED = "A", _('Approved')
    AUDIT_PENDING = "AP", _('Audit Pending')
    AUDIT_APPROVED = "AA", _('Audit Approved')
    AUDIT_REJECTED = "AR", _('Audit Rejected')
    PARTICULAR = "PA", _('Particular')


class Report(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    praxis = models.ManyToManyField("reports.Praxis", through="reports.ReportPraxis", related_name="reports", blank=True)
    measurements = models.ManyToManyField("reports.Measurement", through="reports.ReportMeasurement", related_name="reports", blank=True)
    patient = models.ForeignKey("patients.Patient", on_delete=models.PROTECT, related_name="reports")
    delivery_datetime = models.DateTimeField(_("Delivery Datetime"), blank=True, null=True)
    health_insurances = models.ForeignKey("health_insurances.HealthInsurance", on_delete=models.PROTECT, related_name="reports", blank=True, null=True)
    coinsurance_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Coinsurance price"))
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Deposit"))
    receipt = models.FileField(_("Receipt"), upload_to="receipts", null=True, blank=True)
    order = models.FileField(_("Order"), upload_to="orders", null=True, blank=True)
    status = models.CharField(choices=ReportStatus.choices, default=ReportStatus.DRAFT, max_length=2)

    def __str__(self):
        return f'{self.patient} - {str(self.id)}'


class ReportPraxis(TimeStampedModel):
    report = models.ForeignKey("reports.Report", on_delete=models.PROTECT)
    praxis = models.ForeignKey("reports.Praxis", on_delete=models.PROTECT)
    status = models.CharField(choices=ReportPraxisStatus.choices, default=ReportPraxisStatus.PENDING, max_length=2)


class ReportMeasurement(TimeStampedModel):
    report = models.ForeignKey("reports.Report", on_delete=models.PROTECT)
    measurements = models.ForeignKey("reports.Measurement", on_delete=models.PROTECT)
    result = models.CharField(max_length=255, verbose_name=_("Result"), blank=True, null=True)


class Measurement(TimeStampedModel):
    code = models.CharField(max_length=10, unique=True, verbose_name=_("Code"))
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    short_name = models.CharField(max_length=40, verbose_name=_("Short Name"))
    ub = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("UB"))
    reference_value = models.CharField(max_length=50, verbose_name=_("Reference Value"))

    def __str__(self):
        return f"{self.code} - {self.name}"


class Praxis(TimeStampedModel):
    code = models.CharField(max_length=10, unique=True, verbose_name=_("Code"))
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    standard = models.TextField(blank=True, verbose_name=_("Standard"))
    render = models.TextField(blank=True, verbose_name=_("Render"))
    measurements = models.ManyToManyField(Measurement, blank=True, verbose_name=_("Measurements"))

    def __str__(self):
        return f"{self.code} - {self.name}"
