from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()  # ใช้ User Model ของ Django


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ตาราง Cost Center
class CostCenter(models.Model):
    costcenter_id = models.CharField(max_length=4, primary_key=True)  # รหัส Cost_id
    costcenter_desc = models.CharField(max_length=150)  # รายละเอียด
    division1 = models.CharField(max_length=255, null=True, blank=True)
    division2 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.costcenter_id} - {self.costcenter_desc}" 
 
# ตาราง User (ผู้ใช้)
class UserCostCenter(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ใช้ auth_user ที่มีอยู่
    costcenter = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.costcenter}"

# ตาราง License (สิทธิ์การใช้งาน)
class License(models.Model):
    license_id = models.AutoField(primary_key=True)
    license_name = models.CharField(max_length=255, unique=True)   

    def __str__(self):
        return self.license_name

# ตาราง License Column (รายละเอียด License)
class LicenseColumn(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    table_column = models.CharField(max_length=50)
    table_column_display = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.license.license_name} - {self.table_column_display}"

# ตารางบันทึกบัญชีที่สร้างใหม่
class UserAccountLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # เช่น "Created", "Updated"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"
 