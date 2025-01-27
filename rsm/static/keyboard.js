// keyboard.js
//
// Keyboard interaction
//
import { collapseHandrail, collapseAll } from '/static/handrails.js';

export function setup () {
    // Nagivation: next or previous
    document.addEventListener('keydown', (event) => {
        if (['j', 'k'].includes(event.key)) {
            event.preventDefault();
            const direction = event.key == 'j' ? "next" : "prev";
            focusPrevOrNext(direction);
        }
    });

    // Nagivation: up or down
    // document.addEventListener('keydown', (event) => {
    //     if (['h', 'H', 'l', 'L'].includes(event.key)) {
    //         event.preventDefault();
    //         const direction = ['h', 'H'].includes(event.key) ? "up" : "down";
    //         focusUpOrDown(direction);
    //     }
    // });

    // Navigation: back to top
    document.addEventListener('keydown', (event) => {
        if (event.key == "H") { focusTop() }
    });

    // Basic actions on the currently focused element
    document.addEventListener('keydown', (event) => {
        if (event.key == ".") { toggleMenu(document.activeElement) }
    });
    document.addEventListener('keydown', (event) => {
        if (event.key == ",") { toggleCollapse(document.activeElement) }
    });
    document.addEventListener('keydown', (event) => {
        if (event.key == ";") { toggleCollapseAll(document.activeElement) }
    });
    document.addEventListener('keydown', (event) => {
        if (event.key == "z") { scrollToMiddle(document.activeElement) }
    });

    // Interaction with the menu of the currently focused element
    document.addEventListener('keydown', (event) => {
        if (["ArrowUp", "ArrowDown"].includes(event.key)) {
            event.preventDefault();
            menuUpOrDown(document.activeElement, event.key == "ArrowUp" ? "up" : "down");
        }
    });
    document.addEventListener("keyup", (event) => {
        event.preventDefault();
        if (event.keyCode === 13) {
            event.preventDefault();
            executeActiveMenuItem(document.activeElement);
        }
    });

    // Tooltips
    document.addEventListener('keydown', (event) => {
        if (event.key == "i") {
            toggleTooltip(document.activeElement);
        }
    });

}


function focusTop() {
    const focusable = getFocusableElements();
    focusable[0].focus();
    scrollToMiddle(focusable[0], "up");
}


function toggleTooltip(el) {
    if (!el.classList.contains("tooltipstered")) return;
    if ($(el).tooltipster("status").open) {
        $(el).tooltipster("close");
    } else {
        $(el).tooltipster("open");
    }
}


function executeActiveMenuItem(el) {
    const menu = el.querySelector("& > .hr-menu-zone > .hr-menu");
    if (!menu) return;
    const activeItems = menu.querySelectorAll("& > .hr-menu-item.active");
    if (activeItems.length == 0) return;
    if (activeItems.length > 1) {console.log("more than one active items, ignoring"); return};
    const cls = Array.from(activeItems[0].classList).filter(cls => cls !== 'active' && cls !== 'hr-menu-item');
    if (cls.length == 0) {console.log(`unknown item`); return};
    if (cls.length > 1) {console.log(`item has too many classes, ignoring`); return};
    console.log(cls);
}


function menuUpOrDown(el, direction) {
    const menu = el.querySelector("& > .hr-menu-zone");
    if (!getComputedStyle(menu).display == "none") return;

    const qry = `
      & > .hr-menu > .hr-menu-item:hover,
      & > .hr-menu > .hr-menu-item:active,
      & > .hr-menu > .hr-menu-item:focus,
      & > .hr-menu > .hr-menu-item.active
    `
    const currentItem = menu.querySelector(qry);
    const allItems = Array.from(menu.querySelectorAll("& > .hr-menu > .hr-menu-item"));

    let index = allItems.indexOf(currentItem);
    if (index == -1) index = 0;

    if (!currentItem || index == -1) {
        index = 0
    } else if (direction == "down") {
        index = (index + 1) % allItems.length;
    } else if (direction == "up") {
        index = (index - 1 + allItems.length) % allItems.length;
    }
    if (currentItem) currentItem.classList.remove("active");
    allItems[index].classList.add("active");
}


// function findFirstDescendantInArray(el, array) {
//     const stack = [...el.children];

//     while (stack.length > 0) {
//         const current = stack.pop();
//         if (array.includes(current)) { return current };
//         for (let child of current.children) {
//             stack.push(child);
//         }
//     }

