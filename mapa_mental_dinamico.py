from graphviz import Digraph
g = Digraph()
#g.view()
#Node é a "caixa"
#Edge é a linha, a conexão, o ligamento
with open('estudo.txt', 'r', encoding='utf-8') as arquivo:     #Abrindo texto e lendo ele passando para a variavel "Estudo"
    estudo = arquivo.read()    #Lendo o arquiuvo e colocando na variavel estudo
if estudo != None:     
    print("Carregamento completo")      #Aqui ele dirá quando carregamento estiver completo
else:
    print("Seu texto esta vazio, revise-o")
def separaracao(texto_inicial):
    #Aqui nos iremos contar quantos tempicos
    quantidade_ponto = 0
    for caractere in range(len(texto_inicial)):     #Lendo e verificando cada letra do texto, CADA LETRA
        if texto_inicial[caractere] == ".":           #Caso a letra é um ;
            quantidade_ponto += 1             #Acrescenta na quantidade para saber quantos ; tem nesse texto( ; é a partição do texto entre os temas )
            print(quantidade_ponto)
            pass
    #Agora ta na hora da separação de fato
    mapa = {}                          #Mapa em sua forma mais crua
    restantes_ponto = quantidade_ponto
    while len(texto_inicial)-1:
        print(texto_inicial)
        letras = len(texto_inicial)
        if letras < 1:
            break
        print("Quantidade de letras: ", letras)
        for caractere in range(letras):
            if texto_inicial[caractere] == ':':          #Iniciando o topico com as letras atras sendo o nome desse topico
                atual_tema = texto_inicial[:caractere]   #Ele vai dizer em qual tema esta para no final ele adicionar os subsequentes topicos no devido tema
                mapa[texto_inicial[:caractere]] = []     #Ele cria um um novo "Table" com o nome do topico para depois liga-los no mapa mental
                texto_bruh = texto_inicial[caractere+1:] #Aqui, o texto_bruh é um placeholder do texto original sendo cortado sem o texto que ja foi pego, como se ele tivesse "agarrado e transformado em topico"
                texto_inicial = texto_bruh               #Aqui, o texto original(texto_inicial) fica com o mesmo valor do texto_bruh para ent ser o novo texto original
                print("Novo Topico:", atual_tema)        #Aqui é o DEBUG msm         
                break                                    #Aqui é quando da Break

            elif texto_inicial[caractere] == ';':                    #Adicionando um novo coiso para rechear o topico atual, muito importante que logo irá se unir 
                mapa[atual_tema].append(texto_inicial[:caractere])   #De fato adicioando o seguinte conteudo para o atual tema
                texto_bruh = texto_inicial[caractere+1:]             #Texto placeholder, cortando o conteudo ja usado do texto original
                texto_inicial = texto_bruh                           #Incorporando o novo novo texto
                print('Adicionando novo topico')                     #Aqui é DEBUG msm
                break                                                #Aqui dá o break

            elif texto_inicial[caractere] == '.':             #Aqui é quando se finaliza o atual tema, na espera de um tema novo. pode ser melhorado mas não tenho ideia por enquanto, se ta funcionando ta  bom
                texto_bruh = texto_inicial[caractere+1:]      #Texto Placeholder, cortando o conteudo etc o de sempre
                quantidade_ponto -= 1
                texto_inicial = texto_bruh                    #Incorporando o novo texto
                atual_tema = ''                               #Deixando o tema atual em aberto
                print('Finalizando topico')                   #Debug 
                break                                         #Break

            else:
                print('eita aqui não deu nada')        #Aqui é em casos de bugatinas, onde ele n entenda nenhum das condições anteriores.
    
    return mapa    #Retorna o mapa em forma de dicionario para depois ser feito em mapa visual

def criacao_mapa(mapa):
    lista_temas = list(mapa.keys())   #Transformando os nomes da lista em um conjunto, para usar logo a seguir. list(mapa.keys()) ira retornar o "nome" das casas
    for Tema in lista_temas: #Aqui ele ira separar os temas sabe, para cada tema ele ira passar por cada topico dele
        g.node(Tema)    #Aqui ele cria a "caixinha" para o item
        for conteudo in mapa[Tema]:  
            g.node(conteudo)         #Aqui ele cria a "caixinha" para o conteudo, para cada conteudo (nos vamos liga-los depois)
            g.edge(Tema, conteudo)   #Aqui ele ira criar um "Nó" entre o tema e o conteudo atual 
    g.render("mapa mental", view=True)     #No final de tudo mostrará o resultado
sucesso = separaracao(estudo)
criacao_mapa(sucesso)