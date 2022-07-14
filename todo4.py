'''
Uma empresa recebeu muitos currículos para determinadas vagas e agora precisa classificar quantos candidatos tem o perfil necessário e quantos candidatos estão concorrendo a cada vaga. 

Desenvolva um projeto (usando dicionários) que vai gravar a quantidade de currículos para cada vaga e quantas pessoas têm pelo menos uma das palavras chaves necessárias no currículo. Para isso, nosso código Python vai checar quantos candidatos estão se inscrevendo, para qual vaga, nome do candidato e um resumo que a pessoa está enviando.

Usar as palavras chaves a seguir para cada vaga. Nosso código deve perguntar: quantos candidatos serão cadastrados; qual o nome do candidato; para qual vaga está se inscrevendo; e um pequeno texto com o resumo do currículo do participante;
Vaga Analista de dados com as palavras chaves: Python, PowerBI, SQL, Boa comunicação
Vaga Cientista de dados com as palavras chaves: Python, Banco de dados, Machine Learning, Resolução De Problemas, Estatística


O texto do resumo vai ser informado pelo usuário e então vamos verificar se pelo menos uma palavra chave da vaga está presente no resumo enviado pelo candidato

Ao final, nosso código deve mostrar como saída: quantas pessoas estão inscritas em cada vaga; e quantas pessoas tem o resumo com as palavras que estamos buscando.

Desafio extra 1: entregar o link do Github com os commits devidamente documentados

Desafio extra 2: ler os resumos a partir de arquivos txt em uma pasta 
Dica: Ficará incrível se quiserem usar os próprios currículos! 
'''

analista_de_dados = ['python', 'powerbi', 'sql', 'boacomunicacao']
cientista_de_dados = ['python', 'bancodedados', 'machinelearning', 'resolucaodeproblemas', 'estatistica']
candidatos_cadastrados = {}

def menu():
    while True:
        opcao = str(input(
            f'\nOlá, selecione o que deseja:\n[1] - Cadastrar candidatos(as)\n[2] - Sair\n'))
        if opcao == '1':
            cadastrar_candidato()
        elif opcao == '2':
            exit()
        else:
            print('\nEscolha uma das opções informadas:\n')

def cadastrar_candidato():
    candidatos_analista = candidatos_cientista = match_analista = match_cientista = 0
    quantidade_candidatos = int(input('\nQuantos candidatos(as) você deseja cadastrar?\n'))
    for i in range(quantidade_candidatos):
        candidato_nome = input(f'\nDigite o nome do(a) {i+1}º candidato(a):\n')
        pergunta_resumo = input('\nVocê gostaria de digitar o resumo ou passar o nome do arquivo?\n[1] - Digitar resumo.\n[2] - Digitar nome do arquivo.\n')
        if pergunta_resumo == '1':
            resumo = limpar_resumo(input('\nDigite o resumo do(a) candidato(a) com as palavras-chaves separadas por virgula:\n'))
        elif pergunta_resumo == '2':
            nome_arquivo = input('\nDigite o nome do arquivo com .txt no final: \n')
            with open(nome_arquivo) as f:
                resumo = f.read()
                resumo = limpar_resumo(resumo)
        else:
            resumo = ''
        vaga = input('\nPara qual vaga ele(a) está inscrevendo?\n[1] - Analista de dados\n[2] - Cientista de dados\n')
        if vaga == '1':
            candidatos_analista += 1
            for termo in analista_de_dados:
                if termo in resumo:
                    match_analista += 1
                    break
        elif vaga == '2':
            candidatos_cientista += 1
            for termo in cientista_de_dados:
                if termo in resumo:
                    match_cientista += 1
                    break
        else:
            print("\nEscolha uma das opções informadas:\n")
    print(f'\n{candidatos_analista} se candidataram para a vaga de analista de dados\n{candidatos_cientista} se candidataram para a vaga de cientista de dados\ne um total de {match_analista + match_cientista} deram matchs com o resumo.\n')

def limpar_resumo(resumo):
    return resumo.replace(' ','').lower().split(',')

