from django.contrib import admin
from name.models import Contact

# Register your models here.
admin.site.site_header = 'Disky limited'
admin.site.site_title = 'Disky authentication'
admin.site.index_title = 'Disky Milk limited authentication system'

admin.site.register(Contact) 
