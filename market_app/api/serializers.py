from rest_framework import serializers
from market_app.models import Market, Seller, Product


class MarketSerializer(serializers.ModelSerializer):    

    sellers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='seller_single')

    class Meta:
        model = Market
        fields = '__all__'

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
    
class MarketHyperlinkedSerializer(MarketSerializer, serializers.HyperlinkedModelSerializer):    

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Market
        fields =  ['id','url','name','location','description','net_worth','sellers']


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
    
     
class ProductDetailSerializer(serializers.ModelSerializer):
    
    seller = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='seller_single')
    market = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='market-detail')

    class Meta:
        model = Product
        fields = '__all__'


class SellerListSerializer(SellerSerializer):
        class Meta:
            model = Seller
            fields = ['id','name','market_ids','market_count','contact_info']
