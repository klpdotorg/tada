from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin

from schools.models import CompensationAuditLog


class CompensationLogMixin(CreateModelMixin, UpdateModelMixin):
    def perform_create(self, serializer):
        serializer.save(double_entry=1)

    def perform_update(self, serializer):
        serializer.save(double_entry=2)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        self.calculate_and_log_change(instance, serializer.data)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def calculate_and_log_change(self, instance, data):
        if data.get('answer_score', None):
            self.calculate_answer_score(instance, data)
        elif data.get('answer_grade', None):
            self.calculate_answer_grade(instance, data)
        else:
            raise APIException('Please enter an answer_score or answer_grade')
        
    def calculate_answer_grade(self, instance, data):
        original_value = instance.answer_grade
        new_value = data.get('answer_grade')

        if original_value == new_value:
            pass
        if not (instance.answer_grade in ['', None]):
            pass


    def calculate_answer_score(self, instance, data):
        pass
