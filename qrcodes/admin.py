from django.contrib import admin

from qrcodes.models import qr_code, download, key_value, ordering, ratings, usage

admin.site.register(qr_code)
admin.site.register(download)
admin.site.register(key_value)
admin.site.register(ordering)
admin.site.register(ratings)
admin.site.register(usage)


