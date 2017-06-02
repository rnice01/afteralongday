from django.contrib import admin
from .models import BathBombs, Invoice, Order

class BathBombAdmin(admin.ModelAdmin):
    exclude = ('Invoice', )

class OrderInline(admin.TabularInline):
    model = Order

class InvoiceAdmin(admin.ModelAdmin):
    inlines = (OrderInline, )

admin.site.register(BathBombs, BathBombAdmin)
admin.site.register(Invoice, InvoiceAdmin)