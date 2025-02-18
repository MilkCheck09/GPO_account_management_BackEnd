from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, CostCenterViewSet,LicenseViewSet , LicenseColumnViewSet , UserAccountLogViewSet, UserCostCenterViewSet , UserViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'costcenter', CostCenterViewSet)
router.register(r'License', LicenseViewSet)
router.register(r'LicenseColumn', LicenseColumnViewSet)
router.register(r'UserAccountLog', UserAccountLogViewSet)
router.register(r'UserCostCenter', UserCostCenterViewSet)
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]