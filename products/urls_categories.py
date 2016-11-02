from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^$', views.CategoryListView.as_view(), name='categories'),
    url(r'^(?P<slug>[\w-]+)/$', views.CategoryDetailView.as_view(), name='category_detail'),
]