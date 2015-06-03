from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from kvitter_messages.models import Message

#details on messages
def message_details(request, post_id):
    message = Message.objects.get(pk=post_id)
    context = {'message': message}
    return render(request, 'messages/message_details.html', context)

#new messages
def message_listing(request):
    if request.method == 'POST':
        new_message = request.POST.get('new_message')
        if  new_message:
            postMessage = Message()
            postMessage.message = new_message
            postMessage.created_datetime = timezone.now()
            postMessage.created_by = request.user
            postMessage.save()
  
    messages = Message.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(messages, 5)
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)

    context = {'messages': messages,}
    return render(request, 'messages/message_listing.html', context)

#likes are not working...
def add_likes(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.likes = message.likes + 1
    message.save()
    data = {'likes_updated': message.likes}
    return JsonResponse(data)

