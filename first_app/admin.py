from django.contrib import admin
from first_app.models import Topic,AccessRecord,Webpage,Userr, UserProfileInfo
# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Userr)
admin.site.register(UserProfileInfo)