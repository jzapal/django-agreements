from django.contrib import admin
from .models import Agreement, AgreementToUser


class AgreementToUserAdmin(admin.ModelAdmin):
    fields = ('user', 'agreement', 'datetime')
    readonly_fields = ('datetime',)


admin.site.register(Agreement)
admin.site.register(AgreementToUser, AgreementToUserAdmin)
