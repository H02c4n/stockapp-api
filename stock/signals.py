from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchases, Product, Sales




@receiver(post_save, sender=Purchases)
def increase_product_stock(sender, instance, created, **kwargs):
    if created:
        quantity = instance.quantity
        product_id = instance.product.id
        current_prd = Product.objects.filter(id= product_id)
        #print(quantity, product_id, current_prd[0].stock)
        Product.objects.filter(id=product_id).update(stock = current_prd[0].stock + quantity)





@receiver(post_save, sender=Sales)
def decrease_product_stock(sender, instance, created, **kwargs):
    if created:
        quantity = instance.quantity
        product_id = instance.product.id
        current_prd = Product.objects.filter(id = product_id)
        # if current_prd[0].stock < quantity:
        #     raise Exception(
        #         f'There is no more product more then **{current_prd[0].stock }**')
        Product.objects.filter(id=product_id).update(stock = current_prd[0].stock - quantity)  
