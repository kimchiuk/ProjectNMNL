from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import requests
from .serializers import *
from .models import *


# 데이터 저장


@api_view(["GET"])
def save_deposit_products(request):
    api_key = "86e1ebd9ab78fc50a98238444152d6e1"
    url = f"http://finlife.fss.or.kr/finlifeapi/"
    params = {
        "auth": api_key,
        "topFinGrpNo": "020000",
        "pageNo": 1,
    }
    deposit = "depositProductsSearch.json"

    deposit_response = requests.get(url + deposit, params=params).json()
    deposit_base_list = deposit_response.get("result").get("baseList")
    deposit_option_list = deposit_response.get("result").get("optionList")

    deposit_base_serializer = DepositListSerializer(data=deposit_base_list, many=True)
    if deposit_base_serializer.is_valid(raise_exception=True):
        deposit_base_serializer.save()

    for deposit_option in deposit_option_list:
        deposit_option_serializer = DepositOptionSerializer(data=deposit_option)
        if deposit_option_serializer.is_valid(raise_exception=True):
            deposit_product = Deposit.objects.get(
                fin_prdt_cd=deposit_option["fin_prdt_cd"]
            )
            deposit_option_serializer.save(fin_prdt_cd=deposit_product)

    saving = "savingProductsSearch.json"

    saving_response = requests.get(url + saving, params=params).json()
    saving_base_list = saving_response.get("result").get("baseList")
    saving_option_list = saving_response.get("result").get("optionList")

    saving_base_serializer = SavingListSerializer(data=saving_base_list, many=True)
    if saving_base_serializer.is_valid(raise_exception=True):
        saving_base_serializer.save()

    for saving_option in saving_option_list:
        saving_option_serializer = SavingOptionSerializer(data=saving_option)
        if saving_option_serializer.is_valid(raise_exception=True):
            saving_product = Savings.objects.get(
                fin_prdt_cd=saving_option["fin_prdt_cd"]
            )
            saving_option_serializer.save(fin_prdt_cd=saving_product)
    return Response(saving_option_serializer.data, status=status.HTTP_200_OK)


# 예금 리스트
@api_view(["GET"])
def deposit_list(request):
    depositproducts = Deposit.objects.all()
    print(depositproducts)
    serializer = DepositListSerializer(depositproducts, many=True)
    # if serializer.is_valid(raise_exception=True):
    return Response(serializer.data, status=status.HTTP_200_OK)


# 예금 상세
@api_view(["GET"])
def deposit_option(request):
    depositproduct = DepositOption.objects.all()
    serializer = DepositOptionSerializer(depositproduct, many=True)
    # if serializer.is_valid(raise_exception=True):
    return Response(serializer.data, status=status.HTTP_200_OK)


# 적금 리스트
@api_view(["GET"])
def savings_list(request):
    savingproducts = Savings.objects.all()
    serializer = SavingListSerializer(savingproducts, many=True)
    # if serializer.is_valid(raise_exception=True):
    return Response(serializer.data, status=status.HTTP_200_OK)


# 적금 상세
@api_view(["GET"])
def savings_option(request):
    savingproduct = SavingOption.objects.all()
    serializer = SavingOptionSerializer(savingproduct, many=True)
    # if serializer.is_valid(raise_exception=True):
    return Response(serializer.data, status=status.HTTP_200_OK)
