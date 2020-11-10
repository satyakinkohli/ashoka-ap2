function openForm_Mail() {
    document.getElementById("Form_Initial").style.display = "none";
    document.getElementById("Form_Mail").style.display = "block";
}

function openForm_Initial() {
    document.getElementById("Form_Initial").style.display = "block";
    document.getElementById("Form_Mail").style.display = "none";
    document.getElementById("Form_Signup").style.display = "none";
}

function openForm_Signup() {
    document.getElementById("Form_Initial").style.display = "none";
    document.getElementById("Form_Signup").style.display = "block";
}

function closeForm() {
    document.getElementById("Form_Mail").style.display = "none";
    document.getElementById("Form_Initial").style.display = "none";
    document.getElementById("Form_Signup").style.display = "none";
}

function goback() {
    document.getElementById("Form_Mail").style.display = "none";
    document.getElementById("Form_Initial").style.display = "block";
    document.getElementById("Form_Signup").style.display = "none";
}