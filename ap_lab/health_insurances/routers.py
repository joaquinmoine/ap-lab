from rest_framework import routers

from health_insurances.views import HealthInsuranceViewSet

router = routers.DefaultRouter()
router.register("health-insurances", HealthInsuranceViewSet, basename="health-insurances")
