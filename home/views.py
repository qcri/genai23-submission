from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import testingform
# import socrates

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
            if data["prompt"] != '':
                prompt = data['prompt']
                form = testingform()
                # response = socrates.generate_response(prompt)
                response='true'
                conversation.insert(0, ['PhiloGPT: ' + response, 'You: ' + prompt])
    else:
        conversation=[]
        print(conversation)
        form = testingform()
    return render(request, "home.html", {"names": ["hello",2,3, 4], 'form':form, "conversation":conversation})
