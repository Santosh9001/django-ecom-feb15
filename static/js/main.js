$(document).ready(function(){    
    $(".btn").click(function() {
        $.ajax({
            url:'entity_name',
            type:'GET',
            data:{
                button_text: $(this).text()
            },
            success: function(response){
                $(".btn").text(response.seconds)
            }
        });
    });
});