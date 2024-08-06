from rest_framework import serializers

from health_insurances.models import HealthInsurance


class HealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsurance
        fields = "__all__"
