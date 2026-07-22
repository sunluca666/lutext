function showtext(){
    document.getElementById("text").innerHTML="新的文本";
}

async function gettext(){
    var response = await fetch("http://127.0.0.1:8000/test");
    var data = await response.text();
    document.getElementById("text").innerHTML = data;
}