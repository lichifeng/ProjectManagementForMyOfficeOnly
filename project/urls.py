# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.views.generic import ListView, DetailView
import models
from django.conf import settings
from django.conf.urls.static import static

# 其实DJANGO的URLCONF还有必要重点研究一下
urlpatterns = [
    url(r'^$', ListView.as_view(model=models.Project), name="project-list"),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=models.Project), name="project-detail"),
    url(r'^note/(?P<pk>\d+)/$', DetailView.as_view(model=models.Note), name="note-detail")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)