from django.contrib import admin
from patients.models import Patient, Membership


class MembershipAdmin(admin.TabularInline):
    model = Membership


class PatientAdmin(admin.ModelAdmin):
    inlines = [MembershipAdmin]


admin.site.register(Patient, PatientAdmin)
