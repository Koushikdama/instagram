
from django.shortcuts import redirect, render, get_object_or_404,HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from Messages.models import Message
from django.contrib.auth.models import User
from authy.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def inbox(request):
    user = request.user
    print("inbox",user)
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None
    profile = get_object_or_404(Profile, user=user)
    print("profile",profile.user.username)

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        user = get_object_or_404(User, username=active_direct)
        profile_receiver = Profile.objects.get(user=user)
        print("active",profile_receiver.user.username)
        directs = Message.objects.filter(user=request.user, reciepient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    context = {
        'directs':directs,
        'messages': messages,
        'active_direct': active_direct,
        'profile': profile,
        'profile_receiver':profile_receiver
    }
    return render(request, 'directs/message.html', context)


@login_required
def Directs(request, username):
    user  = request.user
    selected_user= get_object_or_404(User, username=username)    
    profile_search_selecter = Profile.objects.get(user=selected_user)
    messages = Message.get_message(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, reciepient__username=username)  
    directs.update(is_read=True)

    for message in messages:
            if message['user'].username == username:
                message['unread'] = 0
    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
        'profile_receiver':profile_search_selecter


    }
    return render(request, 'directs/message.html', context)

def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    print("user_to",to_user_username)
    body = request.POST.get('body')

    if request.method == "POST":
        to_user = User.objects.get(username=to_user_username)
        Message.sender_message(from_user, to_user, body)
        return redirect('inbox')

def UserSearch(request):
    query = request.GET.get('q')
    context = {}
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Paginator
        paginator = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
            }

    return render(request, 'directs/search.html', context)

def NewConversation(request, username):
    from_user = request.user
    body = ''
    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('usersearch')
    if from_user != to_user:
        Message.sender_message(from_user, to_user, body)
    return redirect('inbox')
def delete_message(request,pk):
    message=Message.objects.get(id=pk)
    message.delete()
    return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER'))

