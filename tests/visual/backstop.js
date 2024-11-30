module.exports = {
    "id": "backstop_default",
    "viewports": [
	// {
	//     "name": "phone_s",
	//     "width": 320,
	//     "height": 480
	// },
	// {
	//     "label": "phone_l",
	//     "width": 375,
	//     "height": 667
	// },
	{
	    "name": "tablet_v",
	    "width": 568,
	    "height": 1024
	},
	{
	    "name": "tablet_h",
	    "width": 1024,
	    "height": 768
	},
	{
	    "label": "web_s",
	    "width": 1440,
	    "height": 900
	}
	// {
	//     "label": "web_l",
	//     "width": 1920,
	//     "height": 1080
	// }
    ],
    "onBeforeScript": "puppet/onBefore.js",
    "onReadyScript": "puppet/onReady.js",
    "scenarios": [
	{
	    "label": "empty",
	    "url": "http://127.0.0.1:5501/empty.html"
	},
	{
	    "label": "paragraph",
	    "url": "http://127.0.0.1:5501/paragraph.html"
	},
	{
	    "label": "theorem_proof",
	    "url": "http://127.0.0.1:5501/theorem_proof.html",
	    "readyEvent": "MathJax ready"
	},
	{
	    "label": "hover_title",
	    "url": "http://127.0.0.1:5501/paragraph.html",
	    "hoverSelector": ".handrail"
	},
	{
	    "label": "click_title",
	    "url": "http://127.0.0.1:5501/paragraph.html",
	    "clickSelector": ".handrail"
	},
	{
	    "label": "ref",
	    "url": "http://127.0.0.1:5501/ref.html"
	},
	{
	    "label": "hover_ref",
	    "url": "http://127.0.0.1:5501/ref.html",
	    "onReadyScript": "openTooltips.js",
	    "readyEvent": "tooltip open"
	}

    ],
    "paths": {
	"bitmaps_reference": "backstop_data/bitmaps_reference",
	"bitmaps_test": "backstop_data/bitmaps_test",
	"engine_scripts": "backstop_data/engine_scripts",
	"html_report": "backstop_data/html_report",
	"ci_report": "backstop_data/ci_report"
    },
    "report": ["browser", "CI"],
    "engine": "puppeteer",
    "engineOptions": {
	"args": ["--no-sandbox"]
    },
    "asyncCaptureLimit": 5,
    "asyncCompareLimit": 50,
    "debug": false,
    "debugWindow": false
}
