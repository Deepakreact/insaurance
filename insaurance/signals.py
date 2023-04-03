from django.db.models.signals import pre_save
from .models import *
from django.db.models import F, ExpressionWrapper,  DateField
from datetime import timedelta


# def updateLead(sender, instance, **kwargs):
#     item = instance
#     print('item', item)

#     if item.score == None:
#         item.score = item.premium*12/100


# pre_save.connect(updateLead, sender=Lead)


def updateQoute(sender, instance, **kwargs):
    item = instance
    print('item', item)

    if item.score == None:
        item.score = item.premium*12/100

    # if item.renew_at == None:
    #     print(item.created_at + timedelta(days=10))
        # item.renew_at = ExpressionWrapper(
        #     DateField(item.created_at)+timedelta(days=10), output_field=DateField())


pre_save.connect(updateQoute, sender=UserMappingRequest)


# ExpressionWrapper(
#     F('created_at') + timedelta(days=8), output_field=DateField()),
