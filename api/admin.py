from django.contrib import admin
from .models import User, CostCenter, License, LicenseColumn, UserAccountLog


admin.site.register(CostCenter)
admin.site.register(License)
admin.site.register(LicenseColumn)
admin.site.register(UserAccountLog)
