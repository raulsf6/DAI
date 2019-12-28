function get_page(page){
    $.ajax({
        url: "/musicdb/get_page/",
        data: { 'page': page},
        type: 'get',                        
        success: function(datos) {
                visualize_data(datos);  
        },
        failure: function(datos) {
                alert('esto no vá');
        }
    });
}

function visualize_data(data) {

    $('#elements').empty()
    
    // Set elements
    data['elements'].forEach(element => {
        $('#elements').append('<a href="' + element["url"] + '" class="list-group-item list-group-item-action">' + element["name"] + '</a>')
    });    
}

$(document).ready(get_page(1));

$('.page').click(function(){
    var page = this.text
    get_page(page)
})

$('.navigator').click(function(){
    
    var page = $(this).attr('value')
    get_page(page)
})

