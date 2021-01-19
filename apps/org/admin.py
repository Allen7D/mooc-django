from django.contrib import admin

from apps.org.models import City as CityModel, Org as OrgModel, Teacher as TeacherModel


class CityAdmin(admin.ModelAdmin):
    pass


class OrgAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(CityModel, CityAdmin)
admin.site.register(OrgModel, OrgAdmin)
admin.site.register(TeacherModel, TeacherAdmin)
