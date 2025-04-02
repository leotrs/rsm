// onload.js
//
// Function to run when the entire document finishes loading
//

export async function onload(root = null, path = "/static/") {
    console.log("onload");
    if (!root) { root = document };

    try {
        const libs = await import(`${path}libraries.js`);

        // Icons
        try {
            const icons = await import(`${path}icons.js`);
            icons.setup(root, local);
        } catch (err) {
            console.error("Loading icons.js FAILED!", err);
        }

        // MathJax
        try {
            const math = await libs.loadMathJax();
        } catch (err) {
            console.error("Loading MathJax FAILED!", err);
        }

        // Handrails
        try {
            const hr = await import(`${path}handrails.js`);
            hr.setup();
        } catch (err) {
            console.error("Loading handrails.js FAILED!", err);
        }

        // Keyboard interaction
        try {
            const kbd = await import(`${path}keyboard.js`);
            kbd.setup();
        } catch (err) {
            console.error("Loading keyboard.js FAILED!", err);
        }

        // Pseudocode
        try {
            await libs.loadPseudocode();

            const elements = document.querySelectorAll("pre.pseudocode");
            if (elements.length) {
                pseudocode.renderElement(elements[0], {
                    lineNumber: true,
                    noEnd: true,
                });
            }
        } catch (err) {
            console.error("Loading pseudocode FAILED!", err);
        }

        // Minimap
        try {
            const mm = await import(`${path}minimap.js`);
            mm.setup();
        } catch (err) {
            console.error("Loading minimap.js FAILED!", err);
        }

        // Tooltipster
        try {
            const tips = await import(`${path}tooltips.js`);
            tips.createTooltips();
        } catch (err) {
            console.error("Loading tooltips FAILED!", err);
        }

    } catch (err) {
        console.error("An error occurred during initialization:", err);
    }
}
