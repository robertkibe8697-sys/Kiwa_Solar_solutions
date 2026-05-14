from django.contrib import admin
from .models import Contact

admin.site.register(Contact)

from django.contrib import admin
from .models import Service

admin.site.register(Service)
from django.contrib import admin
from .models import HomePage, Project

admin.site.register(HomePage)
admin.site.register(Project)