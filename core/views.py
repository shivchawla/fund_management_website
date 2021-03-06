from django.db.models import Sum
from django.shortcuts import render

from transactions.models import Deposit, Withdrawal, Returns


def home(request):
    if not request.user.is_authenticated:
        return render(request, "core/home.html", {})
    else:
        user = request.user
        deposit = Deposit.objects.filter(user=user)
        deposit_sum = deposit.aggregate(Sum('amount'))['amount__sum']
        withdrawal = Withdrawal.objects.filter(user=user)
        withdrawal_sum = withdrawal.aggregate(Sum('amount'))['amount__sum']
        returns = Returns.objects.filter(user=user)
        returns_sum = returns.aggregate(Sum('amount'))['amount__sum']

        context = {
                    "user": user,
                    "deposit": deposit,
                    "deposit_sum": deposit_sum,
                    "withdrawal": withdrawal,
                    "withdrawal_sum": withdrawal_sum,
                    "returns": returns,
                    "returns_sum": returns_sum,
                  }

        return render(request, "core/transactions.html", context)


def about(request):
    return render(request, "core/about.html", {})
