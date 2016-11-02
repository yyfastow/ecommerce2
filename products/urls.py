from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='products'),
    url(r'(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'(?P<pk>\d+)/inventory/$', views.VariationListView.as_view(), name='product_inventory'),
]