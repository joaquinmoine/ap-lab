from rest_framework import viewsets, filters

from reports.models import Report, ReportPraxis, Praxis, ReportMeasurement
from reports.serializers import ReportSerializer, ReportMeasurementSerializer, ReportPraxisSerializer, PraxisSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'id__icontains', 'patient__last_name__icontains', 'patient__first_name__icontains',
        'patient__identification_number__icontains'
    ]


class ReportPraxisViewSet(viewsets.ModelViewSet):
    queryset = ReportPraxis.objects.all()
    serializer_class = ReportPraxisSerializer

    def get_queryset(self):
        return self.queryset.filter(report_id=self.kwargs["report_id"])

    def perform_create(self, serializer):
        serializer.save(report_id=self.kwargs["report_id"])


class ReportMeasurementViewSet(viewsets.ModelViewSet):
    queryset = ReportMeasurement.objects.all()
    serializer_class = ReportMeasurementSerializer

    def get_queryset(self):
        return self.queryset.filter(report_id=self.kwargs["report_id"])

    def perform_create(self, serializer):
        serializer.save(report_id=self.kwargs["report_id"])


class PraxisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Praxis.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['code__icontains', 'name__icontains']
    serializer_class = PraxisSerializer
