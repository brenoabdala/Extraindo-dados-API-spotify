# Extraindo dados API spotify

### Credenciais da API do Spotify

#### Passo 1: Criar uma Conta no Spotify Developer
 - Acesse o site do Spotify Developer: Vá para Spotify for Developers.
Faça login: Use sua conta do Spotify ou crie uma nova conta, se necessário.

#### Passo 2: Criar um Aplicativo
 - Acesse o Dashboard: Depois de fazer login, vá para o seu Painel de Desenvolvedor.
Clique em "Create an App": Preencha o formulário com um nome e descrição para seu aplicativo. Aceite os termos de uso e clique em "Create".

#### Passo 3: Obter as Credenciais
 - Localize seu Aplicativo: Após criar o aplicativo, você será redirecionado para a página do seu aplicativo.
Client ID e Client Secret: Na página do aplicativo, você verá o "Client ID" e o "Client Secret". Esses são os dados que você usará no seu código.


-----------------------------------------------

### Instalação Bibliotecas Python
> spotipy==2.24.0 | pandas==2.2.2

-----------------------------------------------

### Sobre o código
 
 - <strong>Importação das Bibliotecas:</strong> Importa o spotipy e as credenciais.
 - <strong>Autenticação:</strong> Usa as credenciais para autenticar na API do Spotify.
 - <strong>Busca:</strong> Realiza uma busca pelo artista desejado.
 - <strong>Exibição de Resultados:</strong> Exibe algumas informações sobre o artista encontrado.
 - <strong>Resultado:</strong>O resultado da extração em uma arquivo CSV.
 - <strong>Observações:</strong> Substituir 'YOUR_CLIENT_ID' e 'YOUR_CLIENT_SECRET' pelas suas credenciais reais. Você pode modificar a consulta na função sp.search() para buscar músicas, álbuns, etc., alterando o parâmetro type.
