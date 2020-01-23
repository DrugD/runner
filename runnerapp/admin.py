from django.contrib import admin
from .models import User,Plan,JoinPlan,Table_1,Table_2,Table_3,Table_4
# Register your models here.
admin.site.register(User)
admin.site.register(JoinPlan)
admin.site.register(Plan)
admin.site.register(Table_1)
admin.site.register(Table_2)
admin.site.register(Table_3)
admin.site.register(Table_4)
