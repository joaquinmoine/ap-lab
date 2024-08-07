from knox.auth import TokenAuthentication
from rest_framework import viewsets, filters, permissions

from health_insurances.models import HealthInsurance
from health_insurances.serializers import HealthInsuranceSerializer


class HealthInsuranceViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = HealthInsurance.objects.all()
    serializer_class = HealthInsuranceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code__icontains', 'name__icontains']