//     return null;
// }


// function focusUpOrDown(direction) {
//     const focusableElements = getFocusableElements();
//     let index = focusableElements.indexOf(document.activeElement);
//     let current = document.activeElement;
//     if (index !== -1) {
//         if (direction == "up") {
//             do {
//                 current = current.parentElement;
//             } while (current && !focusableElements.includes(current));
//         } else {
//             current = findFirstDescendantInArray(current, focusableElements);
//         }
//     } else { index = 0; }

//     if (current) {
//         current.focus();
//         maybeScrollToMiddle(current, direction);
//     }
// }


function focusPrevOrNext(direction) {
    const focusableElements = getFocusableElements();
    let index = focusableElements.indexOf(document.activeElement);
    if (index !== -1) {
        if (direction == "next") {
            do { index = (index + 1) % focusableElements.length; }
            while ( !isFocusable(focusableElements[index]) );
        } else {
            do { index = (index - 1 + focusableElements.length) % focusableElements.length; }
            while ( !isFocusable(focusableElements[index]) );
        }
    } else { index = 0; }
    focusableElements[index].focus();
    maybeScrollToMiddle(focusableElements[index], direction == "next" ? "down" : "up");
}


function getFocusableElements() {
    return Array.from(
        document.querySelector(".manuscriptwrapper").querySelectorAll('[href], [tabindex]:not([tabindex="-1"])')
    );
}


function toggleCollapse(el) {
    if (!el.classList.contains("hr")) return;
    const coll1 = el.querySelector("& > .hr-collapse-zone > .hr-collapse");
    const coll2 = el.querySelector("& > .hr-menu-zone .collapse-subproof:not(.disabled)");
    if (!coll1 && !coll2) return;
    collapseHandrail(el);
}


function toggleCollapseAll(el) {
    console.log(el);
    if (!el.classList.contains("hr")) return;
    const collAll = el.querySelector(`
        & > .hr-menu-zone .collapse-all:not(.disabled),
        & > .hr-menu-zone .expand-all:not(.disabled)
    `);
    const withinSubproof = el.classList.contains("step");
    if (collAll) collapseAll(el, withinSubproof);
}


function toggleMenu(el) {
    if (!el.classList.contains("hr")) return;
    const menu = el.querySelector("& > .hr-menu-zone");
    if (!menu) return;
    const style = getComputedStyle(menu);
    if (style.display == "none") menu.style.display = "block";
    else if (style.display == "block") {
        menu.querySelectorAll("& > .hr-menu > .hr-menu-item").forEach(it => it.classList.remove("active"));
        menu.style.display = "none"
    };
}


function isFocusable(el) {
    if (el.classList.contains("hr-collapsed") && !el.classList.contains("hide")) return true;
    if (el.closest(".hr-collapsed") || el.closest(".hide")) return false;
    return true;
}


function scrollToMiddle(element) {
    const rect = element.getBoundingClientRect();
    const elementCenterY = rect.top + rect.height / 2;
    const viewportCenterY = window.innerHeight / 2;
    const offset = elementCenterY - viewportCenterY;

    window.scrollBy({
        top: offset,
        behavior: 'smooth',
    });
}


function maybeScrollToMiddle(element, direction) {
    const rect = element.getBoundingClientRect();
    const elementTop = rect.top;
    const elementHeight = rect.height;
    const elementCenterY = elementTop + elementHeight / 2;
    const viewportHeight = window.innerHeight;
    const viewportCenterY = viewportHeight / 2;
    const offset = elementCenterY - viewportCenterY;
    const farEnoughFromCenter = Math.abs(offset) > 48;

    let scrollAmount;
    if (elementHeight > viewportHeight) {
        // element taller than viewport: just align its top with the top of the viewport
        scrollAmount = -elementTop;
    } else {
        // If scrolling would push the element's top above the viewport,
        // limit the scroll to align the top of the element with the top of the viewport
        if (elementTop + offset < 0) { scrollAmount = -elementTop }
        // Otherwise, scroll to center the element (if far enough from center)
        else if (farEnoughFromCenter) { scrollAmount = offset }
        else { return };
    }

    if (direction == "down" && scrollAmount < 0) return;
    if (direction == "up" && scrollAmount > 0) return;
    window.scrollBy({
        top: scrollAmount,
        behavior: 'smooth',
    });
}
