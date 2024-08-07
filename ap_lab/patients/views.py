from knox.auth import TokenAuthentication
from rest_framework import filters, viewsets, permissions

from patients.models import Patient, Membership
from patients.serializers import PatientSerializer, MembershipSerializer


class PatientViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name__icontains', 'last_name__icontains', 'identification_number__icontains']


class MembershipViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer()
