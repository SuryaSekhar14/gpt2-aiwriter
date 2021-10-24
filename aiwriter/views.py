from django.http.response import HttpResponse
from django.shortcuts import render
from GPT2_Pytorch_From_scratch import testcall
import smtpserver

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def output(request):
    words = request.POST['text']
    apians = testcall.aicall(words)
    smtpserver.sendmail()
    return render(request, 'output.html', {'ai_output': apians}) 