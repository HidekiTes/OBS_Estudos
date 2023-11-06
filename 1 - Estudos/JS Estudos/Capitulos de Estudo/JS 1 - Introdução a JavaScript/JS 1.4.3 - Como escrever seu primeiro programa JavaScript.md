## Uso do Console no Chrome
Os navegadores modernos possuem ferramentas de desenvolvimento integradas para funcionar com JavaScript e outras tecnologias da web. Essas ferramentas incluem o Console, que é semelhante a uma interface shell, junto com ferramentas para inspecionar o DOM, depurar e analisar a atividade da rede.

O Console pode ser usado para registrar informações como parte do processo de desenvolvimento de JavaScript, bem como permitir que você interaja com uma página da web executando expressões JavaScript dentro do contexto da página. Essencialmente, o Console oferece a capacidade de escrever, gerenciar e monitorar JavaScript sob demanda.

Este tutorial abordará como trabalhar com o Console e JavaScript no contexto de um navegador e fornecerá uma visão geral de outras ferramentas de desenvolvimento integradas que você pode usar como parte de seu processo de desenvolvimento web.

Para abrir o Console JavaScript no Chrome, você pode navegar até o menu no canto superior direito da janela do navegador, representado por três pontos verticais. A partir daí, você pode selecionar Mais ferramentas e então Ferramentas do desenvolvedor.

![Chrome Developer Tools Menu Item](https://assets.digitalocean.com/articles/eng_javascript/js-console/chrome-developer-tools-menu.png)

Isso abrirá um painel onde você pode clicar em Console na barra de menu superior para abrir o Console JavaScript, caso ele ainda não esteja destacado:

![Chrome Developer Tools Menu Item](https://assets.digitalocean.com/articles/eng_javascript/js-console/chrome-console-tray.png)

Você também pode entrar no Console JavaScript usando o atalho de teclado ==**`CTRL+SHIFT+J`**== no Linux ou Windows, o que trará o foco imediatamente para a Console.
### Código
[[JS Cod. 1.4 -  Alert Hello World]]
## Códigos em Console
O Console também imprimirá o resultado da avaliação de uma expressão, que será lida como indefinida quando a expressão não retornar algo explicitamente.

Pode ser entediante continuar clicando em alertas pop-up, então vamos ver como criar o mesmo programa registrando-o no console com console.log().
### Código
[[JS Cod. 1.2 -  Retornos no Terminal]]
## Prompt para Input
Cada vez que executamos nosso existente “Hello, World!” programa, ele produz a mesma saída. Vamos perguntar o nome da pessoa que está executando nosso programa. Podemos então usar esse nome para personalizar a saída.

Para cada um dos nossos métodos JavaScript que usamos acima, podemos começar com uma linha solicitando entrada. 
### Código
[[JS Cod. 1.5 - Input em Console]]
## Saudando um Usuário com Alert()
Conforme discutido acima, o método alert() cria uma caixa pop-up na janela do navegador. Podemos usar este método para cumprimentar o usuário usando o nome da variável.
### Código
[[JS Cod. 1.6 - Saudando o usuário com alert()]]
## Saudando um usuário com Console.log()
Como vimos na seção anterior, o método console.log() imprime a saída no Console, assim como a função print() pode imprimir a saída no terminal em Python.
### Código
[[JS Cod. 1.6.1 - Saudando o usuário com Console.log]]
