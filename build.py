"""LUX COR GAMES website (renamed from Lux Cor Games, owner 2026-11-10): builds the pages from one shared head, menu and footer.  python3 build.py
No secrets in anything here (owner rule): no Wren, the Stranger is never named."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SUPPORT = FEEDBACK = "LuxCorGames@proton.me"   # (owner 2026-11-10: "LuxCorGames@proton.me is the email for the company"; was irlgamesnow@ / IRLGfeedback@)
DISCORD = "https://discord.gg/7yDTUyphKN"
X_URL, X_HANDLE = "https://x.com/LuxCorMedia", "@LuxCorMedia"   # (owner 2026-11-10: "the New X.com is @LuxCorMedia"; was @IRLGamesNow)
YT_URL = "https://www.youtube.com/@LuxCorGames"   # (owner 2026-11-10: "youtube is @LuxCorGames"; was @IRLGamesNow)
# tips (owner 2026-11-09: Ko-fi + Stripe, two ways so losing one isn't fatal). Empty = that button isn't shown; swap a link here only
KOFI = "https://ko-fi.com/irlgames"
STRIPE_TIP = "https://buy.stripe.com/dRmcN66tAaqpdO12DD7Re00"   # pay-what-you-want link (owner 2026-11-09); redirects to thanks.html
STRIPE_LIVE = True   # the link shows "paused" until Stripe finishes activating the account: True puts the card button on the site
# the visit counter (owner 2026-11-03: "just a visit counter"): the Apps Script web app URL from ../counter/apps_script.gs.
# Empty = no counter on the site and no counter line in the privacy policy.
COUNTER_URL = ""
COUNTER_JS = ("" if not COUNTER_URL else
    '<script>try{if(!sessionStorage.getItem("irl_v")){sessionStorage.setItem("irl_v","1");var u="' + COUNTER_URL + '?ping";'
    'if(!(navigator.sendBeacon&&navigator.sendBeacon(u)))fetch(u,{mode:"no-cors",keepalive:true});}}catch(e){}</script>')
COUNTER_PRIVACY = ("" if not COUNTER_URL else
    "<h2>Website visits</h2><p>This website counts visits. When you open it, that day's tally goes up by one. Nothing about you is "
    "sent or kept: no cookies, no address, no browser details. We see only the number of visits per day, in a private Google spreadsheet.</p>")

SITE = "https://irlgames.github.io/"

def page(name, title, desc, body, current, og="og_home.jpg"):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == current else ""}>{t}</a>'
                  for k, h, t in [("home", "index.html", "Store"), ("bb", "steel-chariot.html", "Steel Chariot"), ("nn", "neon-noon.html", "Neon Noon"), ("npns", "no-people-no-stories.html", "No People, No Stories"), ("dmh", "dead-mans-hand.html", "Dead Man's Hand"),
                                  ("about", "about.html", "About"), ("support", "support.html", "Support"), ("privacy", "privacy.html", "Privacy")])
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:site_name" content="Lux Cor Games">
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
<header class="top"><div class="wrap"><a class="brand" href="index.html"><img src="assets/img/luxcor_mark.webp" alt="" width="32" height="32" style="align-self:center;border-radius:4px">LUX COR <small>GAMES</small></a><nav class="nav" aria-label="Main">{nav}</nav></div></header>
{body}
<footer><div class="wrap"><span>© 2026 Lux Cor LLC · Lux Cor Games</span><a href="privacy.html">Privacy Policy</a><a href="support.html">Support</a><a href="{DISCORD}" rel="noopener">Discord</a><a href="{X_URL}" rel="noopener">X {X_HANDLE}</a><a href="{YT_URL}" rel="noopener">YouTube</a><a href="about.html#support-us">Support us</a><span>{SUPPORT}</span><span class="tm">Google Play and the Google Play logo are trademarks of Google LLC.</span></div></footer>
<script src="assets/site.js"></script>{COUNTER_JS}
</body>
</html>
"""
    open(os.path.join(HERE, name), "w").write(html)

