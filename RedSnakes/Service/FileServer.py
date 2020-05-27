from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


class FileServer:
    def __init__(self):
        pass

    '''def get_filename(self, request):
        context = {}
        if request.methos == 'POST':
            uploaded_file = request.FILES['mile']
            print(uploaded_file.name)
            print(uploaded_file.size)
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
        return render(request, 'speaker-register.html', context)'''
