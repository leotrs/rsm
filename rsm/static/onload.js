// onload.js
//
// Function to run when the entire document finishes loading
//

export function onload(underscore = false) {
    const dir = underscore ? '/_static/' : '/static/';
    import(dir + 'libraries.js').then((libs) => {
        libs.loadMathJax().then(() => {
            console.log('MathJax loaded!');
            libs.loadPseudocode().then(() => {
	        console.log('pseudocode loaded!');
	        const elements = $("pre.pseudocode");
	        if (elements.length) {
                    pseudocode.renderElement(elements[0], {lineNumber: true, noEnd: true});
	        }
	        import(dir + 'tooltips.js').then((tips) => {
                    tips.createTooltips();
                })
            }).catch((err) => {
	        console.error('Loading pseudocode FAILED!');
	        console.error(err);
            })
            import(dir + 'classes.js').then((cls) => {
                cls.setupClassInteractions();
            })
        }).catch((err) => {
	    console.error('Loading MathJax FAILED!');
	    console.error(err);
        })
    })
}
