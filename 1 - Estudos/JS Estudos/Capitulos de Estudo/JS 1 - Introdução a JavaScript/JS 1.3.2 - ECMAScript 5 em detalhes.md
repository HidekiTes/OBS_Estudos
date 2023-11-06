ES5 e ES6 são as especificações mais recentes lançadas que tiveram o maior número de alterações.

Dez anos após o lançamento do ES3, em 2009, foi lançada uma nova versão do ECMAScript. Este padrão foi a maior mudança no JavaScript desde a sua fundação. Alguns dos novos recursos incluem:
## "Use Strict"
Antes do ES5, variáveis ​​não declaradas (aquelas variáveis ​​que não usam a palavra-chave var quando introduzidas inicialmente) podiam ser usadas. Quando o recurso “use strict” está ativado, um erro de referência é gerado.

```js
"use strict" 
x = 5; // ReferenceError: x is not defined
```
## Métodos novos de Array
Existem vários novos métodos de array introduzidos no ES5 que tornaram a vida muito mais fácil ao trabalhar com arrays. Os novos métodos de array são mostrados aqui em ordem alfabética:
### every()
O método de array every() verifica se cada elemento do array satisfaz a condição que você passou.

```js
var arr = [6, 4, 5, 6, 7, 7];
arr.every(function(element) { 
	return element % 2 === 0; //checks to see if even
}); // false
```
### filter()
Pense no método filter como um loop for que possui uma instrução if. Se o elemento passar no teste, você envia esse elemento para um novo array. É assim que filter() funciona nos bastidores.

Assim como map(), outro método de array mencionado nesta seção, filter() retorna um novo array com os valores que passam no teste.

```js
var arr = [6, 4, 5, 6, 7, 7]; 

arr.filter(function(element) { 
	return element/2 > 3;
})
```
### forEach()
Um método muito semelhante a um loop for. Para cada elemento encontrado no array, o método forEach() executa uma função de retorno de chamada nele.

```js
var arr = [6, 4, 5, 6, 7, 7];

arr.forEach(function(element) {
	console.log(element * 2);
})
```
### indexOf() e lastIndexOf()
Se precisar procurar um elemento específico em um array, você pode fazer isso com indexOf() e lastIndexOf(). indexOf() retorna o primeiro índice do parâmetro de pesquisa se for encontrado, caso contrário, retorna -1.

Em lastIndexOf(), nos dá o último índice do elemento de pesquisa no array. Novamente, se não for encontrado, retornará -1.

```js
var arr = [6, 4, 5, 6, 7, 7];

console.log(arr.indexOf(4)); // 1
console.log(arr.indexOf(2)); // -1
console.log(arr.indexOf(7)); // 4

console.log(arr.lastIndexOf(7)); // 5
```
### isArray()
Este método verifica se o objeto passado para ele é um array ou não. Retorna um booleano.

```js
var arr = [6, 4, 5, 6, 7, 7];

var str = "Hello Educative.io"; 

console.log(Array.isArray(arr));
console.log(Array.isArray(str));
```
### map() 
O método map() é muito semelhante ao método forEach(), exceto que retorna um array totalmente novo. Isso permite a manipulação de dados sem comprometer o array original.

A função de retorno de chamada deve ter uma instrução return. Este é o novo valor que irá para aquele índice específico da nova matriz.

```js
var arr = [6, 4, 5, 6, 7, 7];

arr.map(function(element) { 
	return element * 2;
})
```
### reduce() e reduce 
Cada um desses métodos de redução aplica uma função de retorno de chamada a cada elemento do array. O que há de especial nos métodos reduce() e reduceRight() é que eles reduzem o array a um único elemento.

O método reduceRight() é exatamente como reduce(), exceto que ele itera da direita para a esquerda em vez da esquerda para a direita.

```js
var arr = [6, 4, 5, 6, 7, 7]; 

var reduced = arr.reduce(function(curr, next) {
return curr + next;
}, 0); 

var reducedRight = arr.reduceRight(function(curr, next) {
return curr + next;
}, 0) 

console.log(reduced);
console.log(reducedRight);
```
### some()
O método some() é quase exatamente igual ao método every(), com a exceção de que verifica se pelo menos um elemento satisfaz a condição que você definiu para ele.

```js
var arr = [6, 4, 5, 6, 7, 7];

arr.some(function(element) {
return element % 2 === 0; //checks to see if even
}); //true
```
