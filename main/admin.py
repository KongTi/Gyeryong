from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Account
from .forms import UserCreateForm, UserChangeForm

class AccountAdmin(BaseUserAdmin):
    add_form = UserCreateForm
    form = UserChangeForm

    # 관리자 화면에 보여질 칼럼 지정
    list_display = ('email','nickname', 'phone_num','update_at','is_admin', 'is_active')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields':('email','nickname','phone_num')}),
        ('암호화', {'fields': ('password',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'phone_num', 'password1', 'password2')}
         ),
    )

    search_fields = ('email', 'nickname')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)