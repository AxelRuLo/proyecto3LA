function Animal (nombre) {

  }
  class Perro extends Animal {
    hablar(nombre) {
      super.hablar();
      console.log(this.nombre + ' ladra.');
    }
  }
  
  var p = new Perro();
  p.hablar();
  
  switch(nombre){
  
  }