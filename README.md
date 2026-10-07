# Course portal

The published teaching portal is available at https://laborci.github.io/courses/.

The SvelteKit portal and Markdown materials are in `portal/`. The legacy MkDocs source remains in `docs/`.

```sh
cd portal
bun install --frozen-lockfile
bun run check
bun test
BASE_PATH=/courses bun run build
```

The GitHub Pages workflow builds and publishes `portal/build` on pushes to `main`.

---

# Courses

Hallgatóknak szóló, nyilvános tananyagok egyetlen kereshető weboldalon.

A publikált oldal: https://laborci.github.io/courses/

A felső menüben a nyelvek szerepelnek. A Magyar/English ágak alatt az évvel jelölt tárgyak és azok heti fejezetei jelennek meg. A Web Programming I (2026) magyar és angol változata egyaránt tíz heti tananyagot tartalmaz.

## Szerkezet

- `docs/index.md`: közös kezdőlap.
- `docs/hu/` és `docs/en/`: nyelvi kezdőlapok.
- `docs/<tárgy>/hu/` és később `docs/<tárgy>/en/`: nyelvenkénti kurzusáttekintő és önálló fejezetek.
- `scripts/import_course.py`: egy helyi kurzus hallgatói anyagainak átvétele.
- `mkdocs.yml`: a generált navigáció és a megjelenés beállítása.

Az oktatói `HH-00-*.md` PWMD-prezentációk, a `course-plan.md` és más szerkesztői fájlok nem kerülnek ebbe a repositoryba. A GitHub Pages oldala nyilvános, ezért ide csak nyilvánosan megosztható anyag kerülhet.

## Új tárgy hozzáadása

Másold a hallgatói fájlokat a `docs/<tárgy>/<nyelv>/` könyvtárba. A kezdőlap neve `index.md`, az áttekintőé `00-syllabus.md`. A fejezetek a `HH-FF-title.md` mintát követik. A navigációt a `python3 scripts/generate_navigation.py` parancs újragenerálja. Egy új tárgyhoz nem kell új repository vagy külön Pages-oldal.

Az itt használt kurzusszerkezetből az importáló script is képes átmásolni a hallgatói fájlokat:

```sh
python3 scripts/import_course.py /helyi/kurzus/hu web-programming-1 --title 'Webprogramozás I (2026)' --language hu
```

Az import után ellenőrizd a változásokat, futtasd a helyi buildet, majd commitold és pushold a frissítést. A GitHub Actions automatikusan újraépíti a weboldalt.

## Helyi ellenőrzés

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs build --strict
mkdocs serve
```
