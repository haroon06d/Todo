from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'notes/note_create.html')

def note_delete(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note_list')
