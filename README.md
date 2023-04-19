# Atalho Faculdade
**Atalho para facilitar a utilização de arquivos da faculdade:**

Este programa é projetado para simplificar o gerenciamento de arquivos e diretórios da faculdade. O programa oferece as seguintes funcionalidades:

- Interface gráfica baseada na biblioteca Tkinter, que permite ao usuário abrir arquivos e diretórios com facilidade através de botões intuitivos;
- Manipulação de arquivos e diretórios por meio das bibliotecas os e shutil;
- Notificação de erros: caso um arquivo ou diretório seja renomeado, excluído ou movido, uma caixa de texto será exibida para alertar o usuário de que a solicitação não pôde ser concluída;
- Acesso fácil ao site da faculdade usando a biblioteca webbrowser;
- Acesso ao executável Calculadora de VT usando a biblioteca subprocess;
- Ambiente virtual incluído: o programa vem com um ambiente virtual para tornar a criação do executável mais fácil e garantir que as bibliotecas e dependências necessárias sejam incluídas;
- Executável portátil: uma vez que o executável é criado, ele pode ser usado como um programa standalone que pode ser executado em qualquer computador sem a necessidade de instalar as bibliotecas e dependências manualmente.

# Calculadora de VT
Este é um código em Python que apresenta uma interface gráfica utilizando a biblioteca Tkinter e a extensão tkcalendar para selecionar datas. O objetivo é calcular o valor total do vale transporte necessário para um período de trabalho, baseado no número de dias úteis trabalhados e no valor diário do vale transporte.

**Funcionamento**

Ao executar o programa, o usuário seleciona a data de início e término do período que deseja calcular o valor do vale transporte. O programa então verifica se as datas foram inseridas corretamente, comparando a data de início com a data de término. Em seguida, o usuário insere o valor diário do vale transporte.
Caso o usuário insira um valor inválido para o vale transporte, uma mensagem de erro é exibida. Caso todas as informações tenham sido inseridas corretamente, o programa calcula o valor total do vale transporte necessário para o período de trabalho e exibe na tela.

**Bibliotecas utilizadas**
- datetime
- workadays
- tkinter
- tkcalendar
