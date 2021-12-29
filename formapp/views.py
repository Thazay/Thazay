from django.shortcuts import render
from formapp.forms import FormDetailsForm
from  formapp.models import FormDetails
# Create your views here.

def form_display(request):
	if request.method=='GET':
		#Creating the object of the form for displaying the form on the web browser
		form=FormDetailsForm()
		return render(request,'formapp/display.html',context={"form":form})

def form_accept(request):
	if request.method=='POST':
		#Fetching the data from the web browser using request.POST
		form=FormDetailsForm(request.POST)
		if form.is_valid():
			form.save()

		data=FormDetails.objects.all()

	#form=FormDetailsForm()
	return render(request,'formapp/data.html',context={"data":data})
