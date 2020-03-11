from typing import Set

from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from .models import Customer, Product, Seller

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    readonly_fields = ['edit_product']

    def edit_product(self, obj=None):
        try:
            if obj and obj.pk:
                url = reverse('admin:%s_%s_change' %(obj._meta.app_label, 'product'), args=[force_text(obj.pk)])
                return mark_safe("""<a target="_blank" href="{url}">{text}</a>""".format(
					url=url,
					text=_("Edit details of this %s separately") % obj._meta.verbose_name,
				))
            return _("(After adding details click on \'save and continue editing\')")
        except Exception as e:
            print(e)

    edit_product.short_description = _("Edit product information")

class CustomerInline(admin.StackedInline):
    model = Customer
    extra = 1
    list_display = ['name', 'phone_number']

class SellerAdmin(admin.ModelAdmin):
    inlines = [ProductInline, ]
    list_display = ['seller_name', 'address']
    fields = ['seller_name', 'address', 'customers']
    readonly_fields = ['seller_name']
    search_fields = ['seller_name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description']
    search_fields = ['product_name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'status']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Seller, SellerAdmin)