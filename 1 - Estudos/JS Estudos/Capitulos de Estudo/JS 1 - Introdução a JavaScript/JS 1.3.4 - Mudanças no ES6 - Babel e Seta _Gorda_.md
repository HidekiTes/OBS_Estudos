## Babel
Uma das maiores mudanças do ES5 é que o JavaScript ES6 não pode ser compilado diretamente nos navegadores. Precisamos usar um transpiler chamado Babel.js para produzir JavaScript compatível que os navegadores mais antigos possam ler

Para usar o Babel quando seu projeto for compilado, você precisará adicionar um package.json ao seu projeto. É aqui que todas as dependências do seu projeto serão mantidas.

Certifique-se de ter o Node e o npm instalados (ou o Node e o Yarn instalados se preferir usar o Yarn) e digite o comando npm init ou o comando yarn init em seu terminal. Responda às perguntas que surgirem e o package.json será pré-preenchido com esses valores.

Use npm/yarn para adicionar babel às suas dependências com o comando:

```js
npm install --save-dev babel-cli
// or
yarn add babel-cli --dev
```

Você usará o campo scripts em seu package.json para definir seu comando de construção com Babel. O comando real será diferente com base na pasta a partir da qual você está construindo e para onde deseja construir.

Por fim, na pasta raiz do seu projeto (onde reside o package.json), crie um arquivo .babelrc. Este é um arquivo de configuração do Babel que dirá ao Babel para transformar seu código para ES5. Instale a predefinição com:

```js
npm install --save-dev babel-preset-env
// or
yarn add babel-preset-env --dev
```

E então defina-o no seu arquivo .babelrc:

```js
{    
	“presets”: [“env”]
}
```
## Funções de Seta "Gorda"
Agora você pode executar o Babel executando o comando build. Sua pasta de destino agora deve ser exatamente igual à sua pasta de origem, exceto que o conteúdo da pasta de destino é o código ES5 em vez de ES6.

Se acontecer de você usar uma biblioteca ou estrutura JavaScript como create-react-app, é mais do que provável que o Babel já esteja configurado para você e você não precisará se preocupar com isso. Isto é para projetos criados do zero.

```js
//pre ES6
function add(num1, num2) {
return num1 + num2;
} 

//ES6 (implicit return)
const addImplicit = (num1, num2) => num1 + num2;

console.log(add(3, 4));
console.log(addImplicit(3, 4));
```

O one-liner ES6 tem um retorno implícito. Não precisamos da palavra-chave return se a função tiver apenas uma linha. Isso também significa que não há necessidade de chaves. Se a função tiver mais de uma linha, precisaríamos de chaves e uma instrução de retorno:

```js
//ES6 (explicit return)

const addExplicitReturn = (num1, num2) => 
{ let sum = num1 + num2; 
return sum;
};  

console.log(addExplicitReturn(3, 4));
```

Também é importante observar que quando você está usando classes, a função de seta está vinculada à palavra-chave “this”, portanto não há necessidade de realmente usar o método bind() para vincular a função à classe

===**Continuação - [[JS 1.3.5 - Mudanças no ES6 - Classes e Destructuring]]**===
