from django.db import models

class Element(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    active=models.CharField(max_length=10,default='Y')


class Commodity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    inventory = models.FloatField()
    price = models.FloatField()
    active = models.CharField(max_length=10, default='Y')


class Chemical_composition(models.Model):
    id = models.IntegerField(primary_key=True)
    comodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    percentage = models.IntegerField()
    active = models.CharField(max_length=10, default='Y')





# class percentage(models.Model):
#     commodity_composition = models.OneToOneField(element, on_delete=models.CASCADE)
#     percentage = models.IntegerField()
#
# class Commodity(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     inventory = models.FloatField()
#     price = models.FloatField()
#     # commodity_composition = models.OneToOneField(Chemical_composition, on_delete=models.CASCADE)







# Create your models here.
# class Chemical_element(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     # chemical_composition = models.ForeignKey('Commodity', on_delete=models.CASCADE, related_name='eleref')
#
# class Commodity(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     inventory = models.FloatField()
#     price = models.FloatField()
#     chemical_composition = models.ForeignKey('Chemical_element', on_delete=models.CASCADE, related_name='comref')