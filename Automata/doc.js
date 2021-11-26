function toDoSomething(){
    var object_1 = {
      nombre : "Pedro",
      edad : 20
    }


    do {
      i += 1;
      document.write(i);
    } while (i < 5);

    for (var i = 0; i < 9; i++) {
      n += i;
      mifuncion(n);
      if(n == 1){
        console.log("asdasdasd");
      }
    }

    while (n < 3) {
      n ++;
      x += n;
    }

    switch (expr) {
      case 'Naranjas':
        console.log('El kilogramo de naranjas cuesta $0.59.');
        break;
      case 'Manzanas':
        console.log('El kilogramo de manzanas cuesta $0.32.');
        break;
      case 'Platanos':
        console.log('El kilogramo de platanos cuesta $0.48.');
        break;
      case 'Cerezas':
        console.log('El kilogramo de cerezas cuesta $3.00.');
        break;
      case 'Mangos':
      case 'Papayas':
        console.log('El kilogramo de mangos y papayas cuesta $2.79.');
        break;
      default:
        console.log('Lo lamentamos, por el momento no disponemos de ' + expr + '.');
    }
  }

class potato{

}