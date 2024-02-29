from django.urls import path
from Messages.views import inbox, UserSearch, Directs, NewConversation, SendDirect,delete_message
urlpatterns = [
   	path('', inbox, name='inbox'),
   	path('directs/<username>', Directs, name='directs'),
   	path('/new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
    path('/send/', SendDirect, name="send-directs"),
    path('delete-message/<int:pk>',delete_message,name='delete-message')

]