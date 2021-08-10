$(document).ready(function(){
    $( "a" ).hover(function() {
        target = $( this ).attr("href");
        text = $( target + " .proposition-content" ).text();
        $( this ).css('cursor','pointer').attr('title', text);
    })
})
