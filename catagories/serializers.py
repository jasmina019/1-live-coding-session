from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    name =serializers.CharField()
    slug = serializers.SlugField()
    description  =serializers.CharField()
    posts_count = serializers.SerializerMethodField()


