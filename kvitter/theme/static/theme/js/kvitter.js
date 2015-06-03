
$(document).ready(function(){
 
    $(".add-likes-link").click(function(event) {
        event.preventDefault();
        var message_id = $(this).data("messageid");
        var likes_element_id = "#id-likes-for-message-" + message_id;
        $.ajax({
           url: "/add_likes_url/" + message_id + "/add_likes"
       })
       .done(function(data) {
        var likes_updated = data['likes_updated'];
        var likes_element_id = "#id-likes-for-message-" + message_id;
        $(likes_element_id).html(likes_updated);
        });
    });
});