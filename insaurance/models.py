from django.db import models

import uuid

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Lead(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    mobile_number = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    engine_number = models.CharField(max_length=200, null=True, blank=True)
    chassis_number = models.CharField(max_length=200, null=True, blank=True)

    hypothecation = models.CharField(max_length=200, null=True, blank=True)

    nominee_name = models.CharField(max_length=200, null=True, blank=True)
    nominee_age = models.CharField(max_length=200, null=True, blank=True)
    nominee_relation = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
    invoice_image = models.ImageField(
        upload_to='lead_form', null=True, blank=True)
    otherkyc_image = models.ImageField(
        upload_to='lead_form', null=True, blank=True)
    aadharcardf_image = models.ImageField(
        upload_to='lead_form', null=True, blank=True)
    aadharcardb_image = models.ImageField(
        upload_to='lead_form', null=True, blank=True)
    pan_image = models.ImageField(upload_to='lead_form', null=True, blank=True)

    address = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(
        max_length=200, null=True, blank=True, default="Pending")

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.customer_name


class UserMappingRequest(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    registration_number = models.IntegerField(null=True, blank=True)
    insurer_name = models.CharField(max_length=200, null=True, blank=True)
    policy_number = models.IntegerField(null=True, blank=True)
    premium = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='offlineQoute', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    #renew_at = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=200, null=True, blank=True, default='Pending')

    score = models.FloatField(null=True, blank=True)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.customer_name


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    issue = models.CharField(max_length=500, null=True, blank=True)
    old_value = models.CharField(max_length=200, null=True, blank=True)
    new_value = models.CharField(max_length=200, null=True, blank=True)

    myrequest = models.ForeignKey(
        UserMappingRequest, on_delete=models.CASCADE, null=True, blank=True)

    mylead = models.ForeignKey(
        Lead, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.issue


class LeadTicket(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    issue = models.CharField(max_length=500, null=True, blank=True)
    old_value = models.CharField(max_length=200, null=True, blank=True)
    new_value = models.CharField(max_length=200, null=True, blank=True)

    # myrequest = models.ForeignKey(
    # UserMappingRequest, on_delete=models.CASCADE, null=True, blank=True)

    mylead = models.ForeignKey(
        Lead, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.issue
