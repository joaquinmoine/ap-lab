from rest_framework import serializers

from reports.models import Report, ReportPraxis, ReportMeasurement, Praxis


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class ReportPraxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportPraxis
        fields = '__all__'


class ReportMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportMeasurement
        fields = '__all__'


class PraxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Praxis
        fields = '__all__'
