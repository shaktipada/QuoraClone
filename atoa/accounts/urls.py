from django.conf.urls import patterns, include, url
from accounts import views

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.accountRegistration_view', name='profile_page'),
    url(r'^login$', 'accounts.views.login_view', name='login_page'),
    url(r'^home$', 'accounts.views.home_view', name='home_page'),
    url(r'^logout$', 'accounts.views.logout_view', name='logout_page'),
    url(r'^question/(?P<id>[0-9]+)$', 'accounts.views.question_view', name='question_page'),
    url(r'^questions$', 'accounts.views.questions_view', name='questions_page'),
    url(r'^myquestions$', 'accounts.views.my_questions_view', name='my_questions_page'),
    url(r'^edit/(?P<id>[0-9]+)$', 'accounts.views.edit_view', name='edit_answer'),
    url(r'^question/(?P<id>[0-9]+)/delete$', 'accounts.views.delete_q_view', name='del_question_page'),
    url(r'^answer/(?P<id>[0-9]+)/delete$', 'accounts.views.delete_a_view', name='del_answer_page'),
)