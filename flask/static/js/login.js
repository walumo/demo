
function login(){
    var user = document.getElementById("username").value;
    var pass = document.getElementById("password").value;
    if(user !== "" && pass !== ""){
    var creds = [user, pass];
    }
    else{
        alert("Insufficient login data!");
    }
}