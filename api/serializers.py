from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Item, CostCenter ,License , LicenseColumn , UserAccountLog ,  UserCostCenter

User = get_user_model()

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CostCenterSerializer(serializers.ModelSerializer):  # ✅ แก้ชื่อคลาส
    class Meta:
        model = CostCenter
        fields = '__all__'

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'       

class LicenseColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseColumn
        fields = '__all__' 

class UserAccountLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccountLog
        fields = '__all__'          

class  UserCostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  UserCostCenter
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    costcenter = serializers.CharField(source='usercostcenter.costcenter.costcenter_desc', read_only=True)
    costcenter_id = serializers.CharField(source='usercostcenter.costcenter.costcenter_id', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'costcenter_id', 'costcenter']                           


       