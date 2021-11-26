function Animal (nombre) {
  
}
class Perro extends Animal {
  hablar(nombre) {
    super.hablar();
    this.nombre = nombre;
    console.log(this.nombre + ' ladra.');
  }
}

var p = new Perro('Mitzie');
p.hablar();

switch(nombre){

}