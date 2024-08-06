from rest_framework import viewsets, filters

from health_insurances.models import HealthInsurance
from health_insurances.serializers import HealthInsuranceSerializer


class HealthInsuranceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HealthInsurance.objects.all()
    serializer_class = HealthInsuranceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code__icontains', 'name__icontains']
