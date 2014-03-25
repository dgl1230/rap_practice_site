from django.shortcuts import render_to_response
from django.template import RequestContext
from album.models import Album, Rapper

def AlbumsAll(request):
	albums = Album.objects.all().order_by('name')
	context = {'albums': albums}
	return render_to_response('albumsall.html', context, context_instance=RequestContext(request))

def SpecificAlbum(request, albumslug):
	album = Album.objects.get(slug=albumslug)
	context = {'album': album}
	return render_to_response('singlealbum.html', context, context_instance=RequestContext(request))

def SpecificRapper(request, rapperslug):
	rapper = Rapper.objects.get(slug=rapperslug)
	albums = Album.objects.filter(rapper=rapper)
	context = {'albums': albums}
	return render_to_response('singlerapper.html', context, context_instance=RequestContext(request))
