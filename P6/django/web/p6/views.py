from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Group, Musician, Album
from .forms import GroupForm, AlbumForm, MusicianForm

# Create your views here.

def index(request):
    context = {}
    context['groups'] = Group.objects.all()
    context['musicians'] = Musician.objects.all()
    context['albums'] = Album.objects.all()
    
    return render(request,'index.html', context)

def groups(request):

    context = {}
    context['objects'] = Group.objects.all()

    print('Group' in type(context['objects'][0]).__name__)
    
    return render(request,'group-card.html', context)

def musicians(request):

    context = {}
    context['objects'] = Musician.objects.all() 
    
    return render(request,'musician-card.html', context)

def albums(request):

    context = {}
    context['objects'] = Album.objects.all()  
    
    return render(request,'album-card.html', context)

def groups_new(request):
    if request.method == "POST":
        
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('groups')
    else:
        form = GroupForm()

    return render(request, 'group-form.html', {'form': form})

def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        
        form = GroupForm(request.POST, instance = group)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('groups')
    else:
        form = GroupForm(instance = group)

    return render(request, 'group-form.html', {'form': form})

def musicians_new(request):
    if request.method == "POST":
        
        form = MusicianForm(request.POST)
        if form.is_valid():
            musician = form.save(commit=False)
            musician.save()
            return redirect('musicians')
    else:
        form = MusicianForm()

    return render(request, 'musician-form.html', {'form': form})

def musician_edit(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == "POST":
        
        form = MusicianForm(request.POST, instance = musician)
        if form.is_valid():
            musician = form.save(commit=False)
            musician.save()
            return redirect('musicians')
    else:
        form = MusicianForm(instance = musician)

    return render(request, 'musician-form.html', {'form': form})

def musician_delete(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    musician.delete()
    return redirect('musicians')

def albums_new(request):
    if request.method == "POST":
        
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('albums')
    else:
        form = AlbumForm()

    return render(request, 'album-form.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        
        form = AlbumForm(request.POST, instance = album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('albums')
    else:
        form = AlbumForm(instance = album)

    return render(request, 'album-form.html', {'form': form})

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'group-detail.html', {'group': group})

def musician_detail(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    return render(request, 'musician-detail.html', {'musician': musician})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album-detail.html', {'album': album})

def object_new(request):
    path = request.path
    
    if request.method == "POST":
        if("musicians" in path):
            form = MusicianForm(request.POST)
        elif("albums" in path):
            form = AlbumForm(request.POST)
        else:
            form = GroupForm(request.POST)
        
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect('index')
    else:
        if("musicians" in path):
            form = MusicianForm()
        elif("albums" in path):
            form = AlbumForm()
        else:
            form = GroupForm()

    return render(request, 'object-form.html', {'form': form})

def object_detail(request, pk):
    path = request.path
    
    if("musicians" in path):
        musician = get_object_or_404(Musician, pk=pk)
        return render(request, 'group-detail.html', {'group': group})
    elif("albums" in path):
        album = get_object_or_404(Album, pk=pk)
        return render(request, 'album-detail.html', {'album': album})
    else:
        group = get_object_or_404(Group, pk=pk)
        return render(request, 'group-detail.html', {'group': group})