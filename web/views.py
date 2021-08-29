from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
import json
from json import JSONEncoder
from web.models import User, Token, Expense, Income

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_expense(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    return JsonResponse({
        'status': 'ok'
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Income.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    return JsonResponse({
        'status': 'ok'
    }, encoder=JSONEncoder)
