from django.contrib import admin
from .models import *
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm

User = get_user_model()


class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None,{'fields':('reg_no','password')}),
        ('Personal info',{'fields':('first_name', 'second_name','username')}),
        ('Permissions',{'fields':('active','admin','staff','groups','user_permissions')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('reg_no',)}),
        ('Personal info', {'fields': ('first_name', 'second_name','username','phone_no')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','second_name','username','phone_no','gender','password', 'password_confirm')}
         ),
    )
    model = User
    add_form = UserCreationForm
    list_display = ['first_name','second_name','reg_no']
    list_filter = ['groups']
    search_fields = ['first_name','second_name','reg_no']
    ordering = ['reg_no']


admin.site.register(User,UserAdmin)
admin.site.register(Unit)
admin.site.register(Booking)
admin.site.site_header="Result Management Administration"
