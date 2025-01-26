// minimap.js
//
// Table of contents and floating minimap.
//

export function setup() {

    // Table of contents
    const items = document.querySelectorAll('ul.contents li.item');
    const num_items = items.length;
    items.forEach((item, idx) => {
	item.addEventListener('mouseenter', () => {
	    let percent = (idx + 1) / num_items * 100;
            document.getElementById("stop-follow-mouse-1").setAttribute("offset", `${percent}%`);
	    document.getElementById("stop-follow-mouse-2").setAttribute("offset", `${percent}%`);
	});
    });

    // Floating minimap
    window.addEventListener('scroll', () => {
	const toc_mm = document.querySelector(".toc-wrapper > .minimap");
	const float_mm = document.querySelector(".float-minimap-wrapper > .minimap");
	if (withinView(toc_mm, false)) {
	    float_mm.classList.add("hide");
	} else {
	    float_mm.classList.remove("hide");
	};
    });
    window.addEventListener('scroll', () => {
	const mm = document.querySelector(".float-minimap-wrapper > .minimap");
	if (mm.classList.contains("hide")) return;

	const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
	const sections = document.querySelectorAll('section');
	const lastInViewport = Array.from(sections).findLast(sec => withinView(sec, true));
	const circle = document.querySelector(`#mm-${lastInViewport?.id}`)

	let percent;
	if (circle && mm) {
	    const circle_rect = circle.getBoundingClientRect();
	    const mm_rect = mm.getBoundingClientRect();
	    percent = (circle_rect.bottom - mm_rect.top + 12) / mm.offsetHeight * 100;
	} else {
	    percent = 0;
	};
	document.getElementById("stop-follow-scroll-1").setAttribute("offset", `${percent}%`);
	document.getElementById("stop-follow-scroll-2").setAttribute("offset", `${percent}%`);
    });

}


function withinView(el, top = true) {
    const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
    const rect = el.getBoundingClientRect();
    if (top) {
	return rect.top < viewportHeight / 2 && rect.bottom > 0;
    } else {
	return rect.top < viewportHeight && rect.bottom > 0;
    };
};
