from rest_framework.mixins import CreateModelMixin, UpdateModelMixin


class CompensationLogMixin(CreateModelMixin, UpdateModelMixin):
    def perform_create(self, serializer):
        serializer.save(double_entry=1)

    def perform_update(self, serializer):
        serializer.save(double_entry=2)
