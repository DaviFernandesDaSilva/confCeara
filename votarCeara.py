from selenium import webdriver  # Importa o módulo webdriver do Selenium, usado para automatizar o navegador.
import time  # Importa o módulo time, utilizado para adicionar pausas no código com time.sleep().
from selenium.webdriver.chrome.service import Service  # Importa a classe Service para configurar o caminho do ChromeDriver.
from webdriver_manager.chrome import ChromeDriverManager  # Importa o ChromeDriverManager, que facilita o gerenciamento do ChromeDriver.
from selenium.webdriver.common.by import By  # Importa o By, usado para localizar elementos na página com base em seletores.
from selenium.webdriver.support.wait import WebDriverWait  # Importa WebDriverWait, utilizado para esperar elementos estarem presentes ou prontos.
from selenium.webdriver.support import expected_conditions as EC  # Importa EC (Expected Conditions), para condições de espera durante interações com o navegador.
from selenium.webdriver.common.action_chains import ActionChains  # Importa ActionChains para ações mais complexas, como arrastar e soltar ou simular vários cliques.
from selenium.webdriver.support.select import Select  # Importa Select, usado para interagir com campos de seleção (dropdowns).
from selenium import webdriver  #
from threading import Thread  # Importa Thread para possibilitar a execução de tarefas em paralelo.
from webdriver_manager.chrome import ChromeDriverManager  # Importa novamente o ChromeDriverManager, de outra fonte, previnindo erros
import random  # Importa o módulo random para gerar números ou escolhas aleatórias, mas não está sendo utilizado no código até agora.

vezes = 0  # Variável 'vezes' declarada, mas não está sendo usada neste trecho de código.

# Criação de um objeto Service com o caminho do ChromeDriver
service = Service("C:\\ChromeDriver\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")  # Caminho absoluto do ChromeDriver.
driver = webdriver.Chrome(service=service)  # Inicializa o driver do Chrome com o ChromeDriver especificado no objeto Service.

# Acessa a página de votação do site
driver.get("https://CENSURADO/CENSURADO/votacao")  # Navega até o URL de votação.

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}  
# Define um cabeçalho 'User-Agent' para emular um navegador específico, mas não está sendo utilizado em requisições HTTP no código atual.

class Votacao:  # Definindo a classe 'Votacao' para representar ações relacionadas à votação no site.
    def __init__(self):
        self.SITE_LINK = "https://CENSURADO/CENSURADO/votacao"  # URL do site de votação.
        
        self.SITE_MAP = {  # Mapeamento de XPaths para os elementos importantes da página.
            "perguntas": {  # Mapeia a pergunta "campanha".
                "campanha": {  # Mapeia o XPath da pergunta "campanha".
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/form/div[2]/h3"
                }
            },
            "buttons": {  # Mapeia os botões importantes no formulário.
                "iniciar": {  # XPath para o botão de iniciar.
                    "xpath": "/html/body/div[3]/div/div/div/div/div/div/div/form/div[1]/button[1]"
                },
                "campanha": {  # XPath para o campo de seleção da campanha.
                    "xpath": "/html/body/div[3]/div/div/div/div/div/div/form/div[7]/div/div[1]/div[2]/p/label/input"
                },
                "proxima": {  # XPath para o botão de "próxima".
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[2]/button[2]"
                },
                "nome": {  # XPath para o campo de nome.
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[1]/input"
                },
                "email": {  # XPath para o campo de e-mail.
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[2]/input"
                },
                "fone": {  # XPath para o campo de telefone.
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[3]/input"
                },
                "inst": {  # XPath para o campo de instituição.
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[4]/select"
                },
                "finalizar": {  # XPath para o botão de "finalizar".
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[5]/div/button"
                }
            }
        }
        
        self.driver = webdriver.Chrome(service=service)  # Inicializa o WebDriver novamente (potencial redundância).
        self.driver.set_window_size(640, 480)  # Define o tamanho da janela do navegador como 640x480 pixels.
        
    def abrir_site(self):  # Método para abrir o site de votação.
        time.sleep(0.1)  # Pausa de 0.1 segundos.
        self.driver.get(self.SITE_LINK)  # Acessa o link do site de votação.
        time.sleep(0.1)  # Pausa novamente após o carregamento.

    def comecar_quest(self):  # Método para iniciar a interação com o questionário.
        time.sleep(0.1)  # Pausa para garantir que o carregamento seja concluído.
        self.driver.execute_script(f"window.scrollTo(0, 0);")  # Rola a página para o topo.
        time.sleep(0.1)  # Pausa breve.
        self.driver.find_element("xpath",self.SITE_MAP["buttons"]["iniciar"]["xpath"]).click()  # Clica no botão "iniciar".
        time.sleep(0.1)  # Pausa para aguardar a resposta do clique.

    def identificar_pergunta(self):  # Método vazio, parece destinado à identificação das perguntas.
        pass
        
    def abrir_questionarios(self):  # Método para abrir questionários.
        self.driver.execute_script(f"$('.fieldset').css('display','block');")  # Executa um script para mostrar os questionários.

        
    def clicar_botao_certo(self):
    # Lista dos nomes dos botões e seus valores correspondentes
    botoes = [
        ("cat_1", "2", 0.2),
        ("cat_2", "2", 0.2),
        ("cat_3", "3", 0.1),
        ("cat_4", "2", 0.2),
        ("cat_5", "1", 0.1),
        ("cat_6", "1", 0.1),
        ("cat_7", "3", 0.2),
        ("cat_8", "3", 0.1),
        ("cat_9", "1", 0.1),
        ("cat_10", "3", 0.2),
        ("cat_11", "2", 0.1),
        ("cat_12", "1", 0.2),
        ("cat_13", "1", 0.1),
        ("cat_14", "3", 0.1),
        ("cat_15", "2", 0.1),
        ("cat_16", "1", 0.2),
        ("cat_17", "2", 0.1),
        ("cat_18", "3", 0.2),
    ]

    for nome, valor, tempo_espera in botoes:
        if self.driver.find_element(By.NAME, nome).is_displayed():
            time.sleep(tempo_espera)
            elemento = self.driver.find_element("xpath", f"//input[@type='radio' and @name='{nome}' and @value='{valor}']")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
            elemento.click()
            contadorFunc()
        else:
            print(f"{nome} INVISIVEL")


   
    def clicar_no_botao_proxima(self):
        try:
            time.sleep(1)  # Espera fixa de 1 segundo para dar tempo de carregar a página
    
            # Verificar se o botão está visível e habilitado antes de clicar
            botao_proxima = self.driver.find_element("xpath", '//button[text()="Próximo"]')
    
            # Garantir que o botão está visível e habilitado
            if botao_proxima.is_displayed() and botao_proxima.is_enabled():
                botao_proxima.click()  # Clica no botão "Próximo"
                print("Botão 'Próximo' clicado.")
            else:
                print("O botão 'Próximo' não está visível ou habilitado.")
    
        except Exception as e:
            print(f"Erro ao clicar no botão 'Próximo': {e}")
               
    def inserir_campos(self):
        # Pausa Breve
        time.sleep(0.2)

        #Pessoas pré geradas pros campos
        pessoas = [
    ["Davi F", "davipbr12@gmail.com", "(85) 99214-5555"],
    ["Bianca Ferreira", "biancaferreira@gmail.com", "(85) 99874-2233"],
    ["Gabriel Martins", "gabrielmartins@hotmail.com", "(85) 99322-7788"],
    ["Ana Souza", "anasouza@gmail.com", "(85) 99122-5584"],
    ["Carlos Pereira", "carlospereira@gmail.com", "(85) 99442-6677"],
    ["Juliana Alves", "juliana.alves@outlook.com", "(85) 99874-5566"],
    ["Roberta Costa", "roberta.costa@hotmail.com", "(85) 99753-4411"],
    ["Fernando Lima", "fernando.lima@outlook.com.br", "(85) 99553-6677"],
    ["Mariana Oliveira", "mariana.oliveira@gmail.com", "(85) 99224-7788"],
    ["Luiz Eduardo", "luiz.eduardo@hotmail.com", "(85) 99122-3344"],
    ["Bruna Mendes", "bruna.mendes@gmail.com", "(85) 99442-2211"],
    ["Ricardo Lima", "ricardolima@outlook.com", "(85) 99334-4422"],
    ["Renata Souza", "renatasouza@hotmail.com", "(85) 99845-6677"],
    ["José Pereira", "josepereira@hotmail.com", "(85) 99899-3344"],
    ["Leandro Almeida", "leandro.almeida@outlook.com", "(85) 99565-8877"],
    ["Renan Costa", "renancosta@hotmail.com", "(85) 99487-6655"],
    ["Jorge Santos", "jorge.santos@gmail.com", "(85) 99711-3322"],
    ["Maíra Pereira", "mairasantos@outlook.com", "(85) 99545-5566"],
    ["Henrique Alves", "henrique.alves@outlook.com", "(85) 99676-3344"],
    ["Paula Lima", "paulalima@hotmail.com", "(85) 99232-5544"],
    ["Patricia Souza", "patriciasouza@outlook.com", "(85) 99355-6677"],
    ["Leonardo Costa", "leocosta@gmail.com", "(85) 99733-2211"],
    ["Camila Lima", "camilalima@outlook.com", "(85) 99554-6677"],
    ["Lucas Fernandes", "lucas.fernandes@gmail.com", "(85) 99487-5566"],
    ["Ana Carolina", "anacarolina@hotmail.com", "(85) 99322-3344"],
    ["Rodrigo Almeida", "rodrigo.almeida@outlook.com", "(85) 99821-4433"],
    ["Isabela Santos", "isabelasantos@gmail.com", "(85) 99722-7788"],
    ["Marlon Lima", "marlonlima@outlook.com", "(85) 99232-5566"],
    ["Brenda Costa", "brendacosta@hotmail.com", "(85) 99476-3322"],
    ["Felipe Pereira", "felipepereira@gmail.com", "(85) 99789-4455"],
    ["Renato Mendes", "renatomendes@hotmail.com", "(85) 99322-5544"],
    ["Eduarda Fernandes", "eduardaf@gmail.com", "(85) 99465-7788"],
    ["Cristiano Lima", "cristianolima@outlook.com", "(85) 99789-3344"],
    ["Gabriel Costa", "gabriellcosta@outlook.com", "(85) 99845-8877"],
    ["Fábio Pereira", "fabio.pereira@gmail.com", "(85) 99522-4433"],
    ["Veronica Mendes", "veronicamendes@outlook.com", "(85) 99411-5566"],
    ["Thiago Almeida", "thiago.almeida@hotmail.com", "(85) 99765-7788"],
    ["Rebeca Costa", "rebecacosta@gmail.com", "(85) 99876-6677"],
    ["Luis Fernandes", "luis.fernandes@outlook.com", "(85) 99322-3344"],
    ["Manoel Oliveira", "manoel.oliveira78@outlook.com", "(85) 93252-6203"],
    ["Daniel Santos", "daniel.santos85@hotmail.com", "(85) 96970-6768"],
    ["Sergio Peixoto", "sergio.peixoto82@hotmail.com", "(85) 94042-2225"],
    ["Rodrigo Freitas", "rodrigo.freitas87@hotmail.com", "(85) 97549-3541"],
    ["Fabio Pereira", "fabio.pereira60@gmail.com", "(85) 93067-7465"],
    ["Ivan Lima", "ivan.lima30@hotmail.com", "(85) 97149-3231"],
    ["Andre Machado", "andre.machado33@gmail.com", "(85) 95585-2819"],
    ["Ricardo Cardoso", "ricardo.cardoso34@outlook.com", "(85) 98894-4165"],
    ["Rodrigo Azevedo", "rodrigo.azevedo87@outlook.com", "(85) 93373-1257"],
    ["Rodrigo Melo", "rodrigo.melo62@outlook.com.br", "(85) 93511-6275"],
    ["Vinicius Lima", "vinicius.lima21@hotmail.com", "(85) 92098-1456"],
    ["Fernando Martins", "fernando.martins52@outlook.com", "(85) 95213-6354"],
    ["Marcelo Dias", "marcelo.dias49@gmail.com", "(85) 94821-7745"],
    ["Rafael Oliveira", "rafael.oliveira10@outlook.com.br", "(85) 93289-3776"],
    ["Pedro Alves", "pedro.alves38@outlook.com", "(85) 95320-4622"],
    ["Joao Souza", "joao.souza46@hotmail.com", "(85) 94112-6351"],
    ["Leonardo Fernandes", "leonardo.fernandes69@gmail.com", "(85) 96002-8583"],
    ["Carlos Goncalves", "carlos.goncalves11@outlook.com.br", "(85) 94568-7192"],
    ["Eduardo Melo", "eduardo.melo88@hotmail.com", "(85) 98742-3231"],
    ["Felipe Lima", "felipe.lima30@outlook.com", "(85) 97756-1458"],
    ["Mauricio Santos", "mauricio.santos79@gmail.com", "(85) 94401-6688"],
    ["Victor Almeida", "victor.almeida26@outlook.com.br", "(85) 97119-9075"],
    ["Renato Costa", "renato.costa34@gmail.com", "(85) 95329-7756"],
    ["Lucas Barbosa", "lucas.barbosa60@hotmail.com", "(85) 97455-9912"],
    ["Jonathan Martins", "jonathan.martins87@outlook.com", "(85) 95367-8554"],
    ["Gustavo Silva", "gustavo.silva25@hotmail.com", "(85) 94673-5043"],
    ["Thiago Mendes", "thiago.mendes18@outlook.com", "(85) 96809-2365"],
    ["Ricardo Nunes", "ricardo.nunes48@gmail.com", "(85) 97721-5690"],
    ["Heitor Costa", "heitor.costa15@outlook.com", "(85) 96765-8195"],
    ["Henrique Araujo", "henrique.araujo57@gmail.com", "(85) 98345-7239"],
    ["Gabriel Teixeira", "gabriel.teixeira19@outlook.com", "(85) 92465-2548"],
    ["Caio Andrade", "caio.andrade13@hotmail.com", "(85) 97304-8531"],
    ["Rui Figueiredo", "rui.figueiredo27@outlook.com.br", "(85) 95129-9133"],
    ["Hugo Pinto", "hugo.pinto96@hotmail.com", "(85) 94513-7469"],
    ["Manoel Gomes", "manoel.gomes77@outlook.com", "(85) 95654-6027"],
    ["Artur Carvalho", "artur.carvalho81@gmail.com", "(85) 94203-9512"],
    ["Bernardo Sousa", "bernardo.sousa20@outlook.com.br", "(85) 95247-5338"],
    ["Samuel Tavares", "samuel.tavares39@outlook.com", "(85) 96320-2670"],
    ["Sandro Ribeiro", "sandro.ribeiro47@gmail.com", "(85) 95681-4897"],
    ["Luiz Eduardo", "luiz.eduardo58@outlook.com.br", "(85) 94302-8917"],
    ["Rafael Mendes", "rafael.mendes76@hotmail.com", "(85) 92112-4732"],
    ["Julio Vieira", "julio.vieira82@gmail.com", "(85) 98233-5839"],
    ["Marcelo Rocha", "marcelo.rocha29@outlook.com", "(85) 95094-3728"],
    ["Vitor Mendes", "vitor.mendes94@hotmail.com", "(85) 92654-8381"],
    ["Alex Silva", "alex.silva67@outlook.com", "(85) 92742-4233"],
    ["Adriano Dias", "adriano.dias19@gmail.com", "(85) 92204-7519"],
    ["Rodrigo Cunha", "rodrigo.cunha88@outlook.com.br", "(85) 93958-1825"],
    ["Guilherme Ribeiro", "guilherme.ribeiro90@hotmail.com", "(85) 94400-6784"],
    ["Carlos Mendes", "carlos.mendes23@outlook.com", "(85) 93519-6470"],
    ["Fabricio Monteiro", "fabricio.monteiro40@gmail.com", "(85) 96502-3398"],
    ["Douglas Cruz", "douglas.cruz93@outlook.com.br", "(85) 94754-4928"],
    ["Cesar Pereira", "cesar.pereira81@gmail.com", "(85) 97892-3259"],
    ["Marcos Lima", "marcos.lima31@outlook.com", "(85) 95307-1839"],
    ["Davi Sousa", "davi.sousa75@hotmail.com", "(85) 96481-7264"],
    ["Jorge Nascimento", "jorge.nascimento38@outlook.com", "(85) 97795-5214"],
    ["Caio Almeida", "caio.almeida14@outlook.com.br", "(85) 92587-9104"],
    ["Rogerio Santos", "rogerio.santos62@hotmail.com", "(85) 96547-2368"],
    ["Paulo Barbosa", "paulo.barbosa84@outlook.com", "(85) 94876-2046"],
    ["Francisco Melo", "francisco.melo18@outlook.com.br", "(85) 93754-9738"],
    ["Elias Azevedo", "elias.azevedo92@gmail.com", "(85) 93285-7169"],
    ["Fernando Souza", "fernando.souza25@outlook.com", "(85) 97603-4498"],
    ["Pedro Martins", "pedro.martins34@gmail.com", "(85) 96721-8540"],
    ["Lucas Leal", "lucas.leal29@outlook.com", "(85) 93458-9267"],
    ["Igor Rocha", "igor.rocha11@hotmail.com", "(85) 92390-6725"],
    ["Claudio Gomes", "claudio.gomes88@outlook.com.br", "(85) 94729-5741"],
    ["Edson Cardoso", "edson.cardoso17@gmail.com", "(85) 95143-3874"],
    ["Felipe Torres", "felipe.torres94@hotmail.com", "(85) 97713-8753"],
    ["Miguel Correia", "miguel.correia53@outlook.com", "(85) 96237-4452"],
    ["Fabricio Xavier", "fabricio.xavier46@outlook.com.br", "(85) 92678-9036"],
    ["Wilton Ramos", "wilton.ramos78@gmail.com", "(85) 95674-1023"],
    ["Alexandre Melo", "alexandre.melo35@outlook.com", "(85) 93012-6754"],
    ["Eduardo Nunes", "eduardo.nunes40@hotmail.com", "(85) 95764-3890"],
    ["Flavio Rodrigues", "flavio.rodrigues93@outlook.com.br", "(85) 93850-1423"],
    ["Jose Moura", "jose.moura85@outlook.com", "(85) 96240-7359"],
    ["Renan Pinto", "renan.pinto82@gmail.com", "(85) 92105-5160"],
    ["Erick Faria", "erick.faria12@hotmail.com", "(85) 94924-3128"],
    ["Leandro Lima", "leandro.lima55@outlook.com.br", "(85) 98130-2247"],
    ["Igor Lopes", "igor.lopes16@hotmail.com", "(85) 93471-5869"],
    ["Adriel Rodrigues", "adriel.rodrigues40@outlook.com", "(85) 96392-6731"],
    ["Alex Costa", "alex.costa97@outlook.com", "(85) 94703-8935"],
    ["David Gomes", "david.gomes62@gmail.com", "(85) 96411-9297"],
    ["Cleber Nunes", "cleber.nunes19@hotmail.com", "(85) 92971-8583"],
    ["Osvaldo Macedo", "osvaldo.macedo38@outlook.com", "(85) 94826-1062"],
    ["Jean Santos", "jean.santos45@gmail.com", "(85) 93290-3286"],
    ["Anderson Dias", "anderson.dias78@hotmail.com", "(85) 92023-4369"],
    ["Julio Cesar", "julio.cesar96@outlook.com.br", "(85) 95631-8198"],
    ["Mauricio Almeida", "mauricio.almeida74@gmail.com", "(85) 95219-6710"],
    ["Nelson Tavares", "nelson.tavares11@outlook.com", "(85) 97673-1825"],
    ["Marcelo Braga", "marcelo.braga84@hotmail.com", "(85) 97243-8012"],
    ["Everton Moreira", "everton.moreira33@outlook.com", "(85) 93481-6297"],
    ["Camila Lima", "camila.lima54@outlook.com", "(85) 95763-2456"],
    ["Bianca Rocha", "bianca.rocha28@gmail.com", "(85) 97511-6732"],
    ["Fernanda Nunes", "fernanda.nunes77@hotmail.com", "(85) 92351-4576"],
    ["Juliana Ribeiro", "juliana.ribeiro12@outlook.com.br", "(85) 96602-8364"],
    ["Aline Sousa", "aline.sousa18@outlook.com", "(85) 93218-4359"],
    ["Vanessa Costa", "vanessa.costa93@hotmail.com", "(85) 94026-5918"],
    ["Renata Lima", "renata.lima37@outlook.com.br", "(85) 92963-7184"],
    ["Mariana Figueiredo", "mariana.figueiredo60@gmail.com", "(85) 92248-3716"],
    ["Clara Freitas", "clara.freitas83@outlook.com", "(85) 94429-7835"]
]
        # Gera um índice aleatório para selecionar uma pessoa da lista 'pessoas'
        indice_random = random.randint(0, len(pessoas) - 1)
        
        # Acessa os dados da pessoa escolhida com base no índice gerado
        nameF, emailF, foneF = pessoas[indice_random]
        
        # Preenche o campo de Nome com o valor gerado aleatoriamente
        name_element = self.driver.find_element("xpath", self.SITE_MAP["buttons"]["nome"]["xpath"])
        ActionChains(self.driver).send_keys_to_element(name_element, nameF).perform()
        
        # Aguarda um breve momento antes de preencher o próximo campo
        time.sleep(0.2)
        
        # Preenche o campo de Email com o valor gerado aleatoriamente
        email_element = self.driver.find_element("xpath", self.SITE_MAP["buttons"]["email"]["xpath"])
        ActionChains(self.driver).send_keys_to_element(email_element, emailF).perform()
        
        # Aguarda um breve momento antes de preencher o próximo campo
        time.sleep(0.2)
        
        # Preenche o campo de Telefone com o valor gerado aleatoriamente
        fone_element = self.driver.find_element("xpath", self.SITE_MAP["buttons"]["fone"]["xpath"])
        ActionChains(self.driver).send_keys_to_element(fone_element, foneF).perform()
        
        # Aguarda um breve momento antes de preencher o próximo campo
        time.sleep(0.2)
        
        # Preenche o campo de Instituição com o valor "Torcedor" no campo de seleção
        select_element = self.driver.find_element("xpath", self.SITE_MAP["buttons"]["inst"]["xpath"])
        select = Select(select_element)
        select.select_by_value('Torcedor')

    
    def confirmar_votacao(self):
        # Pausa rápida antes de clicar no botão de finalizar
        time.sleep(0.1)
        # Encontra o botão de finalizar votação e clica nele
        self.driver.find_element("xpath",self.SITE_MAP["buttons"]["finalizar"]["xpath"]).click()
        time.sleep(0.2)
        # Aceita o alerta de confirmação de finalização
        self.driver.switch_to.alert.accept()
        time.sleep(0.1)
    
    def rodar_indefinidamente(self):
        # Loop infinito que executa as ações continuamente
        while True:  
            # Executa o início do questionário
            self.comecar_quest()
            # Abre os questionários disponíveis
            self.abrir_questionarios()
            # Clica no botão correto para avançar
            self.clicar_botao_certo()
            # Preenche os campos necessários
            self.inserir_campos()
            # Confirma a votação
            self.confirmar_votacao()
            time.sleep(1)  # Pausa de 1 segundo entre as ações, ajustável conforme necessário
    
    def set_tamanho_tela(self, largura, altura):
        """Define o tamanho da janela do navegador"""
        self.driver.set_window_size(largura, altura)
    
    def iniciar_votacao_em_janela():
        # Cria uma instância de Votacao e inicia o processo
        votar = Votacao()
        votar.abrir_site()  # Abre o site da votação
        votar.set_tamanho_tela(600, 300)  # Define o tamanho da janela
        votar.rodar_indefinidamente()  # Inicia o loop infinito para rodar as ações
    
    def votacaoFinalizada():
        # Imprime uma mensagem quando a votação é finalizada
        print(f"Votação Finalizada")
    
    def contador():
        # Função que mantém e incrementa um contador para as votações finalizadas
        count = 0  # Inicializa o contador de votações finalizadas
        
        def incrementar():
            nonlocal count  # Usa a variável count da função externa
            count += 1  # Incrementa o contador
            print(f"Votações Finalizadas: {count}")  # Exibe o número de votações finalizadas
            
        return incrementar  # Retorna a função que pode ser chamada para incrementar o contador


contador_func = contador()  # Cria uma instância do contador

# Criação de várias janelas para rodar a votação simultaneamente
num_janelas = 10  # Número de janelas a serem abertas simultaneamente
threads = []  # Lista para armazenar as threads

largura_da_tela = 300  # Define a largura da janela
altura_da_tela = 500  # Define a altura da janela

espaco_entre_janelas = 50  # Define o espaço entre as janelas abertas

for i in range(num_janelas):
    # Calcula a posição X de cada janela para que não se sobreponham
    posicao_x = i * (largura_da_tela + espaco_entre_janelas)
    posicao_y = 0  # Mantém a posição Y fixada para todas as janelas
    # Cria e inicia uma nova thread para cada janela de votação
    t = Thread(target=iniciar_votacao_em_janela)
    threads.append(t)  # Adiciona a thread à lista
    t.start()  # Inicia a thread

