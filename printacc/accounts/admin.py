from django.contrib import admin

from .models import Admin, Dealer, User, Plotter, Pattern, Clients


admin.site.register(Admin)
admin.site.register(Dealer)
admin.site.register(User)
admin.site.register(Plotter)
admin.site.register(Pattern)
admin.site.register(Clients)
