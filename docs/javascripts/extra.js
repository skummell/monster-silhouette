/* 
    Scrollable Grids !

    Turn Grid Admonitions into slides by treating each row of the Grid as a Slide
*/

/* 

    Usage : 

    !!! grid col single "" // For best results

        !!! grid scrollable "Columns as slides"
            First column — this is slide 1.

            Second column — slide 2.
            
            Third column — slide 3.

    ??? cards scrollable "Cards as slides"
        - Card one
        - Card two
        - Card three

*/

(function () {
    const SEL = '.admonition.scrollable, details.scrollable';

    function readColumnCount(el) {
        // Read from the container if it's a grid
        const s = getComputedStyle(el);
        if (s.display.includes('grid') && s.gridTemplateColumns && s.gridTemplateColumns !== 'none') {
            return Math.max(1, s.gridTemplateColumns.trim().split(/\s+/).length);
        }
        // Otherwise, maybe the inner UL is the grid
        const ul = el.querySelector(':scope > ul, :scope > ol');
        if (ul) {
            const us = getComputedStyle(ul);
            if (us.display.includes('grid') && us.gridTemplateColumns && us.gridTemplateColumns !== 'none') {
                return Math.max(1, us.gridTemplateColumns.trim().split(/\s+/).length);
            }
        }
        // Fallback to class detection
        if (el.classList.contains('single')) return 1;
        if (el.classList.contains('two')) return 2;
        if (el.classList.contains('three')) return 3;
        if (el.classList.contains('multi-col')) return 3;
        return 2;
    }

    function collectItems(container) {
        const items = [];
        Array.from(container.children).forEach(c => {
            if (c.matches(':scope > ul, :scope > ol')) {
                Array.from(c.children).forEach(li => items.push(li));
            } else if (!c.matches(':scope > summary') && !c.matches(':scope > .admonition-title') &&
                       !c.matches('.scrollable-viewport') && !c.matches('.scrollable-nav')) {
                items.push(c);
            }
        });
        return items;
    }

    function setup(container) {
        if (container.dataset.scrollableInit === '1') { resize(container); return; }

        // Read column count BEFORE we override layout
        const cols = readColumnCount(container);
        const items = collectItems(container);
        if (items.length === 0) return;

        // Neutralize the grid layout on the container (we wrap items now)
        container.style.display = 'block';

        // Group items into rows of `cols` items each
        const slides = [];
        for (let i = 0; i < items.length; i += cols) {
            slides.push(items.slice(i, i + cols));
        }

        // Detach items and build slides
        items.forEach(el => el.remove());

        const track = document.createElement('div');
        track.className = 'scrollable-track';

        slides.forEach(slideItems => {
            const slide = document.createElement('div');
            slide.className = 'scrollable-slide';
            slide.style.gridTemplateColumns = `repeat(${cols}, minmax(0, 1fr))`;
            slideItems.forEach(el => slide.appendChild(el));
            track.appendChild(slide);
        });

        const viewport = document.createElement('div');
        viewport.className = 'scrollable-viewport';
        viewport.appendChild(track);

        // Nav is OUTSIDE the viewport, directly in the container
        const nav = document.createElement('div');
        nav.className = 'scrollable-nav';
        nav.innerHTML = `
            <button type="button" class="scrollable-prev" aria-label="Previous slide">‹</button>
            <button type="button" class="scrollable-next" aria-label="Next slide">›</button>`;

        container.appendChild(viewport);
        container.appendChild(nav);

        // Single slide → no nav needed
        if (slides.length <= 1) nav.style.display = 'none';

        const prev = nav.querySelector('.scrollable-prev');
        const next = nav.querySelector('.scrollable-next');

        prev.addEventListener('click', () => {
            viewport.scrollBy({ left: -viewport.clientWidth, behavior: 'smooth' });
        });
        next.addEventListener('click', () => {
            viewport.scrollBy({ left: viewport.clientWidth, behavior: 'smooth' });
        });

        const updateNav = () => {
            prev.disabled = viewport.scrollLeft <= 2;
            next.disabled = viewport.scrollLeft + viewport.clientWidth >= viewport.scrollWidth - 2;
        };
        viewport.addEventListener('scroll', updateNav, { passive: true });
        prev.disabled = true;

        container.dataset.scrollableInit = '1';
        requestAnimationFrame(() => resize(container));
    }

    function resize(container) {
        if (container.matches('details') && !container.open) return;
        const viewport = container.querySelector(':scope > .scrollable-viewport');
        const track = viewport && viewport.querySelector(':scope > .scrollable-track');
        if (!track) return;

        Array.from(track.children).forEach(s => { s.style.height = ''; });
        let maxH = 0;
        Array.from(track.children).forEach(s => {
            maxH = Math.max(maxH, s.scrollHeight);
        });
        track.style.height = maxH + 'px';
    }

    function run() { document.querySelectorAll(SEL).forEach(setup); }
    let t; function schedule() { clearTimeout(t); t = setTimeout(run, 80); }

    document.addEventListener('DOMContentLoaded', schedule);
    window.addEventListener('load', schedule);
    window.addEventListener('resize', schedule);
    document.addEventListener('toggle', schedule, true);
    if (window.document$ && window.document$.subscribe) window.document$.subscribe(schedule);
})();

