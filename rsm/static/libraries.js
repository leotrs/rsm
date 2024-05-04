// libraries.js
//
// Load external libraries dynamically
//

// Some of these settings are requried by pseudocode.js
window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true,
    }
}

// Use MathJax for beautiful math
export function loadMathJax() {
    const config = document.createElement('script');
    config.innerHTML = `window.MathJax = {
      options: {
        menuOptions: {
          settings: {
            inTabOrder: false
          }
        }
      }
    };`
    document.body.appendChild(config);

    const script = document.createElement('script');
    script.type = "text/javascript";
    script.id = "MathJax-script";
    script.src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js";
    document.body.appendChild(script);

    return new Promise((res, rej) => {
	script.onload = res;
	script.onerror = rej;
    });
}

// Render algorithms using pseudocode.js
// https://github.com/SaswatPadhi/pseudocode.js
export function loadPseudocode() {
    const script = document.createElement('script');
    script.type = "text/javascript";
    script.id = "pseudocode-script";
    script.src = "https://cdn.jsdelivr.net/npm/pseudocode@latest/build/pseudocode.min.js"
    document.body.appendChild(script);

    return new Promise((res, rej) => {
	script.onload = res;
	script.onerror = rej;
    });
};
