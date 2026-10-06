# Webprogramozás I – A web működése, szabványai és minősége

A tantárgy a webet nyílt, elosztott információs rendszerként mutatja be. A hallgató a kurzus végére áttekinti, hogyan kapcsolódnak össze a hálózatok, a böngészők, a szerverek, a webes adatok és a szabványok, majd e tudás alapján értelmezni tudja a webes rendszerek biztonsági, hozzáférhetőségi és teljesítményi döntéseit. A hangsúly a tartós fogalmakon és összefüggéseken van.

## A tárgy célja és haszna

A webes szolgáltatások használata és készítése sok informatikai szakterületet érint. A tárgy abban segít, hogy a hallgató ne csak egy felületet lásson, hanem megértse a mögötte zajló kommunikációt, a résztvevők feladatait és azokat a kompromisszumokat, amelyek a szolgáltatás minőségét meghatározzák. Az itt megszerzett szemlélet fejlesztésnél, üzemeltetésnél, biztonsági elemzésnél és digitális szolgáltatások értékelésénél is használható.

## Elvárt tanulási eredmények

A kurzus végére a hallgató:

- különbséget tud tenni az internet és a World Wide Web között, és el tudja magyarázni a web fő szereplőinek kapcsolatát;
- követni tudja egy webes kérés útját, és fogalmi szinten értelmezi a HTTP, HTTPS, DNS és TLS szerepét;
- felismeri a webes dokumentumok, böngészők, API-k és alkalmazásmodellek alapvető feladatait;
- értelmezni tudja az azonosítás, jogosultságkezelés és webbiztonság alapfogalmait;
- meg tud nevezni hozzáférhetőségi, adatvédelmi, teljesítményi és megbízhatósági szempontokat egy webes szolgáltatás értékelésekor.

## Hetek és fejezetek

### 01. hét – Mi a web?

Az első hét a web jelentőségéből indul ki, majd történeti fejlődését, fő szereplőit, kliens–szerver modelljét és nyílt szabványait egy közös rendszer részeként tárgyalja. Az internet és a web különbsége a heti bevezetésben jelenik meg.


- [01.01. A web mint általános platform](01-01-web-as-a-platform.md) — a web szerepe az informatikai szakterületek között.
- [01.02. A web fejlődése](01-02-web-evolution.md) — a dokumentumközpontú és az alkalmazásszerű web kapcsolata.
- [01.03. A web fő szereplői](01-03-web-actors.md) — a böngésző, szerver, tartalomszolgáltató és közvetítők feladata.
- [01.04. Kliens–szerver modell és rétegek](01-04-client-server-and-multitier.md) — a kérés–válasz működés és a logikai rétegek.
- [01.05. Webszabványok és interoperabilitás](01-05-web-standards-and-interoperability.md) — a nyílt szabályok szerepe a rendszerek együttműködésében.

### 02. hét – Webcímek és HTTP-alapok

A második hét megmutatja, hogyan nevezünk meg egy webes erőforrást, hogyan kérjük el, és hogyan olvassuk a választ. A metódusokat, státuszkódokat és fejléceket a böngésző Network paneljében is összekapcsolja.


- [02.01. Webcímek és erőforrások](02-01-web-addresses-and-resources.md) — az URL részei és az erőforrás fogalma.
- [02.02. A HTTP-kérés és -válasz](02-02-http-request-and-response.md) — a kliens és a szerver üzenetváltása.
- [02.03. HTTP-metódusok](02-03-http-methods.md) — a kérés szándéka és a GET, POST alapvető különbsége.
- [02.04. HTTP-státuszkódok](02-04-http-status-codes.md) — a válasz eredményének értelmezése.
- [02.05. Fejlécek, törzs és tartalomtípusok](02-05-headers-body-and-content-types.md) — az üzenet további részei és a HTML/JSON különbsége.
- [02.06. Egy kérés megfigyelése](02-06-reading-network-panel.md) — a Network panel alapvető olvasása.

### 03. hét – Böngésző és webes dokumentum

A HTML, CSS és JavaScript szerepét, a DOM-ot, a renderelést és az erőforrások betöltését vizsgálja. Kitér a szemantikus dokumentumokra, a Can I use? használatára, valamint a helyi fájlok, az IndexedDB és a WebGL böngészős szerepére.


