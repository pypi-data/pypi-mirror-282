class eventObject:
    requiredParameters = ['gebeurteniscode', 'actiecode', 'utcisodatetime', 'aard']
    def __init__(self, **eventParameters) -> None:
        for param in self.requiredParameters:
            if param not in list(eventParameters.keys()):
                raise KeyError(f"Missing required parameter: {param}")
            setattr(self, param, eventParameters[param])

class userObject:
    requiredParameters = ['gebruikersnaam', 'gebruikersrol', 'identificatortype', 'identificator', 'autorisatieprotocol', 'weergave_gebruikersnaam']
    def __init__(self, **userParameters) -> None:
        for param in self.requiredParameters:
            if param not in userParameters:
                raise KeyError(f"Missing required parameter: {param}")
            setattr(self, param, userParameters[param])

class customObject:
    def __init__(self, **customParameters) -> None:
        for param in customParameters:
            setattr(self, param, customParameters[param])


if __name__ == '__main__':
    custom = customObject()
