$(document).ready(function() {
    // $( "div.step-number-container" ).hover(function() {
    //     // this is the parent step, we do not want to do anything to it because the
    //     // mouse just hovered over its only step-number-container. We want to go up the
    //     // step hierarchy starting from it.
    //     parents = $( this ).parents( "div.step" );
    //     for (p of parents) {
    //         $( p ).find( "div.step-number-container" ).first().addClass("hover");
    //     }
    // }, function() {
    //     parents = $( this ).parents( "div.step" );
    //     for (p of parents) {
    //         $( p ).find( "div.step-number-container" ).first().removeClass("hover");
    //     }
    // });

    $( "div.step" ).hover(function() {
        console.log('foo');
        $( this ).children( "div.tombstone-container" ).css("display", "flex");
    }, function() {
        console.log('bar');
        $( this ).children( "div.tombstone-container" ).css("display", "none");
    })
});
