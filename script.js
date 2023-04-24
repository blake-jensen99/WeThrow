console.log("test")

function displayMark() {
    console.log("test")
    var element = document.querySelector("#mark");
    element.classList.add("show");
}

function removeMark(){
    var element = document.querySelector("#mark");
    element.classList.remove("show");
}

function displayVid() {
    console.log("test")
    var element = document.querySelector("#vid");
    element.classList.add("show");
}

function removeVid(){
    var element = document.querySelector("#vid");
    element.classList.remove("show");
}

function displaySign(){
    var element = document.querySelector(".signup");
    element.classList.add("show");
}

function removeSign(){
    var element = document.querySelector(".signup");
    element.classList.remove("show");
}

function displayAdd(){
    var element = document.querySelector(".add_form");
    element.classList.add("show");
}

function removeAdd(){
    var element = document.querySelector(".add_form");
    element.classList.remove("show");
}