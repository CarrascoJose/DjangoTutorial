from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='all-meetups'), #our-domain.com/meetups
    path('<meetup_slug>',views.meetup_details,name='meetup-detail'), #our-domain.com/meetups/<dynamic-path-segment>
    path('confirmation/<meetup_slug>',views.confirmation_page,name='meetup-confirmation') #confirmation-page
]