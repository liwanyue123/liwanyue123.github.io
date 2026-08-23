/* Wanyue Li — site behaviour. No dependencies. */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- sticky nav state ---- */
  var nav = document.querySelector(".nav");
  if (nav) {
    var onScroll = function () {
      nav.classList.toggle("is-stuck", window.scrollY > 24);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- scroll reveal ---- */
  var revealables = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  if (revealables.length) {
    if (reduced || !("IntersectionObserver" in window)) {
      revealables.forEach(function (el) { el.classList.add("is-in"); });
    } else {
      // Anything already inside the first viewport reveals straight away. The
      // observer's negative bottom margin would otherwise strand elements sitting
      // low in the initial view — they would stay invisible until the user scrolled.
      var vh = window.innerHeight || document.documentElement.clientHeight;
      var pending = [];
      revealables.forEach(function (el) {
        if (el.getBoundingClientRect().top < vh) el.classList.add("is-in");
        else pending.push(el);
      });
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("is-in");
            io.unobserve(e.target);
          }
        });
      }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
      pending.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---- scrollspy for section nav ---- */
  var spyLinks = Array.prototype.slice.call(document.querySelectorAll("[data-spy]"));
  if (spyLinks.length && "IntersectionObserver" in window) {
    var targets = spyLinks
      .map(function (l) { return document.getElementById(l.getAttribute("data-spy")); })
      .filter(Boolean);
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        spyLinks.forEach(function (l) {
          l.classList.toggle("is-active", l.getAttribute("data-spy") === e.target.id);
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    targets.forEach(function (t) { spy.observe(t); });
  }

  /* ---- current year ---- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
