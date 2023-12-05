from django.contrib import admin
from core.models import Make, Model, Part, Category, Contact

admin.site.register([Make, Model, Part,Category, Contact ])
# Register your models here.