BB_SHOTS = [("01_title", "Title screen"), ("02_holy", "Holy Fire on the highway at dusk"), ("05_coast", "The coast road at night"),
            ("08_corn", "Corn country at night"), ("03_nitro", "Nitro on the highway at dawn"), ("06_strip", "The neon strip"),
            ("07_bridge", "The causeway gates"), ("09_cows", "Cattle on the road"), ("10_farm", "Farm country at dawn"),
            ("11_close", "The Interceptor, up close"), ("14_truck", "The Monster Truck in the scrapyard"),
            ("13_lift", "Paint and flames on the lift"), ("12_marks", "Painted marks")]   # frames from the 4K sizzle reel (2026-11-09)
REL = "https://github.com/IRLGames/irlgames.github.io/releases/download/no-people-no-stories-v1.0.9/"   # the free game's downloads (a GitHub release on this repo)

GAMES = {
    # Brimstone & Buckshot: Steel Chariot (owner 2026-11-08: "the web page updated with 'Coming soon' ... advertize 5 levels at least")
    "bb": dict(file="steel-chariot.html", title="Brimstone & Buckshot: Steel Chariot", short="Weld a cross to the plow, fill the tank with Holy Fire, and drive through the damned.",
               blurb="Zombie-smashing car combat.",
               tags=["Action", "Driving", "Zombies", "Vehicular Combat", "Arcade", "Customization", "Gore", "Singleplayer"],
               shots=BB_SHOTS,
               about=["The dead walk the roads, and the roads are all that's left. You've got a car, a cross welded to the plow and a tank of Holy Fire.",
                      "Build your chariot in the scrapyard: four cars to make your own, with paint and flames, painted marks, armour plate or a welded cage, a supercharger and a gun on the roof. Then take it out and smash through the damned at a hundred miles an hour.",
                      "Highways, coast roads and country back roads at dusk, at night and at dawn, with fuel tankers to blow, police roadblocks to break and ramps to jump. At least five roads at launch, and more after.",
                      "Crank the radio: an original metal soundtrack rides along with you, punk metal to heavy metal, and you can flip stations on the fly. More songs are on the way. And when you start the game, an Orthodox chant, Steel Chariot, is waiting on the title screen. Hear every song, and a few extras, on <a href=\"https://www.youtube.com/@LuxCorGames\" rel=\"noopener\">our YouTube channel</a>."],
               features=["5+ roads at launch: highway, coast, country and more", "Four cars to build: the Interceptor, the Monster Truck, the Synaxis and the Bug",
                         "Paint, flames, marks, armour, cages, superchargers", "Roof guns: twin buckshot, stake launcher, rockets, a .50 cal heavy machine gun",
                         "Holy Fire: blue flame from the cross on your plow", "Nitro, ramps, smash combos", "An original metal soundtrack on the in-car radio, with more songs on the way", "Controller support, on Windows, Linux and SteamOS"],
               release="Coming soon", platforms="Windows · Linux · SteamOS (Steam)", badge="Coming soon",
               buy="Coming soon to Steam (Windows, Linux, SteamOS).", desc="Coming soon to Steam for Windows, Linux and SteamOS."),
    "nn": dict(file="neon-noon.html", title="Neon Noon", short="Six hours. Not one man in town will stand with him.",
               blurb="A cyberpunk High Noon visual novel.",
               tags=["Visual Novel", "Cyberpunk", "Western", "Story Rich", "Choices Matter", "Multiple Endings", "Poker", "Noir", "Mature"],
               shots=[("01_title", "Title screen"), ("02_prologue", "The opening"), ("03_sable", "Sable's bar"), ("04_lin", "Lin, the morning of"),
                      ("05_town_map", "The town of Sundown"), ("06_poker", "The card table"), ("07_faces", "Faces of Sundown")],
               about=["A retired lawman has until noon, a wife to protect, and a town that won't stand with him.",
                      "Every choice closes a door, and not every door opens again. Talk your way through Sundown, find out who will stand at noon and who won't, and live with what that costs.",
                      "Five endings. Thirty-three hidden Faces of Sundown cards to find across your playthroughs. A full, fair game of poker at the card table."],
               features=["Single-player story, 5 endings", "33 hidden collectible cards", "A full Texas Hold'em table", "Controller support and Steam Deck controls", "Touch controls on Android"],
               release="November 6, 2026 (Android)", price="Free to start; the full story is a one-time in-app purchase", badge="On Google Play",
               platforms="Android now · Windows and Steam Deck coming", buy="Free to start on Android. Steam (Windows, Steam Deck) coming soon.",
               play="https://play.google.com/store/apps/details?id=com.irlgamesstudio.neonnoon"),
    "npns": dict(file="no-people-no-stories.html", title="No People, No Stories", short="Pools, garages, a night mall, an Egyptian temple, Neon Noon's rain-soaked Sundown. Nobody else is here.",
                 blurb="An endless liminal ASMR walk through empty places.",
                 tags=["Walking Simulator", "Relaxing", "Atmospheric", "ASMR", "Liminal Space", "Exploration", "Procedural", "Free"],
                 shots=[("01_title", "Title screen"), ("16_egypt_well", "The Egyptian Temple"), ("17_egypt_hall", "A hall in the Egyptian Temple"), ("02_pools", "The Pools"), ("08_hotel", "The Hotel"), ("12_hotel_atrium", "The Hotel, two floors up"),
                        ("06_mall", "The Night Mall"), ("15_mall_court", "A court in the Night Mall"), ("14_road", "Long Black Road"), ("13_office", "The Back Office"),
                        ("09_sundown", "Sundown, after hours"), ("05_laundromat", "The Laundromat"), ("07_temple", "The Void Temple"), ("03_garage", "The Garage"),
                        ("04_platform", "The Platform"), ("10_sundown_late", "Sundown, late light"), ("18_egypt_sanctum", "A sanctum in the Egyptian Temple"), ("11_places", "Where would you like to wander?")],
                 about=["No People, No Stories is a quiet, endless walk through the places in between: a sunlit poolroom, a parking garage in the rain, a platform where no train stops, a laundromat at 3 a.m., a hotel lobby two floors high, a night mall with its shutters down, an office where the lights hum and fail, a long black road in the fog, an Egyptian temple where light falls from the water far above.",
                        "Every place is built fresh when you walk in, and it never ends. There's nothing to win and no one to meet. Just the hum of the lights, the water, the rain, mixed the way you like it.",
                        "Eleven places, three times of day, and a sound mixer for each. One of them is Sundown, the district from Neon Noon, empty at 3 a.m., with the theme playing from a bar somewhere. Free, from Lux Cor Games."],
                 features=["11 endless places, new every walk", "Noon, late light and after hours", "A sound mixer for every place", "Controller and Steam Deck support", "Touch controls on Android", "Free"],
                 release="October 30, 2026", price="Free", platforms="Windows · Linux · Steam Deck · Android", badge="Free",
                 buy="Free on Google Play, or download it here: Windows, Linux (Steam Deck: the Linux build) and Android APK. Version 1.0.9",
                 play="https://play.google.com/store/apps/details?id=com.irlgamesstudio.nopeoplenostories",
                 downloads=[("Windows", REL + "NoPeopleNoStories-1.0.9-windows.zip"), ("Linux", REL + "NoPeopleNoStories-1.0.9-linux.tar.gz"), ("Android APK", REL + "NoPeopleNoStories-1.0.9-android.apk")]),
    "dmh": dict(file="dead-mans-hand.html", title="Neon Noon: Dead Man's Hand", short="Eleven years before noon. A stranger sits down with money and a question.",
                blurb="The poker prequel to Neon Noon.",
                tags=["Poker", "Card Game", "Visual Novel", "Cyberpunk", "Western", "Story Rich", "Multiple Endings", "Noir"],
                shots=[("01_title", "Title screen"), ("06_stranger", "A stranger at the Xenon Lamp"), ("03_bar", "The Xenon Lamp"),
                       ("05_table_late", "A big pot, late"), ("04_table", "The back table")],
                about=["One night at the back table of the Xenon Lamp, where every hand is honest and every player is hiding something.",
                       "Play real Texas Hold'em, never rigged, while the story plays out one hand at a time. What you win loosens tongues; what you lose keeps them shut.",
                       "Three endings. Twelve decks to collect from Sable's drawer."],
                features=["Single-player story, 3 endings", "Real Texas Hold'em, never rigged", "Collectible card decks", "Controller support and Steam Deck controls", "Touch controls on Android"],
                release="November 6, 2026 (Android)", price="$4.99 on Google Play", badge="On Google Play",
                platforms="Android now · Windows and Steam Deck coming", buy="On Android now. Steam (Windows, Steam Deck) coming soon.",
                play="https://play.google.com/store/apps/details?id=com.irlgamesstudio.deadmanshand"),
}

