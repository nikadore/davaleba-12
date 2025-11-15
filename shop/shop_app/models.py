from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart ({self.user.username})"
    

class Payment_system(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    PAYMENT_SYSTEMS = [
        ('card', 'Credit/Debit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash on Delivery'),
    ]


    payment_system = models.CharField(
        max_length=20,
        choices=PAYMENT_SYSTEMS,
        default='card'
    )

    def __str__(self):
        return f"{self.user.username} payment system"
    


class CommentAndRate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.FloatField(validators=[ MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f"Comment from {self.user}"