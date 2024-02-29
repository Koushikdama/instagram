from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder

	

# Create your views here.
from Stories.models import Story, StoryStream
from Stories.forms import NewStoryForm

from datetime import datetime, timedelta
from authy.models import Profile


@login_required
def NewStory(request):
	user = request.user
	file_objs = []

	if request.method == "POST":
		form = NewStoryForm(request.POST, request.FILES)
		if form.is_valid():
			files = request.FILES.getlist('content')
			caption = form.cleaned_data.get('caption')
			for file in files:
				story = Story(user=user, content=file, caption=caption)
				story.save()
			return redirect('index')
	else:
		form = NewStoryForm()

	context = {
		'form': form,
	}

	return render(request, 'newstory.html', context)


def ShowMedia(request, stream_id):
	"""user = get_object_or_404(Story, id=stream_id)
	user_id=User.objects.get(username=user)
	receiver_user=get_object_or_404(Profile, user=user_id)"""
 
 
	stories = StoryStream.objects.get(id=stream_id)
	print("stories",stories.read)
	stories.read=True
	stories.save()
	print("stories",stories.read)
	
	media_st = stories.story.all().values()
	print("media_st",media_st)
	stories_list = list(media_st)
 
	print("stories after",stories.read)
	
	
	
	return JsonResponse(stories_list, safe=False)