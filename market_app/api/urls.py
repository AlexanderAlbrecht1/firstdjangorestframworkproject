from django.urls import include, path
from .views import MarketsView, SellersView, SellerDetailView, ProductListView, MarketDetailView, SellerOfMarketList, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/',MarketsView.as_view()),
    path('market/<int:pk>', MarketDetailView.as_view(), name ="market-detail"),
    path('market/<int:pk>/sellers', SellerOfMarketList.as_view()),
    path('seller/', SellersView.as_view()),
    path('product/', ProductListView.as_view()),
    path('seller/<int:pk>', SellerDetailView.as_view(), name='seller_single')
]
