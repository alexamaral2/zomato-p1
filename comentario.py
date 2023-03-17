class Comentario:
    def __init__ (self, idComentario , comentario , especialista,imgComentario):
        self.__idComentario = idComentario
        self.__comentario = comentario
        self.__especialista = especialista 
        self.__imgComentario = imgComentario

    def get_idComentario(self):
        return self.__idComentario
    
    def get_comentario(self):
        return self.__comentario
    
    def get_especialista(self):
        return self.__especialista

    def get_imgComentario(self):
        return self.__imgComentario