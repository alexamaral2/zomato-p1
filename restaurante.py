class Restaurante:
    
    def __init__(self,idRestaurante, nomeRestaurante, fotoRestaurante, enderecoCompleto ,horarioFuncionamento, comentario, videoRestaurante):
        self.__idRestaurante = idRestaurante
        self.__nomeRestaurante = nomeRestaurante
        self.__fotoRestaurante = fotoRestaurante
        self.__enderecoCompleto = enderecoCompleto
        self.__horarioFuncionamento = horarioFuncionamento
        self.__comentario = comentario
        self.__videoRestaurante = videoRestaurante

    def get_idRestaurante(self):
        return self.__idRestaurante
        
    def get_nomeRestaurante(self):
        return self.__nomeRestaurante
        
    def get_fotoRestaurante(self):
        return self.__fotoRestaurante
        
    def get_enderecoCompleto(self):
        return self.__enderecoCompleto
    
    def get_horarioFuncionamento(self):
        return self.__horarioFuncionamento
    
    def get_comentario(self):
        return self.__comentario
    
    def get_videoRestaurante(self):
        return self.__videoRestaurante
        
#lista_restaurante = [
#Restaurante(1,"Bom-Gosto", "" ,"Rua xxxxxxxxxxxxxxx","9hrs as 18hrs","Comentario"),
#Restaurante(2,"Beira-Rio", "" ,"Rua xxxxxxxxxxxxxxx" ,"9hrs as 18hrs","Comentario"),
#Restaurante(3,"Bom-Aperitivo", "" ,"Rua xxxxxxxxxxxxxxx","9hrs as 18hrs","Comentario"),
#Restaurante(4,"Três Marias", "" ,"Rua xxxxxxxxxxxxxxx","9hrs as 18hrs","Comentario"),
#Restaurante(5,"Quero Mais", "" ,"Rua xxxxxxxxxxxxxxx","9hrs as 18hrs","Comentario")]
#
#for lista in lista_restaurante:
#    print(lista.get_nomeRestaurante())