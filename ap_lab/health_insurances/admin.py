from django.contrib import admin
from health_insurances.models import HealthInsurance


class HealthInsuranceAdmin(admin.ModelAdmin):
    pass


admin.site.register(HealthInsurance, HealthInsuranceAdmin)
