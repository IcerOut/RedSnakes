class ConferencePaperManagement:
    def __init__(self, service):
        self.__service = service

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, value):
        self.__service = value
