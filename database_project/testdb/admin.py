from django.contrib import admin
from testdb.models import testList, testForeign

# Register your models here.

admin.site.register(testList)
admin.site.register(testForeign)