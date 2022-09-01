from datetime import datetime
from rest_framework import serializers


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='email@example.com', content='Hello World!')

# print(comment.email)


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=256)
    created = serializers.DateTimeField()


serializer = CommentSerializer(comment)

print('\n')
print(serializer.data)


## в формат json
from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)

print('\n')
print(json)


## из json в формат python
import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)

print('\n')
print(data)


serializer = CommentSerializer(data=data)
serializer.is_valid()
print('\n')
print(serializer.data)