- [03.01. HTML, CSS és JavaScript](03-01-html-css-and-javascript.md) — a webes felület szerkezete, megjelenése és viselkedése.
- [03.02. Dokumentumszerkezet, DOM és szemantika](03-02-document-structure-and-dom.md) — a HTML-forrás és az aktuális dokumentumfa különbsége.
- [03.03. Böngészős renderelés](03-03-browser-rendering.md) — a dokumentumtól a látható felületig vezető lépések.
- [03.04. Webes erőforrások betöltése](03-04-loading-web-resources.md) — képek, stíluslapok, szkriptek és más fájlok kérései.
- [03.05. Böngészőkompatibilitás](03-05-browser-compatibility.md) — használhatóság különböző környezetekben és a Can I use? támogatottsági táblázatai.
- [03.06. A böngésző képességei](03-06-browser-capabilities.md) — helyi fájlok, IndexedDB, Canvas/WebGL és egyéb böngésző API-k.

### 04. hét – Egy webes kérés teljes útja

A már ismert URL-eket, HTTP-üzeneteket és böngészős erőforrásokat összekapcsolva követi végig a névfeloldást, a kapcsolatot és a közvetítő rendszereket. A DNS, TCP, TLS, proxyk és CDN-ek szerepét fogalmi szinten tárgyalja.


- [04.01. Domainnév, IP-cím és DNS](04-01-dns-and-ip-addresses.md) — a hosztnévtől a hálózati címig vezető lépések.
- [04.02. Kapcsolatfelépítés, TCP és TLS](04-02-connection-tcp-and-tls.md) — a szállítás és a védett kommunikáció szerepe.
- [04.03. A HTTPS védelme és határai](04-03-https-protection-and-limits.md) — titkosság, sértetlenség, szerverazonosítás és a védelem korlátai.
- [04.04. Proxyk, reverse proxyk és CDN-ek](04-04-proxies-and-cdns.md) — közvetítők és tartalomkézbesítés.
- [04.05. Egy webes kérés teljes útja](04-05-complete-web-request.md) — a webcímtől a használható felületig.
- [04.06. Késleltetés és hibák](04-06-latency-and-failures.md) — a különböző szakaszok tüneteinek értelmezése.

### 05. hét – Webes adatok és API-k

Az API-k, a JSON és XML adatcsere, a REST, GraphQL és RPC alapfogalmait rendezi el. Bemutatja a valós idejű kommunikáció és a verziózás szerepét is.


- [05.01. Mi a webes API?](05-01-what-is-a-web-api.md) — a programok közötti szerződés és annak részei.
- [05.02. JSON, XML és strukturált adatok](05-02-json-xml-and-data.md) — az adatok formája, jelentése és hiányzó értékei.
- [05.03. REST és HTTP-erőforrások](05-03-rest-and-http-resources.md) — erőforrások, metódusok és válaszok.
- [05.04. GraphQL és RPC](05-04-graphql-and-rpc.md) — mezőválasztás és műveletközpontú API-k.
- [05.05. Változó adatok és események](05-05-changing-data-and-events.md) — polling, SSE, WebSocket és webhook.
- [05.06. Verziózás és dokumentáció](05-06-api-evolution-and-documentation.md) — kompatibilitás, változások és az API leírása.

### 06. hét – Webes alkalmazások és renderelési stratégiák

Összehasonlítja a többoldalas és egyoldalas alkalmazásokat, a kliensoldali, szerveroldali és statikus renderelést. Az architektúraválasztás szempontjait a felhasználói célhoz és az előző héten megismert adatcseréhez köti.


- [06.01. Többoldalas és egyoldalas alkalmazások](06-01-multi-page-and-single-page-apps.md) — MPA, SPA és navigáció.
- [06.02. Kliensoldali renderelés](06-02-client-side-rendering.md) — JavaScript, API-adat és a böngészőben felépülő nézet.
- [06.03. Szerveroldali renderelés](06-03-server-side-rendering.md) — kéréskor előállított HTML és hidratálás.
- [06.04. Statikus és hibrid renderelés](06-04-static-rendering-and-hybrids.md) — előre készített HTML és vegyes stratégiák.
- [06.05. Navigáció és kliensoldali állapot](06-05-navigation-and-client-state.md) — URL, előzmények és helyi állapot.
- [06.06. Service worker és offline működés](06-06-service-workers-and-offline.md) — erőforrások gyorsítótárazása és az offline használat határai.
- [06.07. Architektúraválasztás](06-07-choosing-an-application-architecture.md) — modell és renderelés a felhasználói feladathoz igazítva.

### 07. hét – Állapot, identitás és hozzáférés

Az állapotmentes HTTP mellett szükséges állapotkezelést, a cookie-kat, munkameneteket és tokeneket tárgyalja. Elkülöníti a hitelesítést a jogosultságkezeléstől, majd bevezeti a külső bejelentkezés és az egyszeri bejelentkezés alapgondolatát.


