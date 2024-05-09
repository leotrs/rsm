// onload.js
//
// Function to run when the entire document finishes loading
//



export function onload(path = "/static/") {
    let lsp_ws;
    import(path + 'libraries.js').then((libs) => {
        libs.loadMathJax().then(() => {
            console.log('MathJax loaded!');

	    // window.MathJax = {
	    //     loader: {load: ['[tex]/mathtools']},
	    //     tex: {packages: {'[+]': ['mathtools']}}
	    // };

            libs.loadPseudocode().then(() => {
	        console.log('pseudocode loaded!');
	        const elements = $("pre.pseudocode");
	        if (elements.length) {
                    pseudocode.renderElement(elements[0], {lineNumber: true, noEnd: true});
	        }
	        import(path + 'tooltips.js').then((tips) => {
                    tips.createTooltips();
                })
            }).catch((err) => {
	        console.error('Loading pseudocode FAILED!');
	        console.error(err);
            })
            import(path + 'classes.js').then((cls) => {
                cls.setupClassInteractions();
            })
        }).catch((err) => {
	    console.error('Loading MathJax FAILED!');
	    console.error(err);
        })
    });

    lsp_ws = new WebSocket("ws://127.0.0.1:1234");
    lsp_ws.onerror = function(error) {console.log(`[error]`)};
    lsp_ws.onclose = function(event) {
        if (event.wasClean) {
            console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        } else {
            console.log('[close] Connection died');
        }
    };
    lsp_ws.onopen = function(e) {
        console.log("[open] Connection established");
        lsp_ws.send(JSON.stringify({
            "jsonrpc": "2.0",
            "method": "initialize",
            "id": 1,
            "params": {
	        "processId": null,
	        "capabilities":  {}
            }
        }));
        const src = $("body").children(".rsm-source");
        lsp_ws.send(JSON.stringify({
            "jsonrpc" : "2.0",
            "method" : "textDocument/didOpen",
            "params": {
                "textDocument": {
                    "languageId": "rsm",
                    "text": src.text(),
                    "uri": "file://src/hello.rsm",
                    "version": 1
                }
           }
        }))
    };

    return lsp_ws;
}
