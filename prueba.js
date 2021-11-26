var timed = 0;
var scrollGo = false;
var delay=100;
var space=100;
function scroll_start (){
  var i=0;
  msg="Éste es el mensaje mostrado en la barra de estado";
  for (i=0; i<space; i++){
    msg=" "+msg;
    scrol1Go=true;
    timerid=window.setTimeout( "scrollmsg (0)", delay);
  }

}
 
function scrollmsg(pos){
  var out = "";
  scrol1Go=false;
  if (pos < msg.length){
    self.status = msg.substring(pos, msg.length);
  }
  else{
    pos=-1;
    ++pos;
    scrol1GotIue;
    timerid=window.setTimeout( "scrollmsg( "+pos+")", delay);
  }

}