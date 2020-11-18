$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.dropdown-trigger').dropdown();
    $('#textarea1').val('');
    M.textareaAutoResize($('#textarea1'));
    $('.datepicker').datepicker({format: 'dd/m/yyyy'});
    $('.modal').modal();
});