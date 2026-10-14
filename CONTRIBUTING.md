# Adding a context layer

A context layer lights up a set of buildings that share a piece of history, and tells why each one is there.
There are two kinds. Pick the one that fits, open a pull request, and describe the layer in a sentence or two.

## 1. A hand-picked layer (most contributions)

Add an entry to `CURATED` in [`pipeline/curated.py`](pipeline/curated.py):

```python
CURATED.append(dict(
    id="markets", section="Trade and empire", title="Markets", era="1600–today",
    intro="Two or three sentences on the history behind the layer.",
    entries=[
        # (name, Wikidata item, story, "en:Wikipedia title", (facts the article must contain), NHLE number or None, group)
        ("Leadenhall Market", "Q1144626",
         "A covered market on the site of the Roman forum; the present roof dates from 1881.",
         "en:Leadenhall Market", ("1881",), None, "markets"),
    ]))
```

Rules, checked by `uv run python -m pipeline.s08_curated`:

- **Every story rests on a Wikipedia article.** The checks are strings that must appear in it: a year, a name, a key word.
  If the article does not say it, the story should not either.
- **The building is named by its Wikidata item**, which must have coordinates on the building. When the item has a
  National Heritage List number, the footprints listed under it are used.
- **Stories are short and plain:** one or two sentences, what happened and when. Legends are named as legends.
- **No personal data about private people.** Public figures are fine.

The script prints `layer n/m` and every entry it dropped with the reason. A layer needs five to ten buildings or more;
smaller sets fit better in an existing layer.


## 2. A layer from an open dataset

Add a function to [`pipeline/layers.py`](pipeline/layers.py) with the `@layer(...)` decorator. It returns
`{building id: group}` or `{building id: (group, {"story": ...})}`; `buildings()` gives every footprint with its id,
year, listing and geometry (British National Grid). Add a download step for the dataset as a `pipeline/s00_fetch_*.py`
and say which licence it carries; only openly licensed data can go in.

## Checking your layer

```bash
uv run python -m pipeline.s08_curated   # hand-picked layers
uv run python -m pipeline.s05_layers    # counts per group
uv run python -m pipeline.s03_tiles
python3 -m http.server 8645 --directory web
```
