from rest_framework.serializers import ModelSerializer


class BaseReadSerializer(ModelSerializer):
    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)

        if fields:
            common_fields = ["id", "created", "modified"]
            fields = list(set(fields) - set(common_fields))
            fields.extend(common_fields)
        return fields


class BaseWriteSerializer(ModelSerializer):
    pass
