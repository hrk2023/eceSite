import uuid
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms.subjectForm import SubjectForm
from .creds import db
from .handleFile import handleFiles
# Create your views here.
def index(request):
    response = db.subjects.find()
    return render(request, 'layout.html', {'subjects' : response})

def videopage(request,course):
    courseCol = db[course]
    response = courseCol.find()
    return render(request, 'videoPage.html', {'videos' : response})

def pdfpage(request,course):
    course = course + 'P'
    courseCol = db[course]
    response = courseCol.find()
    return render(request, 'pdfPage.html', {'docs' : response})

def livevidpage(request,course):
    course = course + 'L'
    courseCol = db[course]
    response = courseCol.find()
    return render(request, 'livePage.html', {'videos' : response})

def classification(request,course):
    subjectDetails = db.subjects.find_one({"subjectCode":course})
    return render(request,'classification.html', {'courseDetails': subjectDetails})

# ADD A NEW SUBJECT
def subjectAdd(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            subjectName = form.cleaned_data['subjectName']
            subjectCode = form.cleaned_data['subjectCode']
            subjectDescription = form.cleaned_data['subjectDescription']
            if subjectCode in db.list_collection_names():
                messages.error(request,'Subject Already Present!')
                return HttpResponseRedirect(request.path)

            #CREATING A NEW COLLECTION FOR VIDEOS
            createdCol=db[subjectCode]
            createdCol.insert_one({"sampleId":100})
            #CREATING A NEW COLLECTION FOR VIDEOS END

            #CREATING A NEW COLLECTION FOR DOCUMENT
            doc = subjectCode + 'P'
            createdCol=db[doc]
            createdCol.insert_one({"sampleId":100})
            #CREATING A NEW COLLECTION FOR DOCUMENT END

            #CREATING A NEW COLLECTION FOR LIVE VIDEO
            liveVid = subjectCode + 'L'
            createdCol=db[liveVid]
            createdCol.insert_one({"sampleId":100})
            #CREATING A NEW COLLECTION FOR LIVE VIDEO END


            subjectId = str(uuid.uuid4())

            #HANDLING FILES FOR MARKDOWN
            handleFiles(request.FILES["files"])
            #HANDLING FILES FOR MARKDOWN END

            #READING FROM MARKDOWN AND INSERTING IN DATABASE
            insert_status = ''
            with open('mediaManager/write.md', 'r') as fptr:
                lines = fptr.read()
                status = db.subjects.insert_one({
                    "subjectName":subjectName,
                    "subjectCode":subjectCode,
                    "subjectDescription":subjectDescription,
                    "subjectId":subjectId,
                    "subjectDetails":lines,
                    "liveVid":liveVid,
                    "doc":doc
                })
                insert_status = status
            #READING FROM MARKDOWN END 

            if insert_status.inserted_id:
                return HttpResponseRedirect('/subject/')
            return render(request,'<h1>Error</h1>')

    response = db.subjects.find()
    return render(request, 'subject.html' , {'form': form,'subjects':response})
# ADD A NEW SUBJECT END


# UPDATE A SUBJECT
def subjectUpdate(request,id):
    if request.method == 'POST':
        subjectName = request.POST.get('subjectName')
        subjectCode = request.POST.get('subjectCode')
        subjectDescription = request.POST.get('subjectDescription')
        handleFiles(request.FILES["files"])
        insert_status = ''
        with open('mediaManager/write.md', 'r') as fptr:
            lines = fptr.read()
            status = db.subjects.update_one(
                {
                    "subjectId":id
                },
                {
                    '$set':{
                        "subjectName":subjectName,
                        "subjectCode":subjectCode,
                        "subjectDescription":subjectDescription,
                        "subjectDetails":lines
                    }
                }
            )
            insert_status = status
        if insert_status:
            return HttpResponseRedirect('/subject/')
        return render(request,'<h1>Error</h1>')

# UPDATE A SUBJECT END


# DELETE A SUBJECT
def subjectDelete(request,id):
    response = db.subjects.delete_one({"subjectCode":id})

    # DELETING ALL COLLECTIONS RELATED TO THE SUBJECT
    deleteCol = db[id]
    res = deleteCol.drop()
    live = id + 'L'
    delLive = db[live]
    res2 = delLive.drop()
    doc = id + 'P'
    delDoc = db[doc]
    res3 = delDoc.drop()
    # DELETING ALL COLLECTIONS RELATED TO THE SUBJECT

    if response:
        messages.success(request,'Subject Deleted')
        return HttpResponseRedirect('/subject/')
    messages.error(request,'Subject Cannot be deleted')
    return HttpResponseRedirect('/subject/')
# DELETE A SUBJECT END

# ADD A VIDEO
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
# ADD A VIDEO END 

# ADD A DOCUMENT
def pdfadd(request):
    if request.method == 'POST':
        pdfTitle = request.POST.get("pdfTitle")
        pdfLink = request.POST.get("pdfLink")
        pdfDescription = request.POST.get("pdfDescription")
        course = request.POST.get("course")
        course = course + 'P'
        courseCol = db[course]
        response = courseCol.insert_one({
            "pdfTitle": pdfTitle,
            "pdfLink": pdfLink,
            "pdfDescription": pdfDescription,
            "dateTime": datetime.datetime.utcnow()
        })
        if response:
            messages.success(request,'Document Added')
            return HttpResponseRedirect('/pdfadd/')

    response = db.subjects.find()
    return render(request, 'pdfAdd.html', {'subjects' : response})
# ADD A DOCUMENT END 

# ADD A LIVE VIDEO
def livevidadd(request):
    if request.method == 'POST':
        liveTitle = request.POST.get("liveTitle")
        liveLink = request.POST.get("liveLink")
        liveDescription = request.POST.get("liveDescription")
        course = request.POST.get("course")
        course = course + 'L'
        courseCol = db[course]
        response = courseCol.insert_one({
            "liveTitle": liveTitle,
            "liveLink": liveLink,
            "liveDescription": liveDescription,
            "dateTime": datetime.datetime.utcnow()
        })
        if response:
            messages.success(request,'Video Added')
            return HttpResponseRedirect('/liveadd/')

    response = db.subjects.find()
    return render(request, 'liveAdd.html', {'subjects' : response})
# ADD A LIVE VIDEO END

def dberror(request):
    return render(request,'databaseError.html')

def error_404(request,exception):
    return render(request,'404.html')

def error_500(request):
    return render(request,'500.html')