from django.contrib import admin
from reports.models import Report, ReportPraxis, ReportMeasurement, Praxis, Measurement


class ReportPraxisAdmin(admin.TabularInline):
    model = ReportPraxis


class ReportMeasurementAdmin(admin.TabularInline):
    model = ReportMeasurement


class ReportAdmin(admin.ModelAdmin):
    inlines = [ReportPraxisAdmin, ReportMeasurementAdmin]


class PraxisAdmin(admin.ModelAdmin):
    pass


class MeasurementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Report, ReportAdmin)
admin.site.register(Praxis, PraxisAdmin)
admin.site.register(Measurement, MeasurementAdmin)
