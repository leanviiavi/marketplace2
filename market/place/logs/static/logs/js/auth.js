let local_machine_id = 3475;
let form_action = document.querySelector("#login");

function GenQR(){
    let qrcode = new QRCode(document.getElementById("login"), {
        text: "http://192.168.0.103:2000/auth/?id="+local_machine_id,
        width: 256,
        height: 256,
        colorDark : "#5868bf",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    });
}

GenQR();