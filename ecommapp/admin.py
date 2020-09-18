from django.contrib import admin

from ecommapp.models import cupon, estado_pedido, categoria, pedido, detalle_pedido

class cuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'descuento' )

class estado_pedidoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', )

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class pedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'subtotal', 'igv', 'total', 'cliente', 'estado', 'cupon')

class detalle_pedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'subtotal')

admin.site.register(cupon, cuponAdmin)
admin.site.register(estado_pedido, estado_pedidoAdmin)
admin.site.register(categoria, categoriaAdmin)
admin.site.register(pedido, pedidoAdmin)
admin.site.register(detalle_pedido, detalle_pedidoAdmin)