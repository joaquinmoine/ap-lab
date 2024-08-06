from rest_framework import routers

from reports.views import ReportViewSet, ReportPraxisViewSet, ReportMeasurementViewSet, PraxisViewSet

router = routers.DefaultRouter()
router.register("reports", ReportViewSet, basename="reports")
router.register("praxis", PraxisViewSet, basename="praxis")
router.register(
    "reports/(?P<report_id>[^/.]+)/praxis",
    ReportPraxisViewSet,
    basename="report-praxis",
)
router.register(
    "reports/(?P<report_id>[^/.]+)/measurements",
    ReportMeasurementViewSet,
    basename="report-measurement",
)