def tags(t): return '<div class="tags">' + "".join(f'<span class="tag">{x}</span>' for x in t) + "</div>"

def facts(g):
    price = f"<dt>Price</dt><dd>{g['price']}</dd>" if g.get("price") else ""
    return f"""<dl class="facts"><dt>Release date</dt><dd>{g.get('release', 'Coming soon')}</dd>{price}<dt>Developer</dt><dd><a href="index.html">Lux Cor Games</a></dd>
<dt>Publisher</dt><dd><a href="index.html">Lux Cor Games</a></dd><dt>Platforms</dt><dd>{g.get('platforms', 'Windows · Steam Deck · Android')}</dd></dl>"""

def play_badge(g, h=58):   # Google's official "Get it on Google Play" badge, unaltered (Google badge rules; trademark line in the footer)
    if not g.get("play"): return ""
    return f'<a class="play" href="{g["play"]}" rel="noopener"><img src="assets/img/google-play-badge.png" alt="Get it on Google Play" height="{h}" width="{round(h * 646 / 250)}"></a>'

def buy(g):   # the buy box: Google Play and/or downloads for a released game, "coming soon" for the rest
    if g.get("play") and not g.get("downloads"):
        return f'<div class="buy"><div><h2>{g["title"]}</h2><p>{g["buy"]}</p></div>{play_badge(g)}</div>'
    if g.get("downloads"):
        btns = "".join(f'<a class="btn" href="{u}">{t}</a>' for t, u in g["downloads"])
        return f'<div class="buy"><div><h2>{g["title"]}</h2><p>{g["buy"]}</p></div><div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">{play_badge(g)}{btns}</div></div>'
    return f'<div class="buy"><div><h2>{g["title"]}</h2><p>{g.get("buy", "Coming soon to Steam and Google Play")}</p></div><span class="btn">Coming soon</span></div>'

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
    page(g["file"], f"{g['title']} · Lux Cor Games", f"{g['blurb']} {g['short']} " + ("Free on Windows, Linux and Android." if g.get("downloads") else "On Google Play now, coming to Steam." if g.get("play") else g.get("desc", "Coming to Steam and Google Play.")), body, key, f"og_{key}.jpg")

