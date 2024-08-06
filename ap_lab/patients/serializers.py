from rest_framework import serializers

from health_insurances.serializers import HealthInsuranceSerializer
from patients.models import Patient, Membership, Gender


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"


class MembershipReadOnlySerializer(serializers.ModelSerializer):
    health_insurance = HealthInsuranceSerializer(read_only=True)

    class Meta:
        model = Membership
        fields = ["id", "health_insurance", "identification", "plan", "active"]


class PatientSerializer(serializers.ModelSerializer):
    memberships = MembershipReadOnlySerializer(many=True, read_only=True)
    gender_choices = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ["memberships", "gender_choices"]

    def get_gender_choices(self, obj):
        return {k: v for k, v in Gender.choices}
