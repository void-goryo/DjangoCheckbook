from django.shortcuts import get_object_or_404, render, redirect
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm

def home(request):
    return render(request, 'checkbook/index.html')

def balance(request):
    account = get_object_or_404(Account, pk=pk)
    content = {'account':account}
    return render(request, 'checkbook/BalanceSheet.html', content)

def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form':form}
    return render(request, 'checkbook/CreateNewAccount.html', content)

def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form':form}
    return render(request, 'checkbook/AddTransaction.html', content)
