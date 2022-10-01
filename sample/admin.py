from django.contrib import admin

from sample.models import Order, OrderLine

class OrderLineInline(admin.StackedInline):
    model = OrderLine


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineInline,)


admin.site.register(Order, OrderAdmin)
