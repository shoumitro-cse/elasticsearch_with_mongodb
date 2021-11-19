from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.documents import DocType
from django_elasticsearch_dsl.registries import registry
from cars.models import Car, Manufacturer

# # The name of your index
# car_index = Index('cars')
# # See Elasticsearch Indices API reference for available settings
# car_index.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )


# @car_index.doc_type
# class CarDocument(DocType):
@registry.register_document
class CarDocument(Document):

    name = fields.TextField(
        attr='name',
        fields={
            'suggest': fields.Completion(),
        }
    )

    manufacturer = fields.ObjectField(
        properties={
            'name': fields.TextField(),
            'country_code': fields.TextField(),
        }
    )
    # Here, get_auction_title is a method name of Car model
    auction_title = fields.TextField(attr='get_auction_title')
    points = fields.IntegerField()

    def prepare_points(self, instance):
        if instance.color == 'silver':
            return 2
        return 1

    class Index:
        name = 'cars'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Car
        fields = [
            'id',
            'color',
            'description',
            'type',
        ]
        related_models = [Manufacturer]

    def get_queryset(self):
        return super().get_queryset().select_related('manufacturer')

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Manufacturer):
            return related_instance.car_set.all()


# Another way

# # The name of your index
# car = Index('cars')
# # See Elasticsearch Indices API reference for available settings
# car.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )
#
#
# @registry.register_document
# @car.document
# class CarDocument(Document):
#     class Django:
#         model = Car
#         fields = [
#             'name',
#             'color',
#         ]
#
#
# @registry.register_document
# class ManufacturerDocument(Document):
#     class Index:
#         name = 'manufacture'
#         settings = {'number_of_shards': 1,
#                     'number_of_replicas': 0}
#
#     class Django:
#         model = Manufacturer
#         fields = [
#             'name',
#             'country_code',
#         ]

