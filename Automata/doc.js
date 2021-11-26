
var intval = ""

function start_Int() {
    if (intval == 2) {
        intval = window.setInterval("start_clock()", 1000);
    }
    else {
        stop_Int();
    }
}

function stop_Int() {
    if (intval != 2) {
        window.clearInterval(intval);
        intval = "";
        document.formu.tiempo.value = "Tiempo detenido";
    }
}

function start_clock() {
    var d = new Date(); 
    var sw = "am";
    var h = d.getHours(); 
    var m = d.getMinutes() + "";
    var s = d.getSeconds() + "";
    if (h > 12) {
        h -= 12;
        sw = "pm";
    }
    if (mlength == 1) {
        m = "0" + m;
    }
    if (slength == 1) {
        s = "0" + s;
    }
    document.formu.tiempo.value = h + ":" + m + ":" + s + " " + sw;
}