def home():
    slides = ""
    for key, g in GAMES.items():
        th = "".join(f'<img src="assets/img/{key}_shot_{s}_t.webp" data-full="assets/img/{key}_shot_{s}.webp" alt="{a}">' for s, a in g["shots"][1:5])
        slides += f"""<div class="slide" data-name="{g['title']}" hidden>
<div class="feat" style="border:0;box-shadow:none"><a class="feat-main" href="{g['file']}"><img src="assets/img/{key}_shot_{g['shots'][1][0]}.webp" alt="{g['title']}"></a>
<div class="feat-side"><h2><a href="{g['file']}" style="color:#fff">{g['title']}</a></h2><div class="thumbs4">{th}</div>
<p class="muted" style="margin:0">{g['short']}</p><div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap"><span class="badge">{g.get('badge', 'Coming soon')}</span>{play_badge(g, 46)}</div>{tags(g['tags'][:5])}</div></div></div>"""
    # the hero is Steel Chariot (owner 2026-11-08: "Make steel chariot the main focus or featured"): its banner, linked to its page
    body = f"""<a class="hero" href="steel-chariot.html" aria-label="Brimstone &amp; Buckshot: Steel Chariot - coming soon to Steam"><img src="assets/img/bb_hero.webp" alt="Brimstone &amp; Buckshot: Steel Chariot - coming soon to Steam" width="1920" height="560"></a>
<main class="wrap">
<section class="section"><p class="h-label">Featured</p>
<div id="feat" style="position:relative"><button class="arrow l" type="button" aria-label="Previous">&#8249;</button>{slides}<button class="arrow r" type="button" aria-label="Next">&#8250;</button></div>
<div class="dots" id="featDots"></div></section>
<section class="section"><p class="h-label">Our games &amp; projects</p><div class="caps">
<a class="cap" href="steel-chariot.html"><img src="assets/img/bb_capsule.webp" alt="Brimstone &amp; Buckshot: Steel Chariot"><div class="ct">Brimstone &amp; Buckshot: Steel Chariot<span>Coming soon</span></div></a>
<a class="cap" href="neon-noon.html"><img src="assets/img/nn_capsule.webp" alt="Neon Noon"><div class="ct">Neon Noon<span>On Google Play</span></div></a>
<a class="cap" href="no-people-no-stories.html"><img src="assets/img/npns_capsule.webp" alt="No People, No Stories"><div class="ct">No People, No Stories<span>Free</span></div></a>
<a class="cap" href="dead-mans-hand.html"><img src="assets/img/dmh_capsule.webp" alt="Neon Noon: Dead Man's Hand"><div class="ct">Neon Noon: Dead Man's Hand<span>On Google Play</span></div></a>
<a class="cap" href="#vtube-live"><div class="vt"><img src="assets/img/vtubelive_icon.webp" alt="Vtube Live"></div><div class="ct">Vtube Live<span>In development</span></div></a>
</div></section>
<section class="section" id="vtube-live"><p class="h-label">Coming soon</p><div class="vtube"><img src="assets/img/vtubelive_icon.webp" alt="Vtube Live icon">
<div><h2>Vtube Live</h2><p class="muted">A VTuber app from Lux Cor Games: build your avatar and go live. In development.</p>{tags(["VTuber", "Avatar", "Streaming", "In development"])}</div></div></section>
<section class="section" id="community"><p class="h-label">Community</p><div class="buy" style="margin:0"><div><h2>Join the community</h2><p>News, development updates, trailers and a place to talk about the games. On X and YouTube: {X_HANDLE}</p></div><div style="display:flex;gap:8px;flex-wrap:wrap"><a class="btn" href="{DISCORD}" rel="noopener">Join the Discord</a><a class="btn" href="{X_URL}" rel="noopener">Follow on X</a><a class="btn" href="{YT_URL}" rel="noopener">Watch on YouTube</a></div></div></section>
<section class="section"><p class="h-label">About the studio</p><p style="max-width:68ch">Lux Cor Games is an American indie studio, and we're gamers first: we make the games we want to play, in whatever genre that takes us. More are on the way. <a href="about.html">More about us</a></p></section>
</main>"""
    page("index.html", "Lux Cor Games", "Games by Lux Cor Games: Brimstone & Buckshot: Steel Chariot, coming soon to Steam; Neon Noon and Neon Noon: Dead Man's Hand, on Google Play now and coming to Steam, and No People, No Stories, free now.", body, "home")

