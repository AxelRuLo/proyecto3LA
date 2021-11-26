var intval = ""

function start_Int() {
    if (intval == "") {
        intval = window.setInterval("start_clock()", 1000);
    }
    else {
        stop_Int();
    }
}

function stop_Int() {
    if (intval != "") {
        window.clearInterval(intval);
        intval = "";
        document.formu.tiempo.value = "Tiempo detenido";
    }
}

function start_clock() {
    var d = new Date(); // Creamos una variable "d" de tipo "Date".
    var sw = "am";
    var h = d.getHours(); // Asignamos a "h" la horas obtenidas de "d".
    var m = d.getMinutes() + "";
    var s = d.getSeconds() + "";
    if (h > 12) {
        h -= 12;
        sw = "pm";
    }
    if (m.length == 1) {
        m = "0" + m;
    }
    if (s.length == 1) {
        s = "0" + s;
    }
    document.formu.tiempo.value = h + ":" + m + ":" + s + " " + sw;
}