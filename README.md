# Automação de Votação

Este repositório contém um script para automação de um processo de votação online usando o Selenium WebDriver. O objetivo do script é realizar ações automáticas em um site de votação, incluindo o preenchimento de formulários, a navegação pelos questionários, e a confirmação das votações.

## ------> Limitações <------
**Atenção**: _O código foi desenvolvido para um site de votação que já encerrou a votação.
Portanto, não será possível testar o funcionamento do script em um ambiente de produção, já que as votações não estão mais ativas. O código, no entanto, pode ser adaptado e utilizado para sites semelhantes que estejam com votações abertas_.

------------

## Funcionalidades

- **Preenchimento automático de formulários**: O script preenche automaticamente campos como nome, e-mail e telefone.
- **Seleção de opções**: O script escolhe automaticamente opções de um campo de seleção (`<select>`).
- **Navegação por questionários**: Clica nos botões necessários para avançar pelos questionários e concluir a votação.
- **Automação contínua**: O script é configurado para rodar indefinidamente, processando várias votações automaticamente.
- **Contagem de votações finalizadas**: Mantém um contador de quantas votações foram completadas com sucesso.

## Como Funciona

O script realiza as seguintes ações principais:
1. **Preenche os campos do formulário**: O nome, e-mail, telefone e uma opção do campo de seleção são preenchidos automaticamente.
2. **Clica no botão "Próximo"**: O script navega pelas páginas clicando nos botões apropriados.
3. **Confirma a votação**: Quando todas as informações são inseridas, a votação é finalizada automaticamente.
4. **Loop infinito**: O script continua rodando indefinidamente, repetindo o processo para várias votações.
5. **Contagem de votações**: A cada votação finalizada, o script incrementa um contador e imprime o número total de votações concluídas.

## Requisitos

- **Python 3.x**: O script foi desenvolvido em Python 3.
- **Selenium**: Usado para automatizar o navegador.
- **WebDriver**: Necessário para controlar o navegador. Pode ser o ChromeDriver, GeckoDriver, etc.
- **Threads**: O script é capaz de abrir várias janelas de navegador simultaneamente, utilizando threads para rodar votações em paralelo.

### Instalação

1. **Instalar o Selenium**:
   Se você ainda não tem o Selenium instalado, execute o seguinte comando:
   ```bash
   pip install selenium
   
2. **Baixar o WebDriver**:

    Chrome: ChromeDriver
    Firefox: GeckoDriver
    Certifique-se de baixar a versão do WebDriver compatível com a versão do seu navegador.
    
    Configuração:
    
    Altere o xpath no código para os elementos do site de votação com o qual você está interagindo.
    Ajuste os parâmetros de tamanho da janela e o número de threads conforme necessário.
    
    
    ## Uso
    Rodar o script: Após configurar o código, execute o script para iniciar a automação de votação.
    
    ```bash
    Copiar código
    python votacao_automatica.py
    Abrir múltiplas janelas: O script cria várias janelas de navegador, em número configurável, e começa a rodar as votações simultaneamente.
    
    Contar as votações: O número de votações finalizadas será exibido no terminal a cada vez que uma votação for concluída.

