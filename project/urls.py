# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.views.generic import ListView
import models
from django.conf import settings
from django.conf.urls.static import static

# 其实DJANGO的URLCONF还有必要重点研究一下
urlpatterns = [
    url(r'^$', ListView.as_view(model=models.Project), name="project-list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)