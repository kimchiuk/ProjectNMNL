from django.db import models
from accounts.models import User
from django.conf import settings


# Create your models here.

# 적금 상품

class Deposit(models.Model):
    fin_prdt_cd = models.CharField(unique=True, max_length=200) # 금융상품 코드
    fin_prdt_nm = models.CharField(max_length=200)              # 금융상품명
    kor_co_nm = models.CharField(max_length=200)                # 금융 회사명
    spcl_cnd = models.TextField(null=True)                      # 우대조건
    mtrt_int = models.TextField(null=True)                      # 최대 금리
    join_deny = models.IntegerField(null=True)                  # 가입 제한     
    join_member = models.TextField(null=True)                   # 가입 대상
    join_way = models.TextField(null=True)                      # 가입 방법
    cart_deposit = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cart_deposit_set', blank=True)
    
    
    
class DepositOption(models.Model):
    # product = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    fin_prdt_cd = models.ForeignKey(Deposit, on_delete=models.CASCADE)              # 금융상품 코드
    intr_rate = models.FloatField(null=True)                    # 저축 금리
    intr_rate2 = models.FloatField(null=True)                   # 최대 우대 금리
    save_trm = models.IntegerField(null=True)                   # 저축 기간
    

# 예금 상품

class Savings(models.Model):
    fin_prdt_cd = models.CharField(unique=True, max_length=200) # 금융상품 코드
    fin_prdt_nm = models.CharField(max_length=200)              # 금융상품명
    kor_co_nm = models.CharField(max_length=200)                # 금융 회사명
    spcl_cnd = models.TextField(null=True)                      # 우대조건
    mtrt_int = models.TextField(null=True)                      # 최대 금리
    join_deny = models.IntegerField(null=True)                  # 가입 제한     
    join_member = models.TextField(null=True)                   # 가입 대상
    join_way = models.TextField(null=True)                      # 가입 방법
    cart_saving = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cart_saving_set', blank=True)
    
    
class SavingOption(models.Model):
    # product = models.ForeignKey(Savings, on_delete=models.CASCADE)
    fin_prdt_cd = models.ForeignKey(Savings, on_delete=models.CASCADE)              # 금융상품 코드
    intr_rate = models.FloatField(null=True)                    # 저축 금리
    intr_rate2 = models.FloatField(null=True)                   # 최대 우대 금리
    save_trm = models.IntegerField(null=True)                   # 저축 기간