def tips():   # the "Support the studio" box (About page)
    btns = (f'<a class="btn" href="{KOFI}" rel="noopener">Tip on Ko-fi</a>' if KOFI else "") + (f'<a class="btn" href="{STRIPE_TIP}" rel="noopener">Card, Apple Pay or Google Pay</a>' if STRIPE_TIP and STRIPE_LIVE else "")
    if not btns: return ""
    return f"""<h2 id="support-us">Support the studio</h2>
<div class="buy" style="margin:0 0 8px"><div><p style="margin:0">Like what we make? A tip goes straight into the games: art, music, tools and the time to make them right. Every tip helps, and every one gets read.</p></div><div style="display:flex;gap:8px;flex-wrap:wrap">{btns}</div></div>"""

def thanks():   # where the Stripe link sends a supporter after paying (and a page to point Ko-fi's thank-you at)
    body = f"""<main class="wrap doc" style="text-align:center"><h1>Thank you!</h1>
<p style="font-size:1.15em">You just put fuel in the chariot. Your tip goes straight into the games, and we read every one.</p>
<p>Come say hi on our <a href="{DISCORD}" rel="noopener">Discord</a>, follow <a href="{X_URL}" rel="noopener">{X_HANDLE}</a> on X, and hear our soundtracks on <a href="{YT_URL}" rel="noopener">YouTube</a>.</p>
<p style="margin-top:28px"><a class="btn" href="index.html">Back to the games</a></p></main>"""
    page("thanks.html", "Thank you · Lux Cor Games", "Thank you for supporting Lux Cor Games.", body, "about")

