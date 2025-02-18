from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from .models import Item, CostCenter ,License , LicenseColumn , UserAccountLog ,  UserCostCenter
from .serializers import ItemSerializer, CostCenterSerializer,LicenseSerializer ,LicenseColumnSerializer , UserAccountLogSerializer , UserCostCenterSerializer,UserSerializer

User = get_user_model()

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CostCenterViewSet(viewsets.ModelViewSet):
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterSerializer

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer  

class LicenseColumnViewSet(viewsets.ModelViewSet):
    queryset = LicenseColumn.objects.all()
    serializer_class = LicenseColumnSerializer      

class UserAccountLogViewSet(viewsets.ModelViewSet):
    queryset = UserAccountLog.objects.all()
    serializer_class = UserAccountLogSerializer        

class  UserCostCenterViewSet(viewsets.ModelViewSet):
    queryset =  UserCostCenter.objects.all()
    serializer_class =  UserCostCenterSerializer  

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




   