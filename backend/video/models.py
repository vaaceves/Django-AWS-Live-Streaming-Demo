from django_chunk_upload.models import ChunkUpload


class ChunkUpload(ChunkUpload):
    pass


# Override the default ChunkUpload to make the `user` field nullable
ChunkUpload._meta.get_field('user').null = True