def about():   # owner 2026-11-09: "we need an 'about us' page on the website as well" (DRAFT for the owner's review)
    games = "".join(f'<li><a href="{g["file"]}">{g["title"]}</a>: {g["blurb"][0].lower() + g["blurb"][1:].rstrip(".")}. <span class="muted">{g.get("badge", "Coming soon")}.</span></li>' for g in GAMES.values())
    body = f"""<main class="wrap doc"><h1>About Lux Cor Games</h1>
<p>Lux Cor Games is an American indie studio, and we're gamers first. We make the games we want to play: the ones we'd stay up too late for, tell our friends about and come back to. If it isn't fun for us, it doesn't ship.</p>
<p>We don't stick to one genre. So far that's meant a cyberpunk western, a back-room poker game, a quiet walk through empty places and a zombie-smashing chariot with a cross welded to the plow. Whatever we make next, it'll be made the same way: by people who love games, for people who love games.</p>
<h2>Our games so far</h2>
<ul>{games}<li><a href="index.html#vtube-live">Vtube Live</a>: a VTuber app for building your avatar and going live. <span class="muted">In development.</span></li></ul>
<p>And we're just getting started. More games are on the way, in genres we haven't touched yet.</p>
<h2>How we work</h2>
<p>Every game is our own: original stories and original worlds, built in-house. We'd rather ship a small game that's finished than a big one that isn't, and we keep working on our games after launch.</p>
<p>We make games for PC (Windows, Linux and SteamOS) and Android, and we test on the Steam Deck. Every game has a "report a problem" button, and every report gets read.</p>
{tips()}
<h2>Say hello</h2>
<p>Questions, help, feedback and ideas: <span class="mail">{SUPPORT}</span></p>
<p>Join us on <a href="{DISCORD}" rel="noopener">Discord</a>, follow <a href="{X_URL}" rel="noopener">{X_HANDLE}</a> on X, and watch trailers and hear our soundtracks on <a href="{YT_URL}" rel="noopener">YouTube</a>.</p></main>"""
    page("about.html", "About · Lux Cor Games", "About Lux Cor Games, an American indie studio of gamers making the games we want to play: what we\'ve made so far, what\'s next and how we work.", body, "about")

