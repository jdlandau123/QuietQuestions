from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import Question, User

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question 
        fields = "__all__"


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=["GET"])
    def follow_question(self, request, pk=None):
        question = self.get_object()
        request.user.followed_questions.add(question)
        return Response(question.title, status=status.HTTP_200_OK) 

    @action(detail=True, methods=["GET"])
    def unfollow_question(self, request, pk=None):
        question = self.get_object()
        request.user.followed_questions.remove(question)
        return Response(question.title, status=status.HTTP_200_OK) 

    @action(detail=True, methods=["GET"])
    def report_question(self, request, pk=None):
        question = self.get_object()
        question.hidden = True
        question.save()
        admin = User.objects.get(username="admin")
        send_mail(
           "Decision Helper - Question Reported",
            f"""
            A question on Decision Helper was reported. Please review question id = {question.id}.
            The question will be hidden until further changes are made.
            """,
            None,
            [admin.email],
            fail_silently=True
        )
        return Response("Question reported", status=status.HTTP_200_OK)


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ChangePasswordView(UpdateAPIView):
    model = User
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response("Incorrect password", status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Password updated", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