- [07.01. Állapotmentes HTTP és alkalmazási állapot](07-01-stateless-http-and-application-state.md) — külön kérések és felhasználói folytonosság.
- [07.02. Cookie-k és munkamenetek](07-02-cookies-and-sessions.md) — munkamenet-azonosító és szerveroldali állapot.
- [07.03. Böngészős tárolás és tokenek](07-03-browser-storage-and-tokens.md) — localStorage, sessionStorage, IndexedDB és hozzáférési értékek.
- [07.04. Hitelesítés és jogosultság](07-04-authentication-and-authorization.md) — identitás és műveleti engedély különbsége.
- [07.05. OAuth 2.0 és OpenID Connect](07-05-oauth-and-openid-connect.md) — delegált hozzáférés és külső identitás.
- [07.06. Egyszeri és külső bejelentkezés](07-06-sso-and-external-login.md) — közös identitásszolgáltató és helyi munkamenetek.

### 08. hét – Webbiztonsági alapok

Fenyegetési modellből kiindulva vizsgálja a same-origin policy, CORS, XSS, CSRF és injekciós támadások szerepét. Kitér a jelszavak, többfaktoros hitelesítés és HTTPS védelmi szempontjaira.


- [08.01. Fenyegetési modell és bizalmi határok](08-01-threat-models-and-trust-boundaries.md) — védendő értékek, szereplők és a kérés határai.
- [08.02. Same-origin policy és CORS](08-02-same-origin-policy-and-cors.md) — az origin, a böngészős olvasás és a preflight.
- [08.03. XSS, CSRF és injekció](08-03-xss-csrf-and-injection.md) — három különböző támadási út és védelmi alapelv.
- [08.04. Jelszavak, MFA és munkamenetek](08-04-passwords-mfa-and-sessions.md) — jelszótárolás, második faktor és hozzáférési értékek.
- [08.05. A HTTPS szerepe és korlátai](08-05-https-and-its-limits.md) — a védett hálózati szakasz és az alkalmazási hibák különbsége.
- [08.06. OWASP és biztonsági áttekintés](08-06-owasp-and-security-review.md) — kockázati keret és egy jelentkezési folyamat elemzése.

### 09. hét – A minőségi web

Az akadálymentességet, szemantikát, reszponzivitást, teljesítményt és kereshetőséget a felhasználói élmény részeként tárgyalja. Az adatvédelmi és digitális etikai kérdéseket is ide kapcsolja.


- [09.01. Akadálymentesség és inkluzív tervezés](09-01-accessibility-and-inclusive-design.md) — eltérő használati helyzetek és a WCAG szemlélete.
- [09.02. Szemantika, billentyűzet és képernyőolvasó](09-02-semantics-keyboard-and-screen-readers.md) — a dokumentum jelentése és kezelhetősége.
- [09.03. Reszponzív és eszközfüggetlen megjelenés](09-03-responsive-and-device-independent-design.md) — rugalmas elrendezés és eltérő beviteli módok.
- [09.04. Felhasználói szempontú teljesítmény](09-04-user-perceived-performance.md) — látható tartalom, interakció és stabilitás.
- [09.05. Kereshetőség és tartalmi minőség](09-05-searchability-and-content-quality.md) — feltérképezés, indexelés és hasznos tartalom.
- [09.06. Adatvédelem, követés és digitális etika](09-06-privacy-tracking-and-digital-ethics.md) — adatgyűjtés, hozzájárulás és valódi választás.

### 10. hét – Megbízható és nagy teljesítményű web

A rendelkezésre állás, hibakezelés, betöltési idő, gyorsítótárazás és terhelési csúcsok fogalmait fogja össze. Megmutatja, hogyan hatnak egymásra a teljesítmény, a biztonság és a költségek.


- [10.01. Szolgáltatásminőség és rendelkezésre állás](10-01-service-quality-and-availability.md) — felhasználói célok, helyreállás, SLI, SLO és SLA.
- [10.02. Hibakezelés és felhasználói kommunikáció](10-02-errors-and-user-communication.md) — státuszkódok, világos visszajelzés és újrapróbálkozás.
- [10.03. Válaszidő, betöltés és erőforrásigény](10-03-response-time-load-and-resources.md) — a teljes kérési út és a lassú esetek mérése.
- [10.04. HTTP-gyorsítótár és CDN](10-04-http-cache-and-cdn.md) — cache-rétegek, frissesség és földrajzi távolság.
- [10.05. Terhelési csúcs és megfigyelhetőség](10-05-load-peaks-and-observability.md) — várakozási sor, fokozatos szolgáltatáscsökkentés és diagnózis.
- [10.06. Teljesítmény, biztonság és költség](10-06-performance-security-and-cost.md) — tudatos kompromisszumok az alkalmazás céljaihoz mérve.

## Kurzusinformációk

A teljesítés, értékelés és beadás végleges szabályait a kurzus külön, hallgatóknak kiadott dokumentumai rögzítik. Ez az áttekintő nem állapít meg önálló határidőt vagy pontozást.
