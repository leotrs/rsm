$(document).ready(function() {
    $( "p.step-narrow" ).on("click", function() {
	console.log("narrow was pressed from " + this);
	step = $( this ).closest("div.step");
	step.siblings().css("display", "none");
    });
});
