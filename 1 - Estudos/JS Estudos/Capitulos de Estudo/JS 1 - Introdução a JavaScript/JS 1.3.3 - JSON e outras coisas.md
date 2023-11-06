## JSON
A capacidade de analisar e restringir JavaScript Object Notation (JSON) tornou-se uma possibilidade no padrão ES5. O formato JSON é usado basicamente para transmitir algum tipo de dados estruturados por meio de uma conexão de rede, geralmente um aplicativo da web e uma API.

Quando transmitimos os dados de um aplicativo, eles devem estar na forma de uma string. Usamos JSON.stringify() para transformar objetos JavaScript em strings.

Em seguida, usamos JSON.parse() do outro lado, para transformar os dados após a transmissão de volta para um objeto JavaScript para que possamos usá-los.

```js
var arr = [6, 4, 5, 6, 7, 7];

var obj = {
	author: "Christina Kopecky",
	title: "How to parse JSON objects",
	published: false
}

console.log("======== ARR EXAMPLE ==========");
console.log("orig arr=====>", arr);
console.log("stringified arr=====>", JSON.stringify(arr));
console.log("proof of type=====>", typeof JSON.stringify(arr));
console.log("parsed string=====>", JSON.parse(JSON.stringify(arr)));
console.log("proof of type=====>", typeo JSON.parse(JSON.stringify(arr)), "\n\n");
console.log("======== OBJ EXAMPLE ==========");
console.log("orig obj=====>", obj);
console.log("stringified obj=====>", JSON.stringify(obj));
console.log("proof of type=====>", typeof JSON.stringify(obj));
console.log("parsed string=====>", JSON.parse(JSON.stringify(obj)));
console.log("proof of type=====>", typeof JSON.parse(JSON.stringify(obj)), "\n\n");
```
## Novos métodos de Date
Houve dois novos métodos de objeto Date introduzidos no ES5 que são funcionalmente equivalentes. Ambos retornam a hora atual em milissegundos desde 1º de janeiro de 1970. Eles são Date.now() e new Date().valueOf().

```js
console.log(Date.now());
console.log(new Date().valueOf());
```

A maior diferença entre os dois métodos é que valueOf() é um método em uma instância do objeto Date e Date.now() é uma função estática do objeto Date.
## Getters e Setters
No ES5, somos apresentados à ideia de propriedades do acessador. Estas são funções cujo único propósito é obter ou definir um valor. Eles se parecem com propriedades padrão quando você os chama:

```js
let character = {
	first_name: "Darth",
	last_name: "Vader",

	get fullName() {
		return `${this.first_name} ${this.last_name}`;
	},
	set fullNane(str) {
		[this.first_name, this.last_name] = str.split(" ");
	}
};

console.log(character.fullName); // Darth Vader

character.fullName = "Luke Skywalker"

console.log(character.first_name);
console.log(character.last_name);
```