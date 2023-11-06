## Introdução
Os navegadores modernos possuem ferramentas de desenvolvimento integradas para funcionar com JavaScript e outras tecnologias da web. Essas ferramentas incluem o Console, que é semelhante a uma interface shell, junto com ferramentas para inspecionar o DOM, depurar e analisar a atividade da rede.

O Console pode ser usado para registrar informações como parte do processo de desenvolvimento de JavaScript, bem como permitir que você interaja com uma página da web executando expressões JavaScript dentro do contexto da página. Essencialmente, o Console oferece a capacidade de escrever, gerenciar e monitorar JavaScript sob demanda.

Este tutorial abordará como trabalhar com o Console e JavaScript no contexto de um navegador e fornecerá uma visão geral de outras ferramentas de desenvolvimento integradas que você pode usar como parte de seu processo de desenvolvimento web.
## Trabalhando com o console em um navegador
A maioria dos navegadores modernos que suportam HTML e XHTML baseados em padrões fornecerão acesso a um Developer Console onde você pode trabalhar com JavaScript em uma interface semelhante a um shell de terminal. Esta seção descreve como acessar o Console no Chrome.

Para abrir o Console JavaScript no Chrome, você pode navegar até o menu no canto superior direito da janela do navegador, representado por três pontos verticais. A partir daí, você pode selecionar Mais ferramentas e depois Ferramentas do desenvolvedor.

![[Pasted image 20231010102159 1.png]]

### Códigos
[[JS Cod. 1.1 -  Primeira Interação no Console]]
## Trabalhando com um arquivo HTML
Você pode trabalhar no contexto de um arquivo HTML ou de uma página renderizada dinamicamente na Console. Isso oferece a oportunidade de experimentar o código JavaScript dentro do contexto de HTML, CSS e JavaScript existentes.

Tenha em mente que assim que você recarregar uma página após modificá-la no Console, ela retornará ao estado anterior à modificação do documento. Certifique-se de salvar todas as alterações que gostaria de manter em outro lugar.

Pegue um documento HTML, como o arquivo index.html a seguir, para entender como usar o Console para modificá-lo.
### Códigos
[[JS Cod. 1.3 - Aplicando JS via HTML]]
## Trabalhando com outras ferramentas de desenvolvimento 
Dependendo das ferramentas de desenvolvimento do navegador que você usa, você poderá usar outras ferramentas para ajudar no fluxo de trabalho de desenvolvimento web.
### DOM — Document Object Model
Cada vez que uma página da web é carregada, o navegador em que ela está cria um Document Object Model, ou DOM, da página.

O DOM é uma árvore de objetos e mostra os elementos HTML dentro de uma visão hierárquica. A árvore DOM está disponível para visualização no painel Inspetor no Firefox ou no painel Elementos no Chrome.

Essas ferramentas permitem inspecionar e editar elementos DOM e também identificar o HTML relacionado a um aspecto de uma página específica. O DOM pode informar se um trecho de texto ou imagem possui um atributo de ID e pode ajudá-lo a determinar qual é o valor desse atributo.

A página que você modificou acima teria uma visualização DOM semelhante a esta antes de recarregar a página:
![[Pasted image 20231011114147 1.png]]

Além disso, você verá estilos CSS em um painel lateral ou abaixo do painel DOM, permitindo ver quais estilos estão sendo empregados no documento HTML ou por meio de uma folha de estilos CSS. Por exemplo, observe o que o estilo do corpo da sua página de amostra inclui no Firefox Inspector:
![[Pasted image 20231011114454 1.png]]

Para editar em tempo real nó DOM, clique duas vezes em um elemento selecionado e faça as alterações. Por exemplo, você pode modificar uma tag ```<h1>``` e torná-la uma tag ```<h2>```.

Tal como acontece com o Console, se você recarregar a página, você retornará ao estado original salvo do documento HTML.
### Network