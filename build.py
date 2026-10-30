"""IRL GAMES STUDIO website: builds the pages from one shared head, menu and footer.  python3 build.py
No secrets in anything here (owner rule): no Wren, the Stranger is never named."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SUPPORT, FEEDBACK = "irlgamesnow@proton.me", "IRLGfeedback@proton.me"
DISCORD = "https://discord.gg/7yDTUyphKN"
X_URL, X_HANDLE = "https://x.com/IRLGamesNow", "@IRLGamesNow"

SITE = "https://irlgames.github.io/"

def page(name, title, desc, body, current, og="og_home.jpg"):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == current else ""}>{t}</a>'
                  for k, h, t in [("home", "index.html", "Store"), ("nn", "neon-noon.html", "Neon Noon"), ("npns", "no-people-no-stories.html", "No People, No Stories"), ("dmh", "dead-mans-hand.html", "Dead Man's Hand"),
                                  ("support", "support.html", "Support"), ("privacy", "privacy.html", "Privacy")])
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:site_name" content="IRL Games Studio">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{'' if name == 'index.html' else name}">
<meta property="og:image" content="{SITE}assets/img/{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="{X_HANDLE}">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}assets/img/{og}">
<meta name="twitter:image:alt" content="{title}">
<link rel="canonical" href="{SITE}{'' if name == 'index.html' else name}">
<meta name="theme-color" content="#941D16">
<link rel="icon" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700;900&family=Source+Sans+3:wght@400;600&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="index.html"><img src="assets/img/irl_logo.webp" alt="" width="36" height="36" style="align-self:center">IRL GAMES <small>STUDIO</small></a><nav class="nav" aria-label="Main">{nav}</nav></div></header>
{body}
<footer><div class="wrap"><span>© 2026 IRL Games Studio</span><a href="privacy.html">Privacy Policy</a><a href="support.html">Support</a><a href="{DISCORD}" rel="noopener">Discord</a><a href="{X_URL}" rel="noopener">X {X_HANDLE}</a><span>{SUPPORT}</span></div></footer>
<script src="assets/site.js"></script>
</body>
</html>
"""
    open(os.path.join(HERE, name), "w").write(html)

REL = "https://github.com/IRLGames/irlgames.github.io/releases/download/no-people-no-stories-v1.0.1/"   # the free game's downloads (a GitHub release on this repo)

GAMES = {
    "nn": dict(file="neon-noon.html", title="Neon Noon", short="Six hours. Not one man in town will stand with him.",
               blurb="A cyberpunk High Noon visual novel.",
               tags=["Visual Novel", "Cyberpunk", "Western", "Story Rich", "Choices Matter", "Multiple Endings", "Poker", "Noir", "Mature"],
               shots=[("01_title", "Title screen"), ("02_prologue", "The opening"), ("03_sable", "Sable's bar, the Last Light"), ("04_lin", "Lin, the morning of"),
                      ("05_town_map", "The town of Sundown"), ("06_poker", "The card table"), ("07_faces", "Faces of Sundown")],
               about=["A retired lawman has until noon, a wife to protect, and a town that won't stand with him.",
                      "Every choice closes a door, and not every door opens again. Talk your way through Sundown, find out who will stand at noon and who won't, and live with what that costs.",
                      "Five endings. Thirty-three hidden Faces of Sundown cards to find across your playthroughs. A full, fair game of poker at the card table."],
               features=["Single-player story, 5 endings", "33 hidden collectible cards", "A full Texas Hold'em table", "Controller support and Steam Deck controls", "Touch controls on Android"]),
    "npns": dict(file="no-people-no-stories.html", title="No People, No Stories", short="Pools, garages, a night mall, a temple of light, Neon Noon's rain-soaked Sundown. Nobody else is here.",
                 blurb="An endless liminal ASMR walk through empty places.",
                 tags=["Walking Simulator", "Relaxing", "Atmospheric", "ASMR", "Liminal Space", "Exploration", "Procedural", "Free"],
                 shots=[("01_title", "Title screen"), ("02_pools", "The Pools"), ("09_sundown", "Sundown, after hours"), ("05_laundromat", "The Laundromat"),
                        ("07_temple", "The Temple"), ("08_hotel", "The Hotel"), ("06_mall", "The Night Mall"), ("03_garage", "The Garage"),
                        ("04_platform", "The Platform"), ("10_sundown_late", "Sundown, late light"), ("11_places", "Where would you like to wander?")],
                 about=["No People, No Stories is a quiet, endless walk through the places in between: a sunlit poolroom, a parking garage in the rain, a platform where no train stops, a laundromat at 3 a.m.",
                        "Every place is built fresh when you walk in, and it never ends. There's nothing to win and no one to meet. Just the hum of the lights, the water, the rain, mixed the way you like it.",
                        "Eight places, three times of day, and a sound mixer for each. One of them is Sundown, the district from Neon Noon, empty at 3 a.m., with the theme playing from a bar somewhere. Free, from IRL Games Studio."],
                 features=["8 endless places, new every walk", "Noon, late light and after hours", "A sound mixer for every place", "Controller and Steam Deck support", "Touch controls on Android", "Free"],
                 release="October 30, 2026", price="Free", platforms="Windows · Linux · Steam Deck · Android", badge="Free",
                 buy="Free. Windows, Linux (Steam Deck: the Linux build) and Android. Version 1.0.1",
                 downloads=[("Windows", REL + "NoPeopleNoStories-1.0.1-windows.zip"), ("Linux", REL + "NoPeopleNoStories-1.0.1-linux.tar.gz"), ("Android", REL + "NoPeopleNoStories-1.0.1-android.apk")]),
    "dmh": dict(file="dead-mans-hand.html", title="Neon Noon: Dead Man's Hand", short="Eleven years before noon. A stranger sits down with money and a question.",
                blurb="The poker prequel to Neon Noon.",
                tags=["Poker", "Card Game", "Visual Novel", "Cyberpunk", "Western", "Story Rich", "Multiple Endings", "Noir"],
                shots=[("01_title", "Title screen"), ("06_stranger", "A stranger at the Xenon Lamp"), ("03_bar", "The Xenon Lamp"),
                       ("05_table_late", "A big pot, late"), ("04_table", "The back table")],
                about=["One night at the back table of the Xenon Lamp, where every hand is honest and every player is hiding something.",
                       "Play real Texas Hold'em, never rigged, while the story plays out one hand at a time. What you win loosens tongues; what you lose keeps them shut.",
                       "Three endings. Twelve decks to collect from Sable's drawer."],
                features=["Single-player story, 3 endings", "Real Texas Hold'em, never rigged", "Collectible card decks", "Controller support and Steam Deck controls", "Touch controls on Android"]),
}

def tags(t): return '<div class="tags">' + "".join(f'<span class="tag">{x}</span>' for x in t) + "</div>"

def facts(g):
    price = f"<dt>Price</dt><dd>{g['price']}</dd>" if g.get("price") else ""
    return f"""<dl class="facts"><dt>Release date</dt><dd>{g.get('release', 'Coming soon')}</dd>{price}<dt>Developer</dt><dd><a href="index.html">IRL Games Studio</a></dd>
<dt>Publisher</dt><dd><a href="index.html">IRL Games Studio</a></dd><dt>Platforms</dt><dd>{g.get('platforms', 'Windows · Steam Deck · Android')}</dd></dl>"""

def buy(g):   # the buy box: downloads for a released game, "coming soon" for the rest
    if g.get("downloads"):
        btns = "".join(f'<a class="btn" href="{u}">{t}</a>' for t, u in g["downloads"])
        return f'<div class="buy"><div><h2>{g["title"]}</h2><p>{g["buy"]}</p></div><div style="display:flex;gap:8px;flex-wrap:wrap">{btns}</div></div>'
    return f'<div class="buy"><div><h2>{g["title"]}</h2><p>Coming soon to Steam and Google Play</p></div><span class="btn">Coming soon</span></div>'

def game_page(key):
    g = GAMES[key]
    strip = f'<button type="button" class="play" data-video="1" aria-current="true" aria-label="Play the trailer"><img src="assets/video/{key}_poster.jpg" alt="Trailer"></button>'
    strip += "".join(f'<button type="button" aria-current="false" data-full="assets/img/{key}_shot_{s}.webp"><img src="assets/img/{key}_shot_{s}_t.webp" alt="{a}" loading="lazy"></button>' for s, a in g["shots"])
    body = f"""<main class="wrap">
<p class="crumbs"><a href="index.html">All Games</a> &rsaquo; {g['title']}</p>
<h1>{g['title']}</h1>
<div class="app">
  <div class="media">
    <div class="viewer" id="viewer"><video controls preload="metadata" poster="assets/video/{key}_poster.jpg" playsinline><source src="assets/video/{key}_trailer.mp4" type="video/mp4"></video><img alt="" hidden></div>
    <div class="strip" id="strip">{strip}</div>
  </div>
  <aside class="side">
    <img class="capimg" src="assets/img/{key}_capsule.webp" alt="{g['title']}">
    <p><b>{g['blurb']}</b> {g['short']}</p>
    {facts(g)}
    {tags(g['tags'])}
  </aside>
</div>
{buy(g)}
<div class="cols">
  <section class="about"><p class="h-label">About this game</p>{''.join(f'<p>{p}</p>' for p in g['about'])}</section>
  <aside class="panel"><p class="h-label">Features</p><ul>{''.join(f'<li>{f}</li>' for f in g['features'])}</ul></aside>
</div>
</main>"""
    page(g["file"], f"{g['title']} · IRL Games Studio", f"{g['blurb']} {g['short']} " + ("Free on Windows, Linux and Android." if g.get("downloads") else "Coming to Steam and Google Play."), body, key, f"og_{key}.jpg")

def home():
    slides = ""
    for key, g in GAMES.items():
        th = "".join(f'<img src="assets/img/{key}_shot_{s}_t.webp" data-full="assets/img/{key}_shot_{s}.webp" alt="{a}">' for s, a in g["shots"][1:5])
        slides += f"""<div class="slide" data-name="{g['title']}" hidden>
<div class="feat" style="border:0;box-shadow:none"><a class="feat-main" href="{g['file']}"><img src="assets/img/{key}_shot_{g['shots'][1][0]}.webp" alt="{g['title']}"></a>
<div class="feat-side"><h2><a href="{g['file']}" style="color:#fff">{g['title']}</a></h2><div class="thumbs4">{th}</div>
<p class="muted" style="margin:0">{g['short']}</p><div><span class="badge">{g.get('badge', 'Coming soon')}</span></div>{tags(g['tags'][:5])}</div></div></div>"""
    body = f"""<div class="hero"><img src="assets/img/irl_header.webp" alt="IRL Games Studio" width="1920" height="560"></div>
<main class="wrap">
<section class="section"><p class="h-label">Featured</p>
<div id="feat" style="position:relative"><button class="arrow l" type="button" aria-label="Previous">&#8249;</button>{slides}<button class="arrow r" type="button" aria-label="Next">&#8250;</button></div>
<div class="dots" id="featDots"></div></section>
<section class="section"><p class="h-label">Our games &amp; projects</p><div class="caps">
<a class="cap" href="neon-noon.html"><img src="assets/img/nn_capsule.webp" alt="Neon Noon"><div class="ct">Neon Noon<span>Coming soon</span></div></a>
<a class="cap" href="no-people-no-stories.html"><img src="assets/img/npns_capsule.webp" alt="No People, No Stories"><div class="ct">No People, No Stories<span>Free</span></div></a>
<a class="cap" href="dead-mans-hand.html"><img src="assets/img/dmh_capsule.webp" alt="Neon Noon: Dead Man's Hand"><div class="ct">Neon Noon: Dead Man's Hand<span>Coming soon</span></div></a>
<a class="cap" href="#vtube-live"><div class="vt"><img src="assets/img/vtubelive_icon.webp" alt="Vtube Live"></div><div class="ct">Vtube Live<span>In development</span></div></a>
</div></section>
<section class="section" id="vtube-live"><p class="h-label">Coming soon</p><div class="vtube"><img src="assets/img/vtubelive_icon.webp" alt="Vtube Live icon">
<div><h2>Vtube Live</h2><p class="muted">A VTuber app from IRL Games Studio: build your avatar and go live. In development.</p>{tags(["VTuber", "Avatar", "Streaming", "In development"])}</div></div></section>
<section class="section" id="community"><p class="h-label">Community</p><div class="buy" style="margin:0"><div><h2>Join the community</h2><p>News, development updates and a place to talk about the games. On X: {X_HANDLE}</p></div><div style="display:flex;gap:8px;flex-wrap:wrap"><a class="btn" href="{DISCORD}" rel="noopener">Join the Discord</a><a class="btn" href="{X_URL}" rel="noopener">Follow on X</a></div></div></section>
<section class="section"><p class="h-label">About the studio</p><p style="max-width:68ch">IRL Games Studio is a small independent studio making story-first games about hard choices and the people who live with them.</p></section>
</main>"""
    page("index.html", "IRL Games Studio", "Story-first games by IRL Games Studio: Neon Noon and Neon Noon: Dead Man's Hand, coming to Steam and Google Play, and No People, No Stories, free now.", body, "home")

def support():
    body = f"""<main class="wrap doc"><h1>Support</h1>
<p>Stuck, found a bug, or have a question about one of our games? We read everything.</p>
<div class="panel"><p style="margin:0">General questions and help: <span class="mail">{SUPPORT}</span></p><p style="margin:6px 0 0">Game feedback and ideas: <span class="mail">{FEEDBACK}</span></p></div>
<h2>Community</h2><p>Talk to us and other players on our <a href="{DISCORD}" rel="noopener">Discord server</a>, or follow <a href="{X_URL}" rel="noopener">{X_HANDLE}</a> on X for news.</p>
<h2>Reporting a bug from inside the game</h2><p>Every IRL Games Studio game has a "report a problem" button. It sends us a short note and a screenshot of where you are, so we can see exactly what went wrong. See our <a href="privacy.html">Privacy Policy</a> for what a report contains.</p>
<h2>Deleting your data</h2><p>Our games don't create accounts or collect anything automatically. If you sent a bug report and want it deleted, email <span class="mail">{SUPPORT}</span> and we'll remove it.</p>
<h2>Refunds</h2><p>Purchases and refunds are handled by the store you bought from (Google Play or Steam).</p></main>"""
    page("support.html", "Support · IRL Games Studio", "Help and contact for IRL Games Studio games.", body, "support")

def privacy():
    body = f"""<main class="wrap doc"><h1>Privacy Policy</h1><p class="muted">Effective October 28, 2026</p>
<p>This policy covers all games by IRL Games Studio ("we"), including Neon Noon, Neon Noon: Dead Man's Hand and No People, No Stories, on every platform.</p>
<p><b>The short version:</b> our games don't collect anything about you unless you choose to send us a bug report. There are no ads, no tracking, no analytics and no accounts.</p>
<h2>Update check (No People, No Stories)</h2><p>When it starts, No People, No Stories asks GitHub once whether a newer version is out. The request carries only the game's version number; like any web request, GitHub sees your internet address. Nothing else is sent, and we receive nothing from it.</p>
<h2>What stays on your device</h2><p>Your saves, settings and progress are stored only on your device. We never see them.</p>
<h2>Bug reports (only if you send one)</h2><p>Each game has a "report a problem" button. Nothing is sent unless you write a report and press Send. A report can include:</p>
<ul><li>the message you write, and your name or email only if you choose to add them;</li><li>a screenshot of the game screen at that moment;</li>
<li>the game's version number and the type of device or operating system;</li><li>where you were in the game, such as the chapter and the last few lines of story shown.</li></ul>
<p>Reports are sent securely (HTTPS) to a private Google spreadsheet that only we can read. We use them only to find and fix problems. We don't sell or share them, and we delete them when they're no longer needed or when you ask us to.</p>
<h2>Store platforms</h2><p>Purchases are handled by the store you buy from, such as Google Play or Steam, under their own privacy policies. On Steam, achievements are recorded through Steam. We don't receive your payment details.</p>
<h2>Children</h2><p>Our games are made for adults and aren't directed at children under 13. We don't knowingly collect information from children.</p>
<h2>Your choices</h2><p>To have a bug report you sent deleted, or to ask any question about privacy, email us at <span class="mail">{SUPPORT}</span>. We'll reply within 30 days.</p>
<h2>Changes</h2><p>If this policy changes, we'll update the date at the top of this page.</p></main>"""
    page("privacy.html", "Privacy Policy · IRL Games Studio", "Privacy policy for IRL Games Studio games.", body, "privacy")

if __name__ == "__main__":
    home(); game_page("nn"); game_page("npns"); game_page("dmh"); support(); privacy()
    print("built:", ", ".join(sorted(f for f in os.listdir(HERE) if f.endswith(".html"))))
