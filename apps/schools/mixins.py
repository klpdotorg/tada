from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin

from schools.models import Question


class CompensationLogMixin(CreateModelMixin, UpdateModelMixin):
    def perform_create(self, serializer):
        serializer.save(double_entry=1)

    def perform_update(self, serializer):
        serializer.save(double_entry=2)


class BulkAnswerCreateModelMixin(CreateModelMixin):
    """
    This is borrowed and overriden from:
    https://github.com/miki725/django-rest-framework-bulk/blob/master/rest_framework_bulk/drf3/mixins.py

    Either create a single or many model instances in bulk by using the
    Serializers ``many=True`` ability from Django REST >= 2.2.5.
    .. note::
        This mixin uses the same method to create model instances
        as ``CreateModelMixin`` because both non-bulk and bulk
        requests will use ``POST`` request method.
    """
    def _cast_answer_type(self, data):
        if not data.get('answer'):
            raise APIException("'answer' field required")
        
        question_id = data.get('question', None)
        try:
            question = Question.objects.get(id=question_id)
        except Exception as ex:
            raise APIException(ex)

        if question.question_type == 1: # Implies it is of 'Marks' type.
            data['answer_score'] = data.pop('answer')
        else:
            data['answer_grade'] = data.pop('answer')

        return data

    def _cast_answer_types(self, request_data, many=None):
        if many:
            processed_data = [self._cast_answer_type(data) for data in request_data]
        else:
            processed_data = self._cast_answer_type(request_data)
        return processed_data

    def create(self, request, *args, **kwargs):
        bulk = isinstance(request.data, list)

        if not bulk:
            data = self._cast_answer_types(request.data)
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            data = self._cast_answer_types(request.data, many=True)
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_bulk_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_bulk_create(self, serializer):
        return self.perform_create(serializer)