def support():
    body = f"""<main class="wrap doc"><h1>Support</h1>
<p>Stuck, found a bug, or have a question about one of our games? We read everything.</p>
<div class="panel"><p style="margin:0">Questions, help, game feedback and ideas: <span class="mail">{SUPPORT}</span></p></div>
<h2>Community</h2><p>Talk to us and other players on our <a href="{DISCORD}" rel="noopener">Discord server</a>, or follow <a href="{X_URL}" rel="noopener">{X_HANDLE}</a> on X for news. Trailers and videos are on our <a href="{YT_URL}" rel="noopener">YouTube channel</a>.</p>
<h2>Reporting a bug from inside the game</h2><p>Every Lux Cor Games game has a "report a problem" button. It sends us a short note and a screenshot of where you are, so we can see exactly what went wrong. See our <a href="privacy.html">Privacy Policy</a> for what a report contains.</p>
<h2>Deleting your data</h2><p>Our games don't create accounts or collect anything automatically. If you sent a bug report and want it deleted, email <span class="mail">{SUPPORT}</span> and we'll remove it.</p>
<h2>Refunds</h2><p>Purchases and refunds are handled by the store you bought from (Google Play or Steam).</p></main>"""
    page("support.html", "Support · Lux Cor Games", "Help and contact for Lux Cor Games games.", body, "support")

def privacy():
    body = f"""<main class="wrap doc"><h1>Privacy Policy</h1><p class="muted">Effective November 9, 2026</p>
<p>This policy covers all games by Lux Cor Games ("we"), including Brimstone &amp; Buckshot: Steel Chariot, Neon Noon, Neon Noon: Dead Man's Hand and No People, No Stories, on every platform, and this website.</p>
<p><b>The short version:</b> our games don't collect anything about you unless you choose to send us a bug report. There are no ads, no tracking, no analytics and no accounts.</p>
<h2>Update check (No People, No Stories)</h2><p>When it starts, No People, No Stories asks GitHub once whether a newer version is out. The request carries only the game's version number; like any web request, GitHub sees your internet address. Nothing else is sent, and we receive nothing from it.</p>
<h2>What stays on your device</h2><p>Your saves, settings and progress are stored only on your device. We never see them.</p>
<h2>Bug reports (only if you send one)</h2><p>Each game has a "report a problem" button. Nothing is sent unless you write a report and press Send. A report can include:</p>
<ul><li>the message you write, and your name or email only if you choose to add them;</li><li>a screenshot of the game screen at that moment;</li>
<li>the game's version number and the type of device or operating system;</li><li>where you were in the game, such as the chapter and the last few lines of story shown.</li></ul>
<p>Reports are sent securely (HTTPS) to a private Google spreadsheet that only we can read. We use them only to find and fix problems. We don't sell or share them, and we delete them when they're no longer needed or when you ask us to.</p>
<h2>Store platforms</h2><p>Purchases are handled by the store you buy from, such as Google Play or Steam, under their own privacy policies. On Steam, achievements are recorded through Steam. We don't receive your payment details.</p>
<h2>Tips</h2><p>If you tip us on our website, the payment is handled by Ko-fi or Stripe under their own privacy policies. We receive the amount and whatever they pass on, such as your name, your email and any message you leave. We never see your card details. We use this only to thank you and keep our books, and we don't sell or share it.</p>
{COUNTER_PRIVACY}<h2>Children</h2><p>Our games are made for adults and aren't directed at children under 13. We don't knowingly collect information from children.</p>
<h2>Your choices</h2><p>To have a bug report you sent deleted, or to ask any question about privacy, email us at <span class="mail">{SUPPORT}</span>. We'll reply within 30 days.</p>
<h2>Changes</h2><p>If this policy changes, we'll update the date at the top of this page.</p></main>"""
    page("privacy.html", "Privacy Policy · Lux Cor Games", "Privacy policy for Lux Cor Games games.", body, "privacy")

if __name__ == "__main__":
    home(); game_page("bb"); game_page("nn"); game_page("npns"); game_page("dmh"); about(); thanks(); support(); privacy()
    print("built:", ", ".join(sorted(f for f in os.listdir(HERE) if f.endswith(".html"))))
