/*function Actualizar(codigo) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/alumno/" + codigo, true);
    xhttp.send();
    xhttp.onload = function (resp) {
        var RESULT = resp['currentTarget']['response'];
        var ALUMNO = JSON.parse(RESULT)[0];
        $('#Actualizar #codigo').val(ALUMNO['codigo']);
        $('#Actualizar #nombre').val(ALUMNO['nombre']);
        $('#Actualizar #apellido').val(ALUMNO['apellido']);
        $('#Actualizar #edad').val(ALUMNO['edad']);
        console.log(ALUMNO);
    };

}*/