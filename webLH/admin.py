from django.contrib import admin

from .forms import *
from .models import *


class UserAdmin(admin.ModelAdmin):
    form = UserForm

admin.site.register(Usuario, UserAdmin)
admin.site.register(Hermano)
admin.site.register(Grupo)
admin.site.register(Permiso)
admin.site.register(InfoPermiso)
admin.site.register(Actividade)
admin.site.register(Photo)
