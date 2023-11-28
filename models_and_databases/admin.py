from django.contrib import admin

from .models import Author
from .models import Blog
from .models import Entry
from .models import Pizza
from .models import Topping

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Entry)
