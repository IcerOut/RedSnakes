from django.contrib import admin

from ConferenceManager.models import Paper

# Test for api/papers/get?id=
admin.site.register(Paper)
