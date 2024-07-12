// -------------------- Country select input color --------------------
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#70707086');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#70707086');
    } else {
        $(this).css('color', '#000');
    }
});