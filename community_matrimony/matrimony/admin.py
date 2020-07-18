from django.contrib import admin
from .models import Appuser,groom_bride_details,Kula_osa,States,District
# Register your models here.
admin.site.register(Appuser)
admin.site.register(groom_bride_details)
admin.site.register(Kula_osa)
admin.site.register(States)
admin.site.register(District)