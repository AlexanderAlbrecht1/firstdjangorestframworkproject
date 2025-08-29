from django.urls import include, path
from .views import ManufacturerDetail, ManufacturerList, ManufacturerProductListCreate, ManufacturerUserDetail, ManufacturerUserList, MarketsView, ProductDetail, ProductList, SellersView, SellerDetailView, ProductListView, MarketDetailView, SellerOfMarketList, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/',MarketsView.as_view()),
    path('market/<int:pk>', MarketDetailView.as_view(), name ="market-detail"),
    path('market/<int:pk>/sellers', SellerOfMarketList.as_view()),
    path('seller/', SellersView.as_view()),
    path('seller/<int:pk>', SellerDetailView.as_view(), name='seller_single'),
    path('manufacturers/', ManufacturerList.as_view(), name='manufacturer-list'),
    path('manufacturers/<int:pk>/', ManufacturerDetail.as_view(), name='manufacturer-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('manufacturer-users/', ManufacturerUserList.as_view(), name='manufactureruser-list'),
    path('manufacturer-users/<int:pk>/', ManufacturerUserDetail.as_view(), name='manufactureruser-detail'),
    path('manufacturers/<int:manufacturer_id>/products/', ManufacturerProductListCreate.as_view(), name='manufacturer-product-list-create')
]