/* Tooltips */

/* 
    Apply Tooltips to Admonitions !
    Apply Tooltips to Tabs !
*/

/* 

    ??? cards "Click to expand"
        <!-- tooltip: Shows the full card layout for the UI screen -->

        - Card one
        - Card two  

    !!! grid "Layout"
        <!-- tooltip: Two-column grid matching the card-set visual -->

        Content here.

*/

/* 
    Apply Tooltips to Tabs
*/

/*
    Usage:

    === "First Tab"
        <!-- tooltip: Shows the first view -->

        Content of the first tab.

    === "Second Tab"
        <!-- tooltip: Alternate view, read-only -->

        Content of the second tab.

*/

(function () {
    function findTooltip(el, deep) {
        if (!el) return null;
        // 1) Direct child comment
        for (const node of el.childNodes) {
            if (node.nodeType === Node.COMMENT_NODE) {
                const m = node.textContent.trim().match(/^tooltip:\s*(.+)$/i);
                if (m) return m[1];
            }
        }
        // 2) Deep search fallback
        if (deep) {
            const walker = document.createTreeWalker(el, NodeFilter.SHOW_COMMENT);
            while (walker.nextNode()) {
                const m = walker.currentNode.textContent.trim().match(/^tooltip:\s*(.+)$/i);
                if (m) return m[1];
            }
        }
        return null;
    }

    // Admonition Tooltips
    function applyAdmonitionTooltips() {
        document.querySelectorAll('details, .admonition').forEach(function (el) {
            let target;
            if (el.tagName === 'DETAILS') {
                target = el.querySelector(':scope > summary');
            } else {
                target = el.querySelector(':scope > .admonition-title') || el;
            }
            if (!target) return;

            // Strip any stale title off the container itself
            if (el.hasAttribute('title')) el.removeAttribute('title');

            const text = findTooltip(el, true);
            if (!text) return;

            if (target.getAttribute('title') !== text) {
                target.setAttribute('title', text);
            }
        });
    }

    // Tab Tooltips 
    function applyTabTooltips() {
        document.querySelectorAll('.tabbed-set').forEach(function (tabset) {
            const labels = tabset.querySelectorAll(':scope > .tabbed-labels > label');
            const blocks = tabset.querySelectorAll(':scope > .tabbed-content > .tabbed-block');
            labels.forEach(function (label, i) {
                // Direct-only search — prevents nested admonition comments from bleeding into tab labels
                const text = findTooltip(blocks[i], false);
                if (text && label.getAttribute('title') !== text) {
                    label.setAttribute('title', text);
                }
            });
        });
    }

    // Let Link Tooltips win over Glossary
    function linkTooltipsWin() {
        document.querySelectorAll('a[title], a[data-md-tooltip]').forEach(function (a) {
            a.querySelectorAll('abbr').forEach(function (abbr) {
                if (abbr.hasAttribute('title') || abbr.hasAttribute('data-md-tooltip')) {
                    abbr.removeAttribute('title');
                    abbr.removeAttribute('data-md-tooltip');
                    abbr.classList.add('link-tooltip-clean'); /* Gets rid of glossary underline */
                }
            });
        });
    }

    // Get rid of Glossary tooltips on Titles 
    function stripGlossaryInTitles() {
        const containers = document.querySelectorAll(
            '.md-typeset h1, .md-typeset h2, .md-typeset h3, .md-typeset h4, .md-typeset h5, .md-typeset h6, ' +
            '.tabbed-labels > label, ' +
            '.admonition-title, ' +
            'details > summary'
        );

        containers.forEach(function (container) {
            container.querySelectorAll('abbr').forEach(function (abbr) {
                const span = document.createElement('span');
                span.className = 'title-abbr-clean';
                span.textContent = abbr.textContent;
                abbr.replaceWith(span);
            });
        });
    }

    function run() {
        applyAdmonitionTooltips();
        applyTabTooltips();
        linkTooltipsWin();
        stripGlossaryInTitles();
    }

    let t;
    function schedule() { clearTimeout(t); t = setTimeout(run, 60); }

    document.addEventListener('DOMContentLoaded', schedule);
    window.addEventListener('load', schedule);
    document.addEventListener('toggle', schedule, true);
    if (window.document$ && window.document$.subscribe) {
        window.document$.subscribe(schedule);
    }
})();

