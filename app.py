from flask import Flask, render_template
from restaurante import Restaurante
from especialista import Especialista
from comentario import Comentario

app = Flask(__name__)

lista_especialista = [
Especialista(1,"Pedro"),
Especialista(2,"Joana"),
Especialista(3,"Paulo"),
Especialista(4,"Luisa"),
Especialista(5,"Alex"),  
Especialista(6,"Mariana")      
]

lista_comentario = [
Comentario(1,"Ta Caro",[lista_especialista[0]],"https://img.icons8.com/material-outlined/344/popular-man.png"),
Comentario(2,"Demora Muito",[lista_especialista[1]],"https://img.icons8.com/material-outlined/344/popular-man.png"),
Comentario(3,"Muito bom",[lista_especialista[2]],"https://img.icons8.com/material-outlined/344/popular-man.png"),
Comentario(4,"Lugar Agradavel",[lista_especialista[3]],"https://img.icons8.com/material-outlined/344/popular-man.png"), 
Comentario(5,"Bons Preços",[lista_especialista[4]],"https://img.icons8.com/material-outlined/344/popular-man.png"), 
Comentario(6,"Comida de Qualidade",[lista_especialista[5]],"https://img.icons8.com/material-outlined/344/popular-man.png"), 

]

lista_restaurante = [
Restaurante(1,"Sabor do Vale", "https://scontent.fsdu10-1.fna.fbcdn.net/v/t1.18169-9/29513205_1855071094567904_6126652539344614528_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=8DRp28aCg34AX8mq2fD&_nc_ht=scontent.fsdu10-1.fna&oh=00_AT9_mx4XH7MoE129fEt3CyyDWuuuFnIRNYL7XGN9AjTAzg&oe=627C8940" ,"Rua Caetano Furquin 105 27700000 Vassouras, RJ","10:30 às 16:00",[lista_comentario[0],lista_comentario[1]],"https://www.facebook.com/1847203468688000/videos/792004804942525"),
Restaurante(2,"Restaurante Varandas", "https://scontent.fsdu10-1.fna.fbcdn.net/v/t1.18169-9/28058689_1689020627830323_4223215194561322128_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=vR1kymINaW0AX-UQhak&_nc_ht=scontent.fsdu10-1.fna&oh=00_AT-f1fYpSy4Rh3PM5eOdUGS-pg1w3mtITJtrhpEyTg-7sw&oe=627C6490" ,"Avenida Expedicionário Oswaldo de Almeida Ramos 110 Centro 27700-000 Vassouras, RJ" ,"11:00 às 00:00",[lista_comentario[2],lista_comentario[3]],"https://www.facebook.com/rede.varandas/videos/3517690498296651/"),
Restaurante(3,"Sabor na Brasa", "https://scontent.fsdu10-1.fna.fbcdn.net/v/t1.6435-9/64875039_463912220845381_657631974885687296_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=v4as14lZjqYAX_lRIYW&_nc_ht=scontent.fsdu10-1.fna&oh=00_AT_wbRgkU-UbJIpjKe3iYTxOESygDkDN01q1mVE3bzpPSg&oe=627C378C","Rua Fernando Pedrosa Fernandes N° 132 27700000 Barão de Vassouras, RJ","18:30 às 23:30",[lista_comentario[4],lista_comentario[5]],"https://www.facebook.com/371878023382135/videos/910700339499898")
]

@app.route('/')
def home():
    return render_template("index.html" , restaurantes = lista_restaurante)

@app.route('/restaurante/<string:nome>')
def exibir_Restaurante(nome):
    for restaurante in lista_restaurante:
        if restaurante.get_nomeRestaurante() == nome:
            return render_template("restaurante.html" , restaurante = restaurante)
    return render_template("index.html" , restaurantes = lista_restaurante)

if __name__ == "__main__":
    app.run()