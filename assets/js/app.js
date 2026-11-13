(function () {
  var d = document, $ = function (s, r) { return (r || d).querySelector(s); }, $$ = function (s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); };
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* header */
  var hd = $(".site-header");
  function stuck() { hd.classList.toggle("is-stuck", window.scrollY > 8); }
  stuck(); window.addEventListener("scroll", stuck, { passive: true });

  /* mobile nav + dropdown */
  var burger = $(".burger"), nav = $("#nav");
  burger.addEventListener("click", function () {
    var o = nav.classList.toggle("open");
    nav.style.top = o ? Math.max(0, Math.round(hd.getBoundingClientRect().bottom)) + "px" : "";
    burger.setAttribute("aria-expanded", o);
    d.body.style.overflow = o ? "hidden" : "";
  });
  $$(".has-dd > button").forEach(function (b) {
    b.addEventListener("click", function () {
      var p = b.parentNode, o = p.classList.toggle("open");
      b.setAttribute("aria-expanded", o);
    });
  });
  d.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      $$(".has-dd.open").forEach(function (p) { p.classList.remove("open"); $("button", p).setAttribute("aria-expanded", "false"); });
      if (nav.classList.contains("open")) burger.click();
    }
  });
  d.addEventListener("click", function (e) {
    if (!e.target.closest(".has-dd") && window.innerWidth > 1024) $$(".has-dd.open").forEach(function (p) { p.classList.remove("open"); });
  });

  /* galeri: filter + lightbox */
  var items = $$(".gi[data-cat]");
  if (items.length) {
    $$(".chip[data-f]").forEach(function (c) {
      c.addEventListener("click", function () {
        $$(".chip[data-f]").forEach(function (x) { x.setAttribute("aria-pressed", x === c); });
        var f = c.getAttribute("data-f");
        items.forEach(function (it) { it.classList.toggle("hide", f !== "all" && it.getAttribute("data-cat") !== f); });
      });
    });
  }
  var lbItems = $$("[data-lb]"), lb = $(".lb"), idx = 0, lastFocus;
  if (lb && lbItems.length) {
    var img = $("img", lb), cap = $("figcaption", lb);
    var vis = function () { return lbItems.filter(function (i) { return !i.classList.contains("hide"); }); };
    var show = function (n) {
      var v = vis(); if (!v.length) return;
      idx = (n + v.length) % v.length;
      var el = v[idx], im = $("img", el);
      img.src = el.getAttribute("data-lb"); img.alt = im ? im.alt : "";
      cap.textContent = el.getAttribute("data-cap") || "";
    };
    var close = function () { lb.classList.remove("open"); d.body.style.overflow = ""; if (lastFocus) lastFocus.focus(); };
    lbItems.forEach(function (el) {
      el.addEventListener("click", function () {
        lastFocus = el; lb.classList.add("open"); d.body.style.overflow = "hidden";
        show(vis().indexOf(el)); $(".x", lb).focus();
      });
    });
    $(".x", lb).addEventListener("click", close);
    $(".pv", lb).addEventListener("click", function () { show(idx - 1); });
    $(".nx", lb).addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    d.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
    });
    var sx = 0;
    lb.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) { var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1)); });
  }

  /* form -> WhatsApp */
  var form = $("#daftar");
  if (form) {
    var pre = $("#preview"), wa = (window.SITE && SITE.wa) || "6281335351697";
    var qs = new URLSearchParams(location.search).get("program");
    if (qs && form.program) { $$("option", form.program).forEach(function (o) { if (o.value === qs) form.program.value = qs; }); }
    var msg = function () {
      var v = function (n) { return (form[n].value || "").trim(); };
      var t = "Halo Shuohao Zhongwen, saya ingin bertanya mengenai program kursus Mandarin.\n\n" +
        "Nama: " + v("nama") + "\n" +
        "Nomor WhatsApp: " + v("wa") + "\n" +
        "Program yang diminati: " + v("program") + "\n" +
        (v("level") ? "Tingkat kemampuan Mandarin: " + v("level") + "\n" : "") +
        "Kebutuhan belajar: " + (v("pesan") || "-") + "\n\nMohon informasi lebih lanjut. Terima kasih.";
      return t;
    };
    var upd = function () { pre.textContent = msg(); };
    form.addEventListener("input", upd); upd();
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      [["nama", function (x) { return x.length > 1; }], ["wa", function (x) { return /^[+\d][\d\s\-]{7,}$/.test(x); }], ["program", function (x) { return !!x; }]].forEach(function (r) {
        var f = form[r[0]], good = r[1](f.value.trim());
        f.closest(".fld").classList.toggle("bad", !good); if (!good) ok = false;
      });
      if (!ok) { var b = $(".bad input,.bad select", form); if (b) b.focus(); return; }
      window.open("https://wa.me/" + wa + "?text=" + encodeURIComponent(msg()), "_blank", "noopener");
    });
  }

  /* motion (GSAP) */
  d.documentElement.classList.add("js");
  if (!window.gsap || reduce) return;
  var g = window.gsap; if (window.ScrollTrigger) g.registerPlugin(window.ScrollTrigger);
  var ease = "power3.out";
  var h = $("[data-hero]");
  if (h) {
    var tl = g.timeline({ defaults: { ease: ease } });
    tl.from("[data-hero] h1", { y: 32, opacity: 0, duration: .9 })
      .from("[data-hero] .lead,[data-hero] .hero-cta,[data-hero] .facts", { y: 20, opacity: 0, duration: .7, stagger: .08 }, "-=.5");
    if ($(".mosaic")) tl.from(".mosaic > *", { scale: .6, opacity: 0, duration: .8, stagger: .1, ease: "back.out(1.4)" }, 0.15);
  }
  if (!window.ScrollTrigger) return;
  $$("[data-stagger]").forEach(function (box) {
    g.from(box.children, { y: 24, opacity: 0, duration: .7, stagger: .08, ease: ease, scrollTrigger: { trigger: box, start: "top 82%", once: true } });
  });
  $$("[data-reveal]").forEach(function (el) {
    g.from(el, { clipPath: "inset(0 0 100% 0)", duration: 1, ease: "power2.inOut", scrollTrigger: { trigger: el, start: "top 85%", once: true } });
  });
})();