/* 
    Auto scrolls to place a collapsable Grid/Card admonition to the top of the screen view when you open it so that you don't have to scroll to see the full body.
*/

(function () {
    const SELECTOR = 'details.grid, details.cards';
    const GAP = 8;   // px of breathing room below the header

    function headerHeight() {
        const header = document.querySelector('.md-header');
        return header ? header.getBoundingClientRect().height : 0;
    }

    function scrollToAdmonitionTop(details) {
        const offset = headerHeight() + GAP;
        const rect = details.getBoundingClientRect();
        const targetY = window.scrollY + rect.top - offset;

        // Already in position — skip
        if (Math.abs(window.scrollY - targetY) < 2) return;

        const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        window.scrollTo({
            top: Math.max(0, targetY),
            behavior: reduceMotion ? 'instant' : 'smooth'
        });
    }

    document.addEventListener('toggle', function (e) {
        const el = e.target;
        if (!(el instanceof HTMLDetailsElement)) return;
        if (!el.matches(SELECTOR)) return;
        if (!el.open) return;

        // Two rAFs: first lets the opened content lay out,
        // second lets the browser commit the new height.
        requestAnimationFrame(() => {
            requestAnimationFrame(() => scrollToAdmonitionTop(el));
        });
    }, true);
})();

/* 
    Hover Markdown Preview 
*/

/* 
    Usage: 
        [Text](path/to/preview){ .hover-preview }
*/

(function () {
    // Only enable on devices that can actually hover with a fine pointer
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    const SELECTOR = 'a.hover-preview';
    const SHOW_DELAY = 350;         // ms before popover appears
    const HIDE_DELAY = 150;         // ms grace period to reach popover
    const MARGIN = 8;               // px from viewport edges
    const MAX_HEIGHT_VH = 0.6;      // 60vh max

    const cache = new Map();
    let popover = null;
    let activeLink = null;
    let showTimer = null;
    let hideTimer = null;

    function ensurePopover() {
        if (popover) return popover;
        popover = document.createElement('div');
        popover.className = 'hover-preview-popover';
        popover.setAttribute('role', 'tooltip');
        document.body.appendChild(popover);

        popover.addEventListener('mouseenter', () => {
            clearTimeout(hideTimer);
        });
        popover.addEventListener('mouseleave', () => {
            hidePopover();
        });
        return popover;
    }

    async function getContent(url) {
        if (cache.has(url)) return cache.get(url);
        try {
            const res = await fetch(url, { credentials: 'same-origin' });
            if (!res.ok) throw new Error('HTTP ' + res.status);
            const html = await res.text();
            const doc = new DOMParser().parseFromString(html, 'text/html');
            const inner =
                doc.querySelector('.md-content__inner .md-typeset') ||
                doc.querySelector('.md-content__inner') ||
                doc.querySelector('.md-typeset');
            const content = inner ? inner.innerHTML : '<em>Preview unavailable.</em>';
            cache.set(url, content);
            return content;
        } catch (err) {
            const msg = '<em>Failed to load preview.</em>';
            cache.set(url, msg);
            return msg;
        }
    }

    function position() {
        if (!popover || !activeLink) return;

        const linkRect = activeLink.getBoundingClientRect();
        const vw = window.innerWidth;
        const vh = window.innerHeight;

        // Right boundary = text content's right edge (not the TOC wrapper's)
        const contentEl =
            activeLink.closest('.md-content') ||
            document.querySelector('.md-content') ||
            document.querySelector('.md-typeset');

        let rightEdge = vw - MARGIN;
        if (contentEl) {
            const cRect = contentEl.getBoundingClientRect();
            const cStyle = getComputedStyle(contentEl);
            const rightPad = parseFloat(cStyle.paddingRight) || 0;
            rightEdge = Math.min(cRect.right - rightPad, vw - MARGIN);
        }

        let left = Math.max(linkRect.left, MARGIN);
        let width = rightEdge - left;
        if (width < 240) width = 240;
        if (left + width > vw - MARGIN) {
            width = vw - MARGIN - left;
        }

        let top = linkRect.bottom + MARGIN;
        let maxH = Math.min(vh * MAX_HEIGHT_VH, vh - top - MARGIN);
        if (maxH < 120) maxH = Math.max(120, vh - top - MARGIN);

        popover.style.left = left + 'px';
        popover.style.top = top + 'px';
        popover.style.width = width + 'px';
        popover.style.maxHeight = maxH + 'px';
    }

    function showPopover(link) {
        ensurePopover();
        activeLink = link;
        popover.innerHTML = '<div class="hover-preview-loading">Loading preview…</div>';
        popover.style.maxHeight = (window.innerHeight * MAX_HEIGHT_VH) + 'px';
        popover.classList.add('is-visible');
        position();

        getContent(link.href).then((html) => {
            if (activeLink !== link) return;   // user left before load finished
            popover.innerHTML = html;
            position();
        });
    }

    function hidePopover() {
        clearTimeout(showTimer);
        clearTimeout(hideTimer);
        if (popover) popover.classList.remove('is-visible');
        activeLink = null;
    }

    function attach() {
        document.querySelectorAll(SELECTOR).forEach((link) => {
            if (link.dataset.hoverPreviewInit) return;
            link.dataset.hoverPreviewInit = '1';

            link.addEventListener('mouseenter', () => {
                clearTimeout(hideTimer);
                showTimer = setTimeout(() => showPopover(link), SHOW_DELAY);
            });
            link.addEventListener('mouseleave', () => {
                clearTimeout(showTimer);
                hideTimer = setTimeout(hidePopover, HIDE_DELAY);
            });
        });
    }

    // Dismiss on page scroll — the popover is position: fixed and won't follow the link
    window.addEventListener('scroll', hidePopover, { passive: true });

    // Dismiss on Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') hidePopover();
    });

    // Dismiss on click outside
    document.addEventListener('click', (e) => {
        if (!popover || !popover.classList.contains('is-visible')) return;
        if (!popover.contains(e.target)) hidePopover();
    });

    // Re-attach after instant navigation
    function run() { attach(); }
    document.addEventListener('DOMContentLoaded', run);
    if (window.document$ && window.document$.subscribe) {
        window.document$.subscribe(run);
    }
})();