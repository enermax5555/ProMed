//var app = new Vue({
//  el: '#app',
//  data:{
//    state: "close"
//  }
//});
//var search_icon = document.getElementById("search_icon");
//data:{
//state: "close"
//}
document.getElementById("search").style.display = 'none';
document.getElementById("search").style.display = 'block';
function validateHHMM(value, message) {
    var isValid = /^(0?[1-9]|1[012])(:[0-5]\d) [APap][mM]$/.test(value);

    if (isValid) {
        document.getElementById(message).style.display = "none";
    }else {
        document.getElementById(message).style.display= "inline";
    }

    return isValid;
}
console.log(validateHHMM())