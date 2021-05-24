from django.shortcuts import render
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create your views here.

def index(request):
    return render(request, 'index.html',{})