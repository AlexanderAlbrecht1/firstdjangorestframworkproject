from django.urls import path
from .views import MarketsView, SellersView, SellerDetailView, ProductListView, MarketDetailView, SellerOfMarketList

urlpatterns = [
    path('market/',MarketsView.as_view()),
    path('market/<int:pk>', MarketDetailView.as_view(), name ="market-detail"),
    path('market/<int:pk>/sellers', SellerOfMarketList.as_view()),
    path('seller/', SellersView.as_view()),
    path('product/', ProductListView.as_view()),
    path('seller/<int:pk>', SellerDetailView.as_view(), name='seller_single')
]
