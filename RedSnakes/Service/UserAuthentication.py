class UserAuthentication:
    def __init__(self, service, userManagement):
        self.__service = service
        self.__userManagement = userManagement

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, value):
        self.__service = value

    @property
    def userManagement(self):
        return self.__userManagement

    @userManagement.setter
    def userManagement(self, value):
        self.__userManagement = value
