from django.db import models


class Textbox(models.Model):
    name = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name



class Userinfo(models.Model):
    x = (("gaming", "gaming"),
         ("dancing", "dancing"),
         ("singing", "singing"))

    name = models.CharField(max_length=100, null=True)
    house = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    interest = models.CharField(max_length=200, null=True, choices=x)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    belongs = models.CharField(max_length=200, null=True)
    relbelongs = models.ManyToManyField(Userinfo)


    def __str__(self):
        return self.name    


class Linked(models.Model):
    name = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
