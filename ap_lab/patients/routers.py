from rest_framework import routers

from patients.views import PatientViewSet

router = routers.DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')
