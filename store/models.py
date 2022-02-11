from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SimFree(models.Model):
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    
    os = models.CharField(max_length=254, null=True, blank=True)
    screen = models.DecimalField(max_digits=6, decimal_places=2)
    camera = models.CharField(max_length=254, null=True, blank=True)
    storage = ArrayField(models.IntegerField(blank=True, null=True))
    # =============================================================
    colors = ArrayField(models.CharField(max_length=254, null=True, blank=True))
    cost = ArrayField(models.FloatField(blank=True, null=True))
    img = models.ImageField(null=True, blank=True)
    img_1 = models.ImageField(null=True, blank=True)
    img_2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


# class SimOnly(models.Model):
#     category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
#     name = models.CharField(max_length=254)

#     cost = models.DecimalField(max_digits=6, decimal_places=2)
#     data = models.CharField(max_length=254, null=True, blank=True)
#     minutes = models.CharField(max_length=254, null=True, blank=True)
#     text = models.CharField(max_length=254, null=True, blank=True)
#     data_5g = models.BooleanField(default=False, null=True, blank=True)
#     length = models.CharField(max_length=254, null=True, blank=True)
#     # =============================================================

#     def __str__(self):
#         return self.name

    
# class SimPlan(models.Model):
#     category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
#     name = models.CharField(max_length=254)
#     os = models.CharField(max_length=254, null=True, blank=True)
#     screen = models.DecimalField(max_digits=6, decimal_places=2)
#     camera = models.CharField(max_length=254, null=True, blank=True)
#     storage = models.CharField(max_length=254, null=True, blank=True)
#     # =============================================================
#     colors = models.CharField(max_length=254, null=True, blank=True)
#     # May need to delete this part as already in sim_free

#     bronze_24_upfront = models.DecimalField(max_digits=6, decimal_places=2)
#     bronze_24_monthly = models.DecimalField(max_digits=6, decimal_places=2)
#     silver_24_upfront = models.DecimalField(max_digits=6, decimal_places=2)
#     silver_24_monthly = models.DecimalField(max_digits=6, decimal_places=2)
#     gold_24_upfront = models.DecimalField(max_digits=6, decimal_places=2)
#     gold_24_monthly = models.DecimalField(max_digits=6, decimal_places=2)
#     platinum_24_monthly = models.DecimalField(max_digits=6, decimal_places=2)

#     def __str__(self):
#         return self.name