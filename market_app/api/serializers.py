from rest_framework import serializers
from market_app.models import Market, Seller, Product



class MarketSerializer(serializers.ModelSerializer):    

    sellers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='seller_single')

    class Meta:
        model = Market
        fields = ['id', 'sellers', 'name', 'location', 'description', 'net_worth']

    def validate_name(self, value):
        errors = []

        if "X" in value:
            errors.append('Bitte kein Schweinskram')
        if "Y" in value:
            pass
            errors.append('Bitte kein Schweinskram mit Y')

        if errors:
             raise serializers.ValidationError(errors)
        return value


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(read_only=True, many=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset = Market.objects.all(),
        many = True,
        write_only = True,
        source = 'markets'
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = '__all__'

    def get_market_count(self, obj):
        return obj.markets.count()
    
     
class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=50, decimal_places=2)
    market = serializers.StringRelatedField(many=True)
    seller = serializers.StringRelatedField(many=True)


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=50, decimal_places=2)
    market = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    seller = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    def validate_markets(self, value):
        market = Market.objects.filter(id__in = value)
        if len(market) != len(value):
            raise serializers.ValidationError("market id not found")
        return value
    
    def validate_seller(self, value):
        seller = Seller.objects.filter(id__in = value)
        if len(seller) != len(value):
            raise serializers.ValidationError("market id not found")
        return value

    def create(self, validated_data):
         market_ids = validated_data.pop('market')
         seller_ids = validated_data.pop('seller')
         market = Market.objects.filter(id__in = market_ids)
         seller = Seller.objects.filter(id__in = seller_ids)
         product = Product.objects.create(**validated_data)
         product.market.set(market)
         product.seller.set(seller)
         return product
