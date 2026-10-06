# Courses

Hallgatóknak szóló, nyilvános tananyagok egyetlen kereshető weboldalon.

A publikált oldal: https://laborci.github.io/courses/

## Szerkezet

- `docs/index.md`: közös kezdőlap.
- `docs/<tárgy>/index.md`: tárgy kezdőlapja.
- `docs/<tárgy>/hu/`: magyar kurzusáttekintő és önálló fejezetek.
- `scripts/import_course.py`: egy helyi kurzus hallgatói anyagainak átvétele.
- `mkdocs.yml`: a generált navigáció és a megjelenés beállítása.

Az oktatói `HH-00-*.md` PWMD-prezentációk, a `course-plan.md` és más szerkesztői fájlok nem kerülnek ebbe a repositoryba. A GitHub Pages oldala nyilvános, ezért ide csak nyilvánosan megosztható anyag kerülhet.

## Új tárgy hozzáadása

Másold a hallgatói fájlokat a `docs/<tárgy>/hu/` könyvtárba. A kezdőlap neve `index.md`, az áttekintőé `00-syllabus.md`. A fejezetek a `HH-FF-title.md` mintát követik. A navigációt a `python3 scripts/generate_navigation.py` parancs újragenerálja. Egy új tárgyhoz nem kell új repository vagy külön Pages-oldal.

Az itt használt kurzusszerkezetből az importáló script is képes átmásolni a hallgatói fájlokat:

```sh
python3 scripts/import_course.py /helyi/kurzus/hu web-programming-1 --title 'Webprogramozás I'
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
