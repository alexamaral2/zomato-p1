class Especialista:
    
    def __init__(self,idEspecialista, nomeEspecialista):
        self.__idEspecialista = idEspecialista
        self.__nomeEspecialista = nomeEspecialista

    def get_idEspecialista(self):
        return self.__idEspecialista

    def get_nomeEspecialista(self):
        return self.__nomeEspecialista        