from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import View
from .forms import SubmitUrlForm
# Create your views here.
from .models import yellowURL
from analysis.models import ClickEvent

def home_view_fbv(request,*args,**kwargs):
	if requests.method=="POST":
		print(request.POST)
	return render(request,"shortener/home.html",{})

class HomeView(View):
	def get(self,request,*args,**kwargs):
		the_form=SubmitUrlForm()
		context={
		   "title":"Submit URL",
		   "form": the_form
		}
		return render(request,"shortener/home.html",context)

	def post(self,request,*args,**kwargs):
		form=SubmitUrlForm(request.POST)

		context={
		   "title":"Submit URL",
		   "form": form
		}
		template="shortener/home.html"
		if form.is_valid():
			new_url=form.cleaned_data.get("url")
			obj,created=yellowURL.objects.get_or_create(url=new_url)
			context={
			"object":obj,
			"created":created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/alread-exists.html"


		return render(request,template,context)


class URLRedirectView(View):
	def get(self,request,shortcode=None,*args,**kwargs):
		#print(shortcode)
		qs=yellowURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count()!=1 and qs.exists():
			raise Http404
		obj=qs.first()
		#obj=get_object_or_404(yellowURL,shortcode=shortcode)
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
		


