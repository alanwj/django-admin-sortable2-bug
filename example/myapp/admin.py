from adminsortable.admin import SortableInlineAdminMixin
from django.contrib import admin

from .models import Foo, Bar

class BarInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Bar
    extra = 0

class FooAdmin(admin.ModelAdmin):
    inlines = (BarInline,)

admin.site.register(Foo, FooAdmin)
