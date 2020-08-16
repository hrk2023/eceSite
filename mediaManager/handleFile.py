def handleFiles(f):
    with open('mediaManager/write.md', 'wb+') as fptr:
        for chunk in f.chunks():
            fptr.write(chunk)