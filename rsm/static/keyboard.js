// keyboard.js
//
// Keyboard interaction
//

export function setup () {
    // Nagivation: next or previous
    document.addEventListener('keydown', (event) => {
        if (['j', 'J', 'k', 'K'].includes(event.key)) {
            event.preventDefault();
            const direction = ['j', 'J'].includes(event.key) ? "next" : "prev";
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

    // Basic actions on the currently focused element
    document.addEventListener('keydown', (event) => {
        if (event.key == ".") { toggleMenu(document.activeElement) }
    });
    document.addEventListener('keydown', (event) => {
        if (event.key == ",") { toggleCollapse(document.activeElement) }
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
            console.log("what to do here?");
        }
    });

    // Tooltips
    document.addEventListener('keydown', (event) => {
        if (event.key == "i") {
            toggleTooltip(document.activeElement);
        }
    });

}


function toggleTooltip(el) {
    if (!el.classList.contains("tooltipstered")) return;
    console.log($(el).tooltipster("status"));
    if ($(el).tooltipster("status").open) {
        $(el).tooltipster("close");
    } else {
        $(el).tooltipster("open");
    }
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
//         console.log(current);
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
    const coll = el.querySelector("& > .hr-collapse-zone > .hr-collapse");
    if (!coll) return;
    collapseHandrail(coll);
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
