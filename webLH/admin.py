from django.contrib import admin
from .models import *
from .forms import *


class UserAdmin(admin.ModelAdmin):
    form = UserForm

admin.site.register(Usuario, UserAdmin)
admin.site.register(Hermano)
admin.site.register(Grupo)
admin.site.register(Permiso)
admin.site.register(InfoPermiso)
