from django.contrib import admin
from .models import Customer, Categories, Orders, Pizza_Toppings, Sub_Toppings, Pizza, Subs, Pasta, Salads, DinnerPlatter

# Register your models here.
admin.site.register(Customer)
admin.site.register(Categories)
admin.site.register(Orders)
admin.site.register(Pizza_Toppings)
admin.site.register(Sub_Toppings)
admin.site.register(Pizza)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatter)