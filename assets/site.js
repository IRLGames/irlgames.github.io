// IRL GAMES STUDIO · the featured carousel (home) and the media viewer (game pages). No libraries.
(() => {
  // featured carousel: slides are .slide inside #feat, one shown at a time
  const feat = document.getElementById("feat");
  if (feat) {
    const slides = [...feat.querySelectorAll(".slide")];
    const dots = document.getElementById("featDots");
    let i = 0, timer;
    slides.forEach((_, n) => {
      const b = document.createElement("button");
      b.type = "button"; b.setAttribute("aria-label", `Show ${slides[n].dataset.name}`);
      b.onclick = () => { show(n); restart(); };
      dots.append(b);
    });
    const show = n => {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => { s.hidden = k !== i; });
      [...dots.children].forEach((d, k) => d.setAttribute("aria-current", String(k === i)));
    };
    const restart = () => {
      clearInterval(timer);
      if (!matchMedia("(prefers-reduced-motion: reduce)").matches) timer = setInterval(() => show(i + 1), 7000);
    };
    feat.querySelector(".arrow.l").onclick = () => { show(i - 1); restart(); };
    feat.querySelector(".arrow.r").onclick = () => { show(i + 1); restart(); };
    // a thumbnail swaps the big picture of its slide
    feat.querySelectorAll(".thumbs4 img").forEach(t => {
      t.onclick = () => { t.closest(".slide").querySelector(".feat-main img").src = t.dataset.full; };
    });
    show(0); restart();
  }

  // game page viewer: the strip swaps the trailer and the screenshots
  const viewer = document.getElementById("viewer");
  if (viewer) {
    const strip = document.getElementById("strip");
    const video = viewer.querySelector("video");
    const img = viewer.querySelector("img");
    strip.querySelectorAll("button").forEach(b => {
      b.onclick = () => {
        strip.querySelectorAll("button").forEach(x => x.setAttribute("aria-current", "false"));
        b.setAttribute("aria-current", "true");
        if (b.dataset.video) { img.hidden = true; video.hidden = false; }
        else { video.pause(); video.hidden = true; img.hidden = false; img.src = b.dataset.full; img.alt = b.querySelector("img").alt; }
      };
    });
  }
})();
