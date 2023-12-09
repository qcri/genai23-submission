from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import testingform

conversation=[]
# Create your views here.
def home(request):
    global conversation
    if request.method == "POST":
        print(conversation)
        print(request)
        form = testingform(request.POST)
        # do not remove the print here or code won't work
        print(form)
        if form.is_valid:
            data=form.cleaned_data
            conversation.append(data['prompt'])
            if data["prompt"]=="A":
                conversation.append("halellouya")
            else:
                conversation.append('too bad')
    else:
        conversation=[]
        print(conversation)
        form = testingform()
    return render(request, "home.html", {"names": ["hello",2,3, 4], 'form':form, "conversation":conversation})
