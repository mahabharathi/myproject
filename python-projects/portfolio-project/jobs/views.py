from django.shortcuts import render , get_object_or_404
from .models import Job
# Create your views here.
def home(request):
    # Redenr is used to render the information in html and to get db values use superclass of that app and .objects
    jobs=Job.objects
    return render(request,'jobs/home.html', {'jobs':jobs})

# variables needed to pass in method will be given like this

def detail(request,job_id):
    # import get_object_or_404 so that it throws error if the page not available
    job_detail = get_object_or_404(Job,pk=job_id)
    return render(request,'jobs/detail.html' , {'job':job_detail})
