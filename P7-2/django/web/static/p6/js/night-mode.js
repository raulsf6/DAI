$(document).ready(function () {
    $('#light').hide()
})

$('#night').click(function () {
    
    $('body').addClass("bg-dark");
    $('#list-row').addClass("text-light");
    $('#elements').children().addClass("list-group-item-dark");
    $('a.page-link').addClass("bg-dark");
    $('footer').addClass("bg-secondary");

    $(this).hide()
    $('#light').show()
   
});


$('#light').click(function () {
    
    $('body').removeClass("bg-dark");
    $('#list-row').removeClass("text-light");
    $('#elements').children().removeClass("list-group-item-dark");
    $('a.page-link').removeClass("bg-dark");
    $('footer').removeClass("bg-secondary");

    $(this).hide();
    $('#night').show();
    
});
