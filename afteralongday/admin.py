from django.contrib import admin
from .models import BathBombs, Invoice, Order

class BathBombAdmin(admin.ModelAdmin):
    exclude = ('Invoice', )

class OrderAdmin(admin.ModelAdmin):
    model = Order

class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice

admin.site.register(Order, OrderAdmin)
admin.site.register(BathBombs, BathBombAdmin)
admin.site.register(Invoice, InvoiceAdmin)