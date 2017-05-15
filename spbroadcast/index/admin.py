from django.contrib import admin
from .models import User
from .models import Group
from .models import Spnews
from .models import Presenter
from .models import Banner

# admin.site.register(User)
admin.site.register(Group)
admin.site.register(Spnews)
admin.site.register(Presenter)
admin.site.register(Banner)
# Register your models here.
