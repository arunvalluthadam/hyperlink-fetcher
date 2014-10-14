from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from hyperlink.models import HyperlinkField
from hyperlink.forms import HyperlinkForm
import requests
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
	if request.POST:
		form = HyperlinkForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/show')
	else:
		form = HyperlinkForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response("home.html", args)

def lastone():
	lis = []
	for a in HyperlinkField.objects.all():
		lis.append(a.id)
	return lis[-1]

def show(request):
	hyperlinks = []
	c = HyperlinkField.objects.get(id=lastone())
	url = c.address
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	links = soup.find_all("a")
	for link in links:
	#	if "http" in link.get("href"):
		hyperlinks.append(str(link.get("href")))
	return render_to_response("show.html", {'hyperlinks': hyperlinks})