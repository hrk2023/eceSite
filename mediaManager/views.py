import uuid
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms.subjectForm import SubjectForm
from .creds import db
# Create your views here.
def index(request):
    response = db.subjects.find()
    return render(request, 'access.html')
'''
def videopage(request,course):
    courseCol = db[course]
    response = courseCol.find()
    return render(request, 'videoPage.html', {'videos' : response})

def subjectAdd(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subjectName = form.cleaned_data['subjectName']
            subjectCode = form.cleaned_data['subjectCode']
            subjectDescription = form.cleaned_data['subjectDescription']
            if subjectCode in db.list_collection_names():
                messages.error(request,'Subject Already Present!')
                return HttpResponseRedirect(request.path)
            #CREATING A NEW COLLECTION
            createdCol=db[subjectCode]
            createdCol.insert_one({"sampleId":100})
            subjectId = str(uuid.uuid4())
            status = db.subjects.insert_one({
                "subjectName":subjectName,
                "subjectCode":subjectCode,
                "subjectDescription":subjectDescription,
                "subjectId":subjectId
            })
            if status.inserted_id:
                return HttpResponseRedirect('/subject/')
            return render(request,'<h1>Error</h1>')

    response = db.subjects.find()
    return render(request, 'subject.html' , {'form': form,'subjects':response})


def subjectDelete(request,id):
    response = db.subjects.delete_one({"subjectCode":id})
    deleteCol = db[id]
    res = deleteCol.drop()
    if response:
        messages.success(request,'Subject Deleted')
        return HttpResponseRedirect('/subject/')
    messages.error(request,'Subject Cannot be deleted')
    return HttpResponseRedirect('/subject/')

def videoadd(request):
    if request.method == 'POST':
        videoTitle = request.POST.get("videoTitle")
        videoLink = request.POST.get("videoLink")
        videoDescription = request.POST.get("videoDescription")
        course = request.POST.get("course")
        courseCol = db[course]
        response = courseCol.insert_one({
            "videoTitle": videoTitle,
            "videoLink": videoLink,
            "videoDescription": videoDescription,
            "dateTime": datetime.datetime.utcnow()
        })
        if response:
            messages.success(request,'Video Added')
            return HttpResponseRedirect('/videoadd/')

    response = db.subjects.find()
    return render(request, 'videoAdd.html', {'subjects' : response})


def dberror(request):
    return render(request,'databaseError.html')
'''
