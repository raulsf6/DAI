from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Group, Musician, Album
from .forms import GroupForm, AlbumForm, MusicianForm
from itertools import chain
from django.http import JsonResponse
import json

def index(request):
    context = {}
    elements_per_row = 4
    page = 1

    musicians_num = Musician.objects.all().count() 
    albums_num =  Album.objects.all().count() 
    groups_num = Group.objects.all().count()
    elements = musicians_num + albums_num + groups_num
    
    num_pages = elements // elements_per_row if elements % elements_per_row == 0 else elements // elements_per_row + 1
    context['previous'] = page - 1 if page > 1 else 1
    context['next'] = page + 1 if page < num_pages else num_pages
    context['range_pages'] = range(1, num_pages+1)
    
    return render(request,'general-list.html', context)

def get_page(request):
    data = {}
    data['elements'] = []
    objects = []
    elements_per_row = 3
    page = int(request.GET.get('page', -1))

    #Get all objects
    for group in Group.objects.all():
        objects.append((group.name, "/musicdb/groups/" + str(group.pk) + "/"))
    for musician in Musician.objects.all():
        objects.append((musician.name, "/musicdb/musicians/" + str(musician.pk) + "/"))
    for album in Album.objects.all():
        objects.append((album.title, "/musicdb/albums/" + str(album.pk) + "/"))
        
    elements = len(objects)
    
    # If module is != we have to add one more page
    num_pages = elements // elements_per_row if elements % elements_per_row == 0 else elements // elements_per_row + 1
        
    data['previous'] = page - 1 if page > 1 else 1
    data['next'] = page + 1 if page < num_pages else num_pages
        
    for i in range((page-1)*elements_per_row, page*elements_per_row):
        if i >= elements:
            break
        else:
            data["elements"].append({"name": objects[i][0], "url": objects[i][1]})
        
    data['pages'] = num_pages

    return JsonResponse(data, safe=False)

def groups(request):

    context = {}
    context['objects'] = Group.objects.all()
    
    return render(request,'group-card.html', context)

def musicians(request):

    context = {}
    context['objects'] = Musician.objects.all() 
    
    return render(request,'musician-card.html', context)

def albums(request):

    context = {}
    context['objects'] = Album.objects.all()  
    
    return render(request,'album-card.html', context)

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

    return render(request, 'object-form.html', {'form': form})

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

    return render(request, 'object-form.html', {'form': form})

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

    return render(request, 'object-form.html', {'form': form})

def object_delete(request, pk):
    path = request.path

    if("musicians" in path):
        musician = get_object_or_404(Musician, pk=pk)
        musician.delete()
        return redirect('musicians')
    elif("albums" in path):
        album = get_object_or_404(Album, pk=pk)
        album.delete()
        return redirect('albums')
    else:
        group = get_object_or_404(Group, pk=pk)
        group.delete()
        return redirect('groups')

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
        return render(request, 'musician-detail.html', {'musician': musician})
    elif("albums" in path):
        album = get_object_or_404(Album, pk=pk)
        return render(request, 'album-detail.html', {'album': album})
    else:
        group = get_object_or_404(Group, pk=pk)
        return render(request, 'group-detail.html', {'group': group})