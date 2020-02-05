class Dynamodb-cri():
    def __init__(self, config):
        self._config.entity = config.entity
        self._config.gsik = config.gsik
        
        if config.index_name != None:
            self._config.index_name = config.index_name

        if config.table_name != None:
            self._config.table_name = config.table_name