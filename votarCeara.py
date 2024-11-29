from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver .support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from threading import Thread
from webdriver_manager.chrome import ChromeDriverManager
import random

vezes = 0;


# Crie um objeto Service com o caminho do ChromeDriver
service = Service("C:\\ChromeDriver\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Acessar o WhatsApp Web
driver.get("https://confutnordeste.com.br/premiacoes/votacao")

#url = 'https://confutnordeste.com.br/votacao'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

#site = requests.get(url, headers=headers)
#soup = BeautifulSoup(site.content, 'html.parser')

class Votacao:
    def __init__(self):
        self.SITE_LINK = "https://confutnordeste.com.br/premiacoes/votacao"
        
        self.SITE_MAP = {
            "perguntas": {
                "campanha":{
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/form/div[2]/h3"
                }
            },
            "buttons": {
                "iniciar":{
                    "xpath": "/html/body/div[3]/div/div/div/div/div/div/div/form/div[1]/button[1]"
                },
                "campanha":{
                    "xpath": "/html/body/div[3]/div/div/div/div/div/div/form/div[7]/div/div[1]/div[2]/p/label/input"
                },
                "proxima":{
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[2]/button[2]"
                },
                "nome":{
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[1]/input"
                },
                "email":{
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[2]/input"
                },
                "fone":{
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[3]/input"
                },
                "inst":{
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[4]/select"
                },
                "finalizar":{
                    "xpath":"/html/body/div[3]/div/div/div/div/div/div/div/form/div[20]/div[1]/div[5]/div/button"
                }
            }
        }
        
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(640, 480)
        #self.driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe")
        
        
    def abrir_site(self):
        time.sleep(0.1)
        self.driver.get(self.SITE_LINK)
        time.sleep(0.1)

    def comecar_quest(self):
        time.sleep(0.1)
        self.driver.execute_script(f"window.scrollTo(0, 0);")
        time.sleep(0.1)
        self.driver.find_element("xpath",self.SITE_MAP["buttons"]["iniciar"]["xpath"]).click()
        time.sleep(0.1)

    def identificar_pergunta(self):

        pass
        
    def abrir_questionarios(self):
        self.driver.execute_script(f"$('.fieldset').css('display','block');")
        
    def clicar_botao_certo(self):

        button1 = self.driver.find_element(By.NAME, "cat_1").is_displayed()
        button2 = self.driver.find_element(By.NAME, "cat_2").is_displayed()
        button3 = self.driver.find_element(By.NAME, "cat_3").is_displayed()
        button4 = self.driver.find_element(By.NAME, "cat_4").is_displayed()
        button5 = self.driver.find_element(By.NAME, "cat_5").is_displayed()
        button6 = self.driver.find_element(By.NAME, "cat_6").is_displayed()
        button7 = self.driver.find_element(By.NAME, "cat_7").is_displayed()
        button8 = self.driver.find_element(By.NAME, "cat_8").is_displayed()
        button9 = self.driver.find_element(By.NAME, "cat_9").is_displayed()
        button10 = self.driver.find_element(By.NAME, "cat_10").is_displayed()
        button11 = self.driver.find_element(By.NAME, "cat_11").is_displayed()
        button12 = self.driver.find_element(By.NAME, "cat_12").is_displayed()
        button13 = self.driver.find_element(By.NAME, "cat_13").is_displayed()
        button14 = self.driver.find_element(By.NAME, "cat_14").is_displayed()
        button15 = self.driver.find_element(By.NAME, "cat_15").is_displayed()
        button16 = self.driver.find_element(By.NAME, "cat_16").is_displayed()
        button17 = self.driver.find_element(By.NAME, "cat_17").is_displayed()
        button18 = self.driver.find_element(By.NAME, "cat_18").is_displayed()
        actions = ActionChains(self.driver)

        if button1 is True:
            #print("Cat_1 VISIVEL")
            time.sleep(0.2)
            button1element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_1' and @value='2']")

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button1element)
            self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_1' and @value='2']").click()


        else:
            print("Cat_1 INVISIVEL")

        if button2 is True:
            #print("Cat_2 VISIVEL")
            time.sleep(0.2)
            button2element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_2' and @value='2']")

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button2element)
            self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_2' and @value='2']").click()

        else:
            print("Cat_2 INVISIVEL")

        # if button3 is True:
        #     #print("Cat_3 VISIVEL")
        #     time.sleep(0.1)
        #     button3element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_3' and @value='3']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button3element)
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='0']"))
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='0']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_3' and @value='3']").click()
        #     #Valor 0
        # else:
        #     print("Cat_3 INVISIVEL")

        # MENOS TELA MAIS ESPORTE CAT_4
        if button4 is True:
            #print("Cat_4 VISIVEL")
            time.sleep(0.2)
            button4element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_4' and @value='2']")

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button4element)
            self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_4'  and @value='2']").click()
        else:
            print("Cat_4 INVISIVEL")

        # if button5 is True:
        #     #print("Cat_5 VISIVEL")
        #     time.sleep(0.1)
        #     #Valor 2
        #     button5element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_5' and @value='1']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button5element)
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='2']"))
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='2']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_5' and @value='1']").click()
        # else:
        #     print("Cat_5 INVISIVEL")

    # DOAR É JOGAR JUNTO CAT_6
        # if button6 is True:
        #     #print("Cat_6 VISIVEL")
        #     time.sleep(0.1)
        #     button6element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_6' and @value='1']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button6element)
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_6' and @value='1']").click()
        # else:
        #     print("Cat_6 INVISIVEL")        

        if button7 is True:
            #print("Cat_7 VISIVEL")
            time.sleep(0.2)
            button7element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_7' and @value='3']")

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button7element)
            self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_7' and @value='3']").click()
        else:
            print("Cat_7 INVISIVEL")     

        # if button8 is True:
        #     #print("Cat_8 VISIVEL")
        #     time.sleep(0.1)
        #     button8element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_8' and @value='3']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button8element)
        #     #Valor 0
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='0']")).click(self.driver).perform()
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='0']"))
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_8' and @value='3']").click()
        # else:
        #     print("Cat_8 INVISIVEL")     

        # if button9 is True:
        #     #print("Cat_9 VISIVEL")
        #     time.sleep(0.1)
        #     button9element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_9' and @value='1']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button9element)
        #     #Valor 2 ( Not Ceará )
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='2']"))
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='2']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_9' and @value='1']").click()
        # else:
        #     print("Cat_9 INVISIVEL")     

        if button10 is True:
            #print("Cat_10 VISIVEL")
            time.sleep(0.2)
            button10element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_10' and @value='3']")

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button10element)
            self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_10' and @value='3']").click()
        else:
            print("Cat_10 INVISIVEL")

        # if button11 is True:
        #     #print("Cat_11 VISIVEL")
        #     time.sleep(0.1)
        #     button11element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_11' and @value='2']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button11element)
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='0']"))
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='0']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_11' and @value='2']").click()
        #     #Valor 0 
        # else:
        #     print("Cat_11 INVISIVEL")

        if button12 is True:
            #print("Cat_12 VISIVEL")
            time.sleep(0.2)
            button12element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_12' and @value='1']")

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button12element)
            self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_12' and @value='1']").click()
        else:
            print("Cat_12 INVISIVEL")

        # if button13 is True:
        #     #print("Cat_13 VISIVEL")
        #     time.sleep(0.1)
        #     button13element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_13' and @value='1']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button13element)
        #     #Valor 2
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='2']"))
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='2']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_13' and @value='1']").click()
        # else:
        #     print("Cat_13 INVISIVEL")


    # SANDRO QUEIROZ CAT_14
        # if button14 is True:
        #     #print("Cat_14 VISIVEL")
        #     time.sleep(0.1)
        #     button14element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_14' and @value='3']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button14element)
        #     #Valor 2
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='2']"))
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='2']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_14' and @value='3']").click()
        # else:
        #     print("Cat_14 INVISIVEL")

        # if button15 is True:
        #     #print("Cat_15 VISIVEL")
        #     time.sleep(0.1)
        #     button15element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_15' and @value='3']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button15element)
        #     #Valor 2
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='2']"))
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='2']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_15' and @value='3']").click()
        # else:
        #     print("Cat_15 INVISIVEL")

        # if button16 is True:
        #     #print("Cat_16 VISIVEL")
        #     time.sleep(0.2)
        #     button16element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_16' and @value='1']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button16element)
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_16' and @value='1']").click()
        # else:
        #     print("Cat_16 INVISIVEL")

        # if button17 is True:
        #     #print("Cat_17 VISIVEL")
        #     time.sleep(0.1)
        #     button17element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_17' and @value='2']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button17element)
        #     #Valor 2
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='2']"))
        #     #ActionChaivons(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='2']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_17' and @value='2']").click()
        # else:
        #     print("Cat_17 INVISIVEL")

        # if button18 is True:
        #     #print("Cat_18 VISIVEL")
        #     time.sleep(0.1)
        #     button18element = self.driver.find_element("xpath","//input[@type='radio' and @name='cat_18' and @value='1']")

        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button18element)
        #     #Valor 2
        #     #self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath",".//input[@type='radio' and @value='2']"))
        #     #ActionChains(self.driver).move_to_element(self.driver.find_element("xpath","//input[@type='radio' and @value='2']")).click(self.driver).perform()
        #     self.driver.find_element("xpath",".//input[@type='radio' and @name='cat_18' and @value='1']").click()
        # else:
        #     print("Cat_18 INVISIVEL")    

        contador_func()

   
    def clicar_no_botao_proxima(self):
        time.sleep(1)

        self.driver.find_element("xpath", '//button[text()="Próximo"]').click()
        time.sleep(1)
               
    def inserir_campos(self):
        time.sleep(0.2)
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
        indice_random = random.randint(0, len(pessoas) - 1)

        # Acessa diretamente a pessoa escolhida
        nameF, emailF, foneF = pessoas[indice_random]

        #GERAR NOME
        name_element = self.driver.find_element("xpath", self.SITE_MAP["buttons"]["nome"]["xpath"])
        ActionChains(self.driver).send_keys_to_element(name_element, nameF).perform()

        #GERAR EMAIL

        time.sleep(0.2)
        email_element = self.driver.find_element("xpath", self.SITE_MAP["buttons"]["email"]["xpath"])
        ActionChains(self.driver).send_keys_to_element(email_element, emailF).perform()

        #GERAR FONE

        time.sleep(0.2)
        fone_element = self.driver.find_element("xpath", self.SITE_MAP["buttons"]["fone"]["xpath"])
        ActionChains(self.driver).send_keys_to_element(fone_element, foneF).perform()

        time.sleep(0.2)
        select_element = self.driver.find_element("xpath",self.SITE_MAP["buttons"]["inst"]["xpath"])
        select = Select(select_element)
        select.select_by_value('Torcedor')

    
    def confirmar_votacao(self):
        time.sleep(0.1)
        self.driver.find_element("xpath",self.SITE_MAP["buttons"]["finalizar"]["xpath"]).click()
        time.sleep(0.2)
        self.driver.switch_to.alert.accept()
        time.sleep(0.1)       

    def rodar_indefinidamente(self):
        while True:  # Loop infinito para rodar as ações continuamente
            self.comecar_quest()
            self.abrir_questionarios()
            self.clicar_botao_certo()
            self.inserir_campos()
            self.confirmar_votacao()
            time.sleep(1)  # Pausa entre as ações, pode ser ajustado conforme necessário

    def set_tamanho_tela(self, largura, altura):
        """Define o tamanho da janela"""
        self.driver.set_window_size(largura, altura)

def iniciar_votacao_em_janela():
    votar = Votacao()
    votar.abrir_site()
    votar.set_tamanho_tela(600, 300)
    votar.rodar_indefinidamente()  # Chama o loop infinito para executar as ações indefinidamente

def votacaoFinalizada():
    print(f"Votação Finalizada")

def contador():
    # Variável local para contar
    count = 0
    
    # Função interna que incrementa o contador
    def incrementar():
        nonlocal count  # Informa que queremos usar a variável count da função externa
        count += 1
        print(f"Votações Finalizadas: {count}")
    
    return incrementar
contador_func = contador()

# Criação de várias janelas (por exemplo, 3)
num_janelas = 10  # Defina quantas janelas você deseja abrir simultaneamente
threads = []

largura_da_tela = 300
altura_da_tela = 500

espaco_entre_janelas = 50

for i in range(num_janelas):
    posicao_x = i * (largura_da_tela + espaco_entre_janelas)
    posicao_y = 0 
    # Inicia a votação em cada janela usando threads para executar simultaneamente
    t = Thread(target=iniciar_votacao_em_janela)
    threads.append(t)
    t.start()

