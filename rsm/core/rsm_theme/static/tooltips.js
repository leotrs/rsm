loadTooltips = function() {
    $("a.reference.internal").tooltipster({
        theme: 'tooltipster-shadow',
        functionInit: function(instance, helper) {
            target = $(helper.origin).attr("href");

            // make sure to escape any '.' in the id, otherwise jquery will think we are
            // trying to select a class instead!
            target = target.replaceAll(".", "\\.");

            tag = $(target).prop('tagName');
            classes = $(target)[0].classList;
            content = "";

            if (tag == "P") {
                content = $(target).html();


            } else if (tag == "SPAN") {
                content = $(target).parent().html();
            } else {
                switch(true) {
                case classes.contains("step"):
                    content = $(target).children(".statement").html();
                    break;
                }
            }

            instance.content($(content));

        }
    });
    MathJax.typeset();
}
