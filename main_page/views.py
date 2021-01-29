from django.shortcuts import render, redirect
from main_page.forms import CongratulationForm
from main_page.models import Congratulation
# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html',)


def wish_luck(request):
    if request.method == 'GET':
        return render(request, 'wish-luck.html')


def add_congratulation(request):
    if request.method == 'POST':
        form = CongratulationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            congratulation = data.get('congratulation')
            Congratulation.objects.create(congratulation=congratulation)
        return redirect('/home/')


def congratulations(request):
    if request.method == 'GET':
        congratulations_list = Congratulation.objects.all()
        return render(request, 'congratulations.html', {'congratulations_list': congratulations_list})