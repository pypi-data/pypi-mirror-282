from typing import Type
from kameleoon.network.services.service import Service


class ServiceInitializeContext:
    def set_service(self, service_type: Type[Service], service: Service):
        raise NotImplementedError()
