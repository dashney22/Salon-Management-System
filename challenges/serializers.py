from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name','description','price','is_published']