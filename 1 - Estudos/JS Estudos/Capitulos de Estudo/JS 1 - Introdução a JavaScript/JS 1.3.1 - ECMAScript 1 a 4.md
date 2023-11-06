ECMAScript 1 (ES1) foi lançado em 1997 com ES2 no ano seguinte. Não mudou muita coisa entre as duas versões.
## ES3
ES3 foi lançado em 1999 e adicionou suporte para muitas coisas novas que se tornaram parte padrão da linguagem hoje:
### Strict Equality
A partir do ES3, o operador de igualdade estrita ( === ) tornou-se uma opção para usar além do operador de igualdade ( == ). A diferença entre os dois é uma questão de comparar o tipo e o número. A igualdade estrita considera valores iguais, mas de tipo diferente, como desiguais.

```js
const compareTypeAndValue = (num, str) => {
return num === str;
} 

console.log(compareTypeAndValue(8, '8')); //false
console.log(compareTypeAndValue(8, 8)); //true
```
### Regular Expressions
Dois tipos de expressões regulares tornaram-se disponíveis no ES3: literal e construtor.
### Literal Expressions
Expressões regulares literais são expressas entre duas barras invertidas. A expressão real está entre as barras e o global, ignore maiúsculas e minúsculas, e os sinalizadores de várias linhas podem ser ativados ou desativados após a última barra invertida.

```js
/[^abc]/gim
```
### Constructor Expressions
Expressões regulares construtoras são aquelas expressões criadas como uma instância do objeto RegExp. A expressão regular real é o primeiro argumento passado para o construtor RegExp. A segunda, se necessário, são os sinalizadores que você gostaria de usar.

```js
const regex = new RegExp(‘[^abc]’, ‘gim’);
```
### Switch Statement
A instrução switch é uma instrução de fluxo de controle que basicamente encadeia muitas condições if sem a necessidade de usar instruções else if. A instrução switch usa um parâmetro e compara esse parâmetro com cada uma das instruções case. Se esse parâmetro corresponder a um caso, ele executa a lógica nesse bloco.
``` js
const fizzBuzz = (num) => {
	switch(num) {
		case 1:
			console.log(num);
		break;
		case 2:
			console.log(num);
		break;
		case 3:
			console.log("fizz");
		break;
		case 4:
			console.log(num);
		break;
		case 5:
			console.log("buzz");
		break;
		case 6:
			console.log("fizz");
		break;
		case 7:
			console.log(num);
		break;
		case 8:
			console.log(num);
		break;
		case 9:
			console.log("fizz");
		break;
		case 10:
			console.log(num);
		break;
	}
}
console.log(fizzBuzz(3))
```
### Try/Catch Handling
Um manipulador try/catch gerará um erro se o bloco try falhar por qualquer motivo. Abaixo, o try falha porque obj nunca foi definido. O bloco catch é executado e uma nova exceção do objeto Error é lançada.

```js
const isValidKey = (val1) => {
	try {
		let obj;
		return obj.hasOwnProperty(val1);
	} catch (err) {
		throw new Error("not valid key");
	}
}
console.log(isValidKey(""))
```

