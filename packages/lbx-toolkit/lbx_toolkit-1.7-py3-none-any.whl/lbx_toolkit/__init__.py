import os
import sys
import locale
import time
import threading
import logging
import msal
import requests
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import numpy as np
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class auth_EntraID: # Classe de autenticação de usuários no Microsoft Entra ID (antiga Azure AD)
    def __init__(self, client_id, client_secret, tenant_id, grupo, timeout=60, log_file='auth_EntraID.log'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.timeout = timeout
        self.grupo = grupo
        self.authority = f"https://login.microsoftonline.com/{self.tenant_id}"
        self.scope = ["https://graph.microsoft.com/.default"]
        self.redirect_uri = "http://localhost:8000"
        self.response = ""
        self.status_code = 0
        self.server = None
        self.log_file = log_file

        # Configura o logger
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def valida_grupo(self): # Valida se o usuário autenticado pertence a grupo de segurança informado
        # Redireciona stdout e stderr para arquivos de log
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = open('stdout.log', 'a')
        sys.stderr = open('stderr.log', 'a')

        # Configurações do Selenium
        chrome_options = Options()
        chrome_options.add_argument("--incognito")

        # Inicializa a aplicação MSAL
        try:        
            app = msal.ConfidentialClientApplication(
                self.client_id,
                authority=self.authority,
                client_credential=self.client_secret,
            )
        except BaseException as err:
            print(f'Falha ao iniciar aplicação MSAL: {err}')
            # Restaura saída padrão
            sys.stdout.close()
            sys.stderr.close()
            sys.stdout = original_stdout
            sys.stderr = original_stderr
            print(f'Script abortado por falha aplicação MSAL. Verifque logs: {self.log_file}, stdout.log e sterr.log')
            os._exit(0)

        # Inicia o fluxo de código de autorização
        try:
            flow = app.initiate_auth_code_flow(scopes=self.scope, redirect_uri=self.redirect_uri)
            auth_url = flow["auth_uri"]
            self.response = f"Acessando a URL de autenticação Microsoft Entra ID (antiga Azure AD): {auth_url}"
            self.logger.info(self.response)
        except BaseException as err:
            print(f'Falha no fluxo de autorização Microsoft Entra ID (antiga Azure AD): {err}')
            # Restaura saída padrão
            sys.stdout.close()
            sys.stderr.close()
            sys.stdout = original_stdout
            sys.stderr = original_stderr
            print(f'Script abortado por falha no fluxo de autorização Microsoft Entra ID (antiga Azure AD). Verifque logs: {self.log_file}, stdout.log e sterr.log')
            os._exit(0)            

        # Inicializa o ChromeDriver com redirecionamento de saída
        try:
            service = Service(ChromeDriverManager().install())
            service.start()
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.get(auth_url)
        except BaseException as err:
            print(f'Falha na inicialização do Chrome: {err}')
            # Restaura saída padrão
            sys.stdout.close()
            sys.stderr.close()
            sys.stdout = original_stdout
            sys.stderr = original_stderr
            print(f'Script abortado na inicialização do Chrome. Verifque logs: {self.log_file}, stdout.log e sterr.log')
            os._exit(0)                    

        class AuthHandler(BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                self.server.logger.info("%s - - [%s] %s\n" %
                                        (self.client_address[0],
                                         self.log_date_time_string(),
                                         format % args))

            def do_GET(self):
                parsed_path = urlparse.urlparse(self.path)
                query_params = urlparse.parse_qs(parsed_path.query)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # Captura o código de autorização e o estado
                if 'code' in query_params and 'state' in query_params:
                    self.server.auth_code = query_params['code'][0]
                    self.server.state = query_params['state'][0]
                    self.wfile.write(b'''
                                    <!DOCTYPE html>
                                    <html lang="pt_BR">
                                    <head>
                                        <meta charset="UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                        <style>
                                                body {
                                                    font-family: 'Arial', sans-serif;
                                                    background-color: #f8f9fa;
                                                    margin: 0;
                                                    font-size: 16px;
                                                    padding: 30px;
                                                    display: flex; *
                                                }

                                                .container {        
                                                    width: 100%;
                                                    margin: auto;
                                                    background-color: #ffffff;
                                                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                                    padding: 16px;
                                                    text-align: center;
                                                    font-size: 16px;
                                                    border-radius: 8px;
                                                }

                                                h1 {    
                                                    font-size: 18px;
                                                    text-align: center;
                                                    color: #007bff;
                                                }
                                        </style>
                                     </head>
                                        <div class="container">
                                            <h1>Autentica&#231;&#227;o realizada com sucesso!</h1>
                                            Aguarde que esta p&#225;gina ser&#225; fechada automaticamente.<br>
                                            Se isto n&#227;o acontecer, pode fech&#225;-la manualmente.
                                        </div>
                                     </body></html>
                                     ''')
                else:
                    self.wfile.write(b'''
                                    <!DOCTYPE html>
                                    <html lang="pt_BR">
                                    <head>
                                        <meta charset="UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                        <style>
                                                body {
                                                    font-family: 'Arial', sans-serif;
                                                    background-color: #f8f9fa;
                                                    margin: 0;
                                                    font-size: 16px;
                                                    padding: 30px;
                                                    display: flex; *
                                                }

                                                .container {        
                                                    width: 100%;
                                                    margin: auto;
                                                    background-color: #ffffff;
                                                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                                    padding: 16px;
                                                    text-align: center;
                                                    font-size: 16px;
                                                    border-radius: 8px;
                                                }

                                                h1 {    
                                                    font-size: 18px;
                                                    text-align: center;
                                                    color: red;
                                                }
                                        </style>
                                     </head>
                                        <div class="container">
                                            <h1>Falha na autentica&#231;&#227;o!</h1>
                                            Esta p&#225;gina ser&#225; fechada automaticamente.<br>
                                            Se isto n&#227;o acontecer, pode fech&#225;-la manualmente.
                                        </div>
                                     </body></html>
                                     ''')

        # Inicializa o servidor HTTP
        self.server = HTTPServer(('localhost', 8000), AuthHandler)
        self.server.logger = self.logger  # Passa o logger para o servidor

        # Função para monitorar o tempo limite
        def monitor_timeout():
            time.sleep(self.timeout)
            if not hasattr(self.server, 'auth_code'):
                self.response = "tempo limite para autenticação foi excedido"
                self.status_code = 490
                self.logger.error(self.response)
                sys.stdout.close()
                sys.stderr.close()
                sys.stdout = original_stdout
                sys.stderr = original_stderr
                print(f'Código retorno: {self.status_code} ', end='') ## self.status_code = 200, usuário pertence ao grupo informado. self.status_code = 299, grupo existe mas usuário NÃO pertence à ele. Erros retornam 4xx.
                print(f'Resposta: {self.response}', end='\n\n')  
                print('Falha na autenticação! Execução abortada!')
                driver.quit()
                self.server.server_close()
                os._exit(0)       

        # Inicia a thread para monitorar o tempo limite
        timeout_thread = threading.Thread(target=monitor_timeout)
        timeout_thread.start()

        # Espera pelo código de autorização
        self.response = "Esperando pela autenticação..."
        self.logger.info(self.response)
        self.server.handle_request()

        # Restaura stdout e stderr
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = original_stdout
        sys.stderr = original_stderr

        # Verifica se o código de autorização foi obtido dentro do tempo limite
        if not hasattr(self.server, 'auth_code'):
            return

        # Obtém o código de autorização e o estado capturados pelo servidor HTTP
        auth_code = self.server.auth_code
        state = self.server.state

        # Adquire o token usando o código de autorização, verificando o estado
        try:
            result = app.acquire_token_by_auth_code_flow(flow, {"code": auth_code, "state": state})
        except ValueError as e:
            self.response = f"Erro ao obter o token de acesso: {e}"
            self.status_code = 401
            self.logger.error(self.response)
            driver.quit()
            return

        if "access_token" in result:
            access_token = result['access_token']
            headers = {
                'Authorization': 'Bearer ' + access_token
            }

            # Obtém o email do usuário autenticado
            me_response = requests.get(
                'https://graph.microsoft.com/v1.0/me',
                headers=headers
            )
            self.status_code = me_response.status_code
            if me_response.status_code == 200:
                me_data = me_response.json()
                user_email = me_data['userPrincipalName']
                self.response = f"Email do usuário autenticado: {user_email}"
                self.logger.info(self.response)

                # Verifica se o usuário pertence ao grupo
                group_name = self.grupo

                # Obtém o ID do usuário
                user_response = requests.get(
                    f'https://graph.microsoft.com/v1.0/users/{user_email}',
                    headers=headers
                )
                self.status_code = user_response.status_code
                if user_response.status_code == 200:
                    user_data = user_response.json()
                    user_id = user_data['id']

                    # Pesquisa o grupo pelo nome
                    group_response = requests.get(
                        f"https://graph.microsoft.com/v1.0/groups?$filter=displayName eq '{group_name}'",
                        headers=headers
                    )
                    self.status_code = group_response.status_code
                    if group_response.status_code == 200:
                        group_data = group_response.json()
                        if 'value' in group_data and len(group_data['value']) > 0:
                            group_id = group_data['value'][0]['id']

                            # Verifica se o usuário está no grupo
                            members_response = requests.get(
                                f'https://graph.microsoft.com/v1.0/groups/{group_id}/members',
                                headers=headers
                            )
                            self.status_code = members_response.status_code
                            if members_response.status_code == 200:
                                members_data = members_response.json()
                                if 'value' in members_data:
                                    user_in_group = any(member['id'] == user_id for member in members_data['value'])
                                    if user_in_group:
                                        self.response = f"O usuário {user_email} liberado para uso desta aplicação."
                                    else:
                                        self.response = f"O usuário {user_email} NÃO liberado para uso desta aplicação. Solicite acesso à TI."
                                        self.status_code = 299
                                else:
                                    self.response = "Resposta da API de membros não contém a chave 'value'."
                                    self.status_code = 460
                            else:
                                self.response = f"Erro na resposta da API de membros: {members_response.status_code}"
                                self.response += f"\n{members_response.json()}"
                        else:
                            self.response = f"Grupo '{group_name}' não encontrado."
                            self.status_code = 470
                    else:
                        self.response = f"Erro na resposta da API de grupos: {group_response.status_code}"
                        self.response += f"\n{group_response.json()}"
                else:
                    self.response = f"Erro na resposta da API de usuário: {user_response.status_code}"
                    self.response += f"\n{user_response.json()}"
            else:
                self.response = f"Erro ao obter informações do usuário: {me_response.status_code}"
                self.response += f"\n{me_response.json()}"
        else:
            self.response = f"Erro ao obter o token de acesso: {result.get('error')}"
            self.response += f"\n{result.get('error_description')}"
            self.status_code = 480
    
        # Fecha o navegador
        driver.quit()
        service.stop()

        # Define o retorno
        print(f'\nCódigo retorno: {self.status_code} ', end='') ## self.status_code = 200, usuário pertence ao grupo informado. self.status_code = 299, grupo existe mas usuário NÃO pertence à ele. Erros retornam 4xx.
        print(f'Resposta: {self.response}', end='\n\n')  
        if self.status_code == 200:
            print('Acesso autorizado!')
        else:
            print('Permissões inválidas! Execução abortada!')
            os._exit(0)        

    def disclaimer(self): # Mostra o aviso do funcionamento e necessidade de autenticação
        input(f'''
              
        Para ser utilizado de forma adequada e segura, este script requer autenticação no Microsoft Entra ID (antiga Azure AD).
        Também requer que seu usuário pertença a um grupo de segurança específico. Se você não tem a segurança que tem permissão de uso, solicite previamente à TI.
        
        Para continuar, é necessário fornecer suas credenciais, aquelas que costumeiramente utiliza para acessar os serviços de e-mail corporativo.
        Uma janela de navegador será aberta e você será direcionado à tela de Logon do Microsoft Entra ID.
        Faça o Logon fornecendo usuário, senha e validação de duplo fator (no autenticador da Microsoft, instalado em seu celular).        
        Após a autenticação, a janela do navegador será fechada e o script iniciará o processo de execução.

        Você tem {self.timeout} segundos para realizar a autenticação ou a execução será abortada.

        Tecle [ENTER] para continuar ...
        
        ''')

class postgreSQL: # Classe de acesso e interação com banco PostgreSQL
    def db(Config): # Conecta no banco de dados
        try:
            DbConn = psycopg2.connect(**Config)  ## na chamada de uma função/método, o * explode os valores de um dicionário em argumentos posicionais (só valores) e ** explode discionário em argumentos nominais (nome=valor)
            return DbConn
        except Exception as Err:
            print(f"Erro ao conectar ao banco de dados: {Err}\nBanco: {DbConfig['user']}@{DbConfig['host']}:{DbConfig['dbname']}")
            #return None
            os._exit(1)

    def csv_df(CsvPath, CsvDelim=';'): # Le arquivo CSV e gera Dataframe do Pandas
        try:
            DataFrame = pd.read_csv(CsvPath, delimiter=CsvDelim)  # Verifique se o delimitador é ';'
            DataFrame.replace({np.nan: None}, inplace=True)  ## troca 'NaN' por None (null no postgresql)
            return DataFrame
        except Exception as Err:
            print(f"Erro ao ler CSV: {Err}\nArquivo: str({CsvPath})")
            #return None
            os._exit(1)

    def db_insert_df(DbConn, DataFrame, Tabela, Schema=None, Colunas=None, OnConflict=None): # Insere os dados de um dataframe em uma tabela equivalente no banco (exige mesma estrutura de colunas)
        # Essa função exige que os nomes dos cabeçalhos das colunas do CSV sejam os mesmos das colunas da tabela de destino
        Colunas = Colunas or DataFrame.columns.tolist()     # Caso não seja fornecida a lista de colunas, assume as colunas do DataFrame
        Valores = [tuple(Linha) for Linha in DataFrame[Colunas].values]    
        Schema = Schema or 'public'
        Query = f'insert into {Schema}.{Tabela} ({', '.join(Colunas)}) values %s '
        if not OnConflict is None:
            Query = Query + OnConflict

        try:
            DbCursor = DbConn.cursor() 
            execute_values(DbCursor, Query, Valores)  
            DbConn.commit()
        except Exception as Err:
            DbConn.rollback()
            print(f"Erro ao inserir dados do DataFrame: {Err}\nQuery:\n{Query}")
            #return None        
            os._exit(1)
        finally:        
            DbCursor.close()
            DbConn.close()

    def db_select(DbConn, Query): # Retorna um cursor à partir de um select
        BlackList = ['INSERT ', 'DELETE ', 'UPDATE ', 'CREATE ', 'DROP ', 'MERGE ', 'REPLACE ', 'CALL ', 'EXECUTE ']
        if any(element in Query.upper() for element in BlackList):
            BlackListed = [element for element in BlackList if element in Query.upper()]          
            print(f'Este método permite apenas consultas. Outras instruções SQL de manipulação de dados e metadados não são permitidas:\n')
            print(f'\nA query informada possui as seguintes palavras reservadas não aceitas: {BlackListed} e não foi executada!')
            return None            
        else:
            try:
                DbCursor = DbConn.cursor()
                DbCursor.execute(Query)
                Dados = DbCursor.fetchall()
                Colunas = [Col[0] for Col in DbCursor.description]
                DbConn.commit()
                DbCursor.close()
                return Dados, Colunas
            except Exception as Err:
                DbConn.rollback()
                print(f"Erro ao executar Select: {Err}\nQuery:\n{Query}")
                #return None        
                os._exit(1)
            finally:
                DbConn.close()    

    def db_update(DbConn, Query): # Retorna um cursor à partir de um select
        UpdRows = 0
        BlackList = ['INSERT ', 'DELETE ', 'SELECT ', 'CREATE ', 'DROP ', 'MERGE ', 'REPLACE ', 'CALL ', 'EXECUTE ']
        if any(element in Query.upper() for element in BlackList):
            BlackListed = [element for element in BlackList if element in Query.upper()]          
            print(f'Este método permite apenas updates. Outras instruções SQL de manipulação de dados e metadados não são permitidas:\n')
            print(f'\nA query informada possui as seguintes palavras reservadas não aceitas: {BlackListed} e não foi executada!')
            return None            
        else:
            try:
                DbCursor = DbConn.cursor()
                DbCursor.execute(Query)
                UpdRows = DbCursor.rowcount
                DbConn.commit()
                DbCursor.close()
                return UpdRows
            except Exception as Err:
                DbConn.rollback()
                print(f"Erro ao executar Update: {Err}\nQuery:\n{Query}")
                #return None        
                os._exit(1)
            finally:
                DbConn.close()    

class api_rest: # Classe para interação com APIs Rest (especialmente Sienge)
    def __init__(self, url, credenciais, cadencia):
        self.Url = url
        self.Credenciais = credenciais
        self.Cadencia = 1/cadencia  
        self.TempoUltReq = None 
        self.Intervalo = self.Cadencia + 1     

    def controla_cadencia(self): ## para controle apenas, não deve ser chamada fora da classe
        # Verificar o tempo atual
        Agora = time.time()
        
        # Calcular intervalo entre requisições
        if self.TempoUltReq:
            self.Intervalo = Agora - self.TempoUltReq
        else:
            self.Intervalo = float('inf')  # Primeira requisição não espera
        
        # Calcular o tempo de espera necessário para respeitar o limite
        if self.Intervalo < self.Cadencia:
            self.Espera = self.Cadencia - self.Intervalo
            time.sleep(self.Espera)
            return self.Espera
        else:
            self.Espera = 0
            return self.Espera, self.Intervalo


    def auth_basic(self): # Autentica e abre sessão na API      
        try:          
            self.Sessao = requests.Session()
            #Sessao.auth = (ApiUser, ApiPass)
            self.Sessao.auth = HTTPBasicAuth(self.Credenciais['user'], self.Credenciais['password'])
            Auth = self.Sessao.post(self.Url)  
            #print(f'Status: {Auth.status_code}')
            #print(f'Retorno: {Auth.text}')
            return self.Sessao
        except Exception as Err:
            print(f"Falha ao autenticar API: {Err}\nURL: {self.Url}")
            os._exit(1)                        

    def endpoint_json(self, endpoint, metodo, payload=None): # Interage com End Point
        self.ult_tempo_req = time.time() 
        self.Metodo = metodo.lower()
        self.EndPoint = self.Url + endpoint
        self.Payload = payload
        MetodosAceitos = ['post', 'get', 'patch', 'put']
        if not any(element in self.Metodo for element in MetodosAceitos):
            print(f'Método {self.Metodo} não previsto. Abortando chamada!')
            #return None
            os._exit(1)
        else:
            ChamadaApi = f'self.Sessao.{self.Metodo}(self.EndPoint)' if self.Payload is None else f'self.Sessao.{self.Metodo}(self.EndPoint, json=self.Payload)'
            try: 
                self.controla_cadencia()
                self.RetEndPoint = eval(ChamadaApi)
                self.TempoUltReq = time.time()  
                self.RetEndPoint.Espera = self.Espera ## adiona o tempo de espera ao retorno da API
                self.RetEndPoint.Intervalo = self.Intervalo ## adiciona o intervalo entre chamada ao retorno da API
                if self.RetEndPoint.status_code >= 500:
                    print(f"Erro na chamada do endpoint: {Err}\nEndpoint: {self.EndPoint}")
                    print(f'Codigo retorno: {self.RetEndPoint.status_code}')
                    print(f'Resposta: {self.RetEndPoint.text}')
                    os._exit(1)    
                return self.RetEndPoint
            except Exception as Err:
                print(f"Falha chamada endpoint: {Err}\nEndpoint: {self.EndPoint}")
                print(f'Codigo retorno: {self.RetEndPoint.status_code}')
                print(f'Resposta: {self.RetEndPoint.text}')
                os._exit(1)                        
        
    def close(self): # Encerra a cessão
        self.Sessao.close()                   