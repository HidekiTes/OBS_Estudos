## Rest e Spread
Os operadores rest e spread têm essencialmente a mesma sintaxe, mas servem a um propósito diferente. O operador rest é usado antes de um parâmetro de função para indicar que vários argumentos devem ser atribuídos a esse parâmetro.

```js
function restExample(a, ...b) {
	console.log(a); // 1
	console.log(b); // [2, 3, 4, 5, 6]
} 

restExample(1, 2, 3, 4, 5, 6);
```

O operador spread usa a mesma sintaxe, mas é usado por arrays. Essencialmente, ele pega o conteúdo do array e o copia para que possa ser espalhado na nova estrutura. Podemos usar o operador spread como uma forma de adicionar algo a um array sem ter que usar push() ou unshift().

```js
function spreadExample(arr) {
	let newArr = [2, 4, 6, 8];
	console.log("arr", arr);
	let combinedArr = [...newArr, ...arr]; //this pushes the contents of newArr and the contens of arr into a one-dimensional combined array.
	let arrWithOtherContents = ["a", ...newArr, {b: "c", d: "e"}, true, ...arr];
	console.log(arrWithOtherContents);
	console.log("combined", combinedArr);
}

console.log(spreadExample([1, 3, 5, 7, 9]))
```

O operador spread funciona muito bem quando você precisa trabalhar com um array, mas não deseja manipular o conteúdo real do array. Você pode usar o operador spread para criar essencialmente uma cópia para trabalhar.
## Template Literals
No ES6, não precisamos mais concatenar strings, espaços e variáveis ​​para formar uma string maior. Usamos literais de modelo para criar expressões que nos permitem ter variáveis ​​incorporadas em nossas strings.

```js
let name = "Jane";
let holiday = "Christmas";

//pre-ES6:
console.log(name + "'s favorite holiday is " + holiday);

//ES6+:
console.log(`${name}'s favorite holiday is ${holiday}`);
```
