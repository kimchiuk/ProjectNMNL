from rest_framework import serializers
from .models import Deposit, Savings, DepositOption, SavingOption

# 예금


class DepositListSerializer(serializers.ModelSerializer):
    cart_deposit = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Deposit
        fields = "__all__"


class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = "__all__"
        read_only_fields = ("fin_prdt_cd",)


# 적금


class SavingListSerializer(serializers.ModelSerializer):
    cart_saving = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Savings
        fields = "__all__"


class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = "__all__"
        read_only_fields = ("fin_prdt_cd",)
