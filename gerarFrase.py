# ler a frase original e substituir uma palavra por alguma aleatoria da lista
from random import randint

def gerar_frase():
    frase.clear()
    garcom = apelidos[randint(0, (len(apelidos) - 1))] #
    resto = restos[randint(0, (len(restos) - 1))]
    layout = ["Ô", garcom, resto] # você pode inserir quantos itens quiser nessa lista, basta inserir o dado na 
    # posição que você deseja que ele apareça no output
    frase.extend(layout)
    frase_nova = " ".join(frase)
    return frase_nova


# frase = ['Ô', 'meu lindo', 'da uma chegada aqui fazendo favor']
frase = list()
apelidos = ['maestro', 'chefia', 'chefe', 'meu rei', 'meu principe', 'meu galo', 'meu lindo', 'professor',
            'meu querido', 'amigão', 'cabeludo', 'meu gato', 'joe', 'galego', 'feio', 'abençoado', 'irmão', 'guerreiro']
            
restos = ["da uma chegada aqui fazendo favor", "to te chamando ha um tempao cara ta surdo porra kkkkkk",
          "ta certo esses 20% de gorjeta aqui?", "me arranja a comanda ai fazendo o favor",
          "é crebito... é dredito... é derbito... É DREBEN... tel", "embrulha que eu vo leva",
          "tem desconto se toma mais de 5?", "quanto ta a gelada mais barata aí?",
          "ta bem gelada essa coquinha aí em?", "posso pedi uma musica?", "faz fiado pra morador?",
          "acho q tem algum erro nessa comanda aqui",
          "entrega esse bilhetinho pra moça daquela mesa ali por favor", 'é aniversario do meu amigo aqui']