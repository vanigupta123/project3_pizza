from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    # orders = models.ManyToManyField(Orders, blank=True, related_name="customers")

class Categories(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.category

class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_id")
    status = models.CharField(max_length=64)
    # include order_id from orders_exp

# class Orders_Exp(models.Model):
    # have item_id that the customer has chosen
    # have toppings_chosen_id
    # multiple rows can have the same order_id from class Orders

class Pizza_Toppings(models.Model):
    topping = models.CharField(max_length=128)

    def __str__(self):
        return self.topping

class Sub_Toppings(models.Model):
    topping = models.CharField(max_length=128)
    price = models.FloatField()

    def __str__(self):
        return self.topping

class Pizza(models.Model):
    item = models.CharField(max_length=512)
    pizzatype = models.CharField(max_length=64)
    # need to make the toppings only available for certain selections (everything but cheese)
    # need to allow users to choose multiple toppings
    # toppings = models.CharField(max_length=128)
    price = models.FloatField()

    def __str__(self):
        return self.pizzatype + self.item + ' (' + str(self.price) + ')'

# class Pizza_Orders(models.Model):
    # item_id of pizza order
    # names of toppings

# class Sub_Orders(models.Model):
    # item_id of pizza order
    # names of add-ons

class Subs(models.Model):
    item = models.CharField(max_length=512)
    # need to make the toppings only available for steak+cheese sub and only allow mushrooms, green peppers, onions, as options
    # toppings = models.ForeignKey(Sub_Toppings, on_delete=models.CASCADE, related_name="toppings_subs")
    price = models.FloatField()

    def __str__(self):
        return self.item + ' (' + str(self.price) + ')'

class Pasta(models.Model):
    item = models.CharField(max_length=512)
    price = models.FloatField()

    def __str__(self):
        return self.item + ' (' + str(self.price) + ')'

class Salads(models.Model):
    item = models.CharField(max_length=512)
    price = models.FloatField()

    def __str__(self):
        return self.item + ' (' + str(self.price) + ')'

class DinnerPlatter(models.Model):
    item = models.CharField(max_length=512)
    price = models.FloatField()

    def __str__(self):
        return self.item + ' (' + str(self.price) + ')'
