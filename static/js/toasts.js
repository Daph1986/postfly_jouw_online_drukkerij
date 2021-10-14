// ----------------------- Bootstrap toast initialize  -----------------------

let toastMessage = [].slice.call(document.querySelectorAll('.toast'));   
let message = toastMessage.map(function (toastEl) {
    return new bootstrap.Toast(toastEl).show();
});