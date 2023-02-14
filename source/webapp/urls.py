from django.urls import path

from webapp.views.tasks import add_view, detail_view, TaskDeleteView, TaskUpdateView
from webapp.views.base import index_view

urlpatterns =[
    path("", index_view),
    path('task/add', add_view),
    path('task/', detail_view),
    path(f'<pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path(f'<pk>/update/', TaskUpdateView.as_view(), name='update')
]
