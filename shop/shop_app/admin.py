from django.contrib import admin
from .models import User, Profile, Product, Cart, Payment_system, CommentAndRate

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Payment_system)
admin.site.register(CommentAndRate)

