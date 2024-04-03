from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question 
        fields = "__all__"


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['post', 'delete'])
    def follow_question(self, request, pk=None):
        pass

