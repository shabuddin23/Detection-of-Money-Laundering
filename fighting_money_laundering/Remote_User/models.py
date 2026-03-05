from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class predict_money_laundering(models.Model):

    Fid= models.CharField(max_length=300)
    AccOpenDate= models.CharField(max_length=300)
    CustomerId= models.CharField(max_length=300)
    Surname= models.CharField(max_length=300)
    CreditScore= models.CharField(max_length=300)
    Geography= models.CharField(max_length=300)
    Gender= models.CharField(max_length=300)
    Age= models.CharField(max_length=300)
    Tenure= models.CharField(max_length=300)
    Balance= models.CharField(max_length=300)
    NumOfProducts= models.CharField(max_length=300)
    HasCrCard= models.CharField(max_length=300)
    IsActiveMember= models.CharField(max_length=300)
    EstimatedSalary= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



