from controller.Controller import Controller
from domain.Payload import Payload
from repo.Repository import Repository
from service.Service import Service

if __name__ == '__main__':
    repository = Repository(None)
    service = Service(repository)
    controller = Controller(service)
