# PiltoverLibrary
A simple CRUD application using Python and Firebase.

O sistema PiltoverLibrary é um CRUD que simula o funcionamento de uma biblioteca. 
Nele é possível realizar o cadastro, remoção e atualização dos livros, assim como também, de usuários do sistema.
O usuário terá acesso limitado ao sistema, podendo apenas buscar um livro específico para acessar suas informações ou listar
todos os livros cadastrados. Já o administrador do sistema poderá realizar todas as demais funcionalidades.

O PiltoverLibrary, na visão do usuário, é composto por 2 telas: Login e tela principal. Na tela principal a pesquisa pelo 
livro é realizada e as informações do mesmo são exibidas logo abaixo.  Para o administrador existem 4 telas: Login, menu 
principal, administrar livros e administrar usuários. O menu principal traz duas opções, administrar livros ou usuários. 

# Como executar?

Para conseguir executar o programa é necessário navegar no terminal até a pasta onde o projeto foi clonado. Lá devem ser instalados os seguintes pacotes, pyqt5, pyrebase4 e requests.
```bash
pip install PyQt5 pyrebase4 requests
```
O pyqt5 é a biblioteca responsável pela interface do sistema e pode ser instalado com o seguinte comando: pip install pyqt5. O pyrebase é a biblioteca que permite a conexão do sistema com o firebase, para instalar execute o comando: pip install pyrebase. Por fim, para abrir o programa, basta executar o arquivo main.py, que está na pasta do projeto, com o comando:
```bash
python main.py
```
Obs.: Certifique-se de utilizar o executável do Python 3. Caso o padrão do python no seu sistema seja o Python 2, especifique a versão correta com o comando:
```bash
python3 main.py
```
