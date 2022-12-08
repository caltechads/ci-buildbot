import os

import docker

from ..typedefs import MessageContext
from .base import AbstractContextProcessor


class DockerImageNameProcessor(AbstractContextProcessor):

    def __init__(self, **kwargs):
        self.image: str = kwargs['image']

    def annotate(self, context: MessageContext) -> None:
        context['short_image'] = os.path.basename(self.image)


class DockerProcessor(AbstractContextProcessor):

    def __init__(self, **kwargs):
        self.image: str = kwargs['image']

    def annotate(self, context: MessageContext) -> None:
        client = docker.from_env()
        image = client.images.get(self.image)
        context['image_id'] = image.short_id.split(':')[1]
        context['image_size'] = image.attrs['Size'] / (1024 * 1024)
