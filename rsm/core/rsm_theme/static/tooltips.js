$(document).ready(function() {

    $("a.reference.internal").tooltipster({
        theme: 'tooltipster-shadow',
        functionInit: function(instance, helper) {
            target = $(helper.origin).attr("href");

            // make sure to escape any '.' in the id, otherwise jquery will think we are
            // trying to select a class instead!
            target = target.replaceAll(".", "\\.");

            classes = $(target)[0].classList;
            content = "";
            switch(true) {
            case classes.contains("step"):
                content = $(target).children(".statement").html();
                instance.content($(content));
                break;
            }

            MathJax.typeset();
        }
    });



});
