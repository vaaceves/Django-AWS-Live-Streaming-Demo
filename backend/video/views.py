from django_chunk_upload.views import (
    ChunkUploadView,
    ChunkUploadCompleteView
)
from video.models import ChunkUpload


class ChunkUploadView(ChunkUploadView):
    model = ChunkUpload
    field_name = 'video'

    def check_permissions(self, request):
        # Allow non authenticated users to make uploads
        pass


class ChunkUploadCompleteView(ChunkUploadCompleteView):
    model = ChunkUpload

    def check_permissions(self, request):
        # Allow non authenticated users to make uploads
        pass

    def on_completion(self, uploaded_file, request):
        # Do something with the uploaded file. E.g.:
        # * Store the uploaded file on another model:
        # SomeModel.objects.create(user=request.user, file=uploaded_file)
        # * Pass it as an argument to a function:
        # function_that_process_file(uploaded_file)
        pass

    def get_response_data(self, chunk_upload, request):
        return {'message': ("You successfully uploaded '%s' (%s bytes)!" %
                            (chunk_upload.filename, chunk_upload.offset))}
