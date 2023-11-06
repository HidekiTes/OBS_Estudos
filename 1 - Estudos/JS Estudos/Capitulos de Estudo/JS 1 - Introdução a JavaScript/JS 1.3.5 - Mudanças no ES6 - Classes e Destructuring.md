## Classes
As classes atuam como açúcar sintático sobre os protótipos de JavaScript. Em vez de herança prototípica, eles usam herança clássica com a palavra-chave extends. No geral, isso apenas reduz a quantidade de código e melhora um pouco.

```js
class StarWarsCharacter{
	constructor(attributes) {
		this.name = attributes.name;
		this.age = attributes.age;
		this.homePlanet = attributes.homePlanet;
	}
	getCharacter = () => `${this.name} is ${this.age} years old and is from ${this.homePlanet}.`;
}

const luke = new StarWarsCharacter({ name: "Luke Skywalker", age: 23, homePlanet: "Tatooine"});

luke.getCharacter();

class Heroes extends StarWarsCharacter {
	constructor(attributes) {
		super(attributes);
		this.favoriteVehicle = attributes.favoriteVehicle;
	}
	getFavoriteVehicle = () => `${this.name} is ${this.age} and their favorite vehicle is the ${this.favoriteVehicle}`;
}

const hans = new Heroes({ name: "Hans Solo", age: 35, favoriteVehicle: "Millennium Falcon"});

console.log(hans.getFavoriteVehicle());```
## Destructuring
A desestruturação de objetos é uma ótima maneira de reduzir a confusão de código para torná-lo mais palatável. Ele nos permite “descompactar” um objeto e usar esse valor descompactado como a variável à qual nos referimos posteriormente no código.

```js 
const state = {
	name: "Luke Skywalker",
	age: 22,
	dark_side: false
}

console.log("before destructuring");

console.log(state.name); // notice the prefixed object name prior to each property
console.log(state.age); // destructuring gets rid of this
console.log(state.dark_side);

const { name, age, dark_side } = state;

console.log("after destructuring");
console.log(name); // we can access using just the property name now!
console.log(age);
console.log(dark_side);
```

Na seção “antes da desestruturação”, temos que usar o nome do objeto além da propriedade que queremos para acessar essa propriedade. Podemos desestruturá-lo retirando as propriedades, colocando-o entre chaves e definindo-o com o nome do objeto.

Certifique-se de usar a palavra-chave const na frente das chaves. Ele nos permite acessar essas propriedades como variáveis, em vez de usar a notação de ponto no próprio objeto.

```js
const arr_state = [ "Luke Skywalker", 22, false];

console.log("before destructuring");

console.log(arr_state[0]); // notice the index number in bracket notation
console.log(arr_state[1]); // destructuring gets rid of this
console.log(arr_state[2]);

console.log("\n\n\n")
const [ name, age, dark_side ] = arr_state; // assign a variable to each of the indexes in the array

console.log("after destructuring");
console.log(name); // we can access using just the variable name we created now!
console.log(age);
console.log(dark_side);
```

===**Continuação - [[JS 1.3.6 - Mudanças no ES6 - Let-Const e Promises]]**===