from rest_framework.viewsets import ViewSet


class MultiSerializerMixin(object):
    serializers = {"default": None}

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])


class BaseViewSet(MultiSerializerMixin, ViewSet):
    pass
