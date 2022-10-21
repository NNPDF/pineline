# Consuming Theory

- official NNPDF theories: https://nnpdf.web.cern.ch/nnpdf/tables/
- other NNPDF stuffs (including fits): https://data.nnpdf.science/

[Infos on servers](https://docs.nnpdf.science/serverconf/index.html) are not
very detailed about the content, and also incomplete, since the theories
location is not listed (and it is nowhere in the docs).

Maybe we can provide the part we are interested in (theories) on our docs, at
the cost of duplication.

## Non-standard grids

We can consider to maintain a set of interesting grids somewhere, even if we
don't fit them, since we are using them for studies.
We don't need to do it for FkTables as well, since they are only used for the
fit (otherwise the evolution is provided by LHAPDF).

If there is already a standard location for them I'm simply not aware of it.

## How to consume a theory

Downloading a theory it is currently done by `validphys`, but it is not
extremely simple to learn how to use the `API` class, especially if you are not
familiar with the fit.

Since we want to have more users than NNPDF, maybe we want to become more
`validphys` independent.

At the moment, an example to load a theory for something that is not fully
managed by `validphys` is provided at:
https://github.com/NNPDF/mcpdf/blob/cb43028ce8f62329cd055e21608e0a6b7bce5b3c/src/mcpdf/nnpdf/theory.py

It requires loading data, and it is done internally importing:
https://github.com/NNPDF/mcpdf/blob/cb43028ce8f62329cd055e21608e0a6b7bce5b3c/src/mcpdf/nnpdf/data.py
but it can also be used manually.

## Using an FkTable/grid

We should put at least the most basic example on the Pineline website, and
redirect to https://pineappl.readthedocs.io/ for more complex ones.

We should also update the docs, since the ["Recipes"
section](https://pineappl.readthedocs.io/en/latest/recipes.html) uses
`grid.Grid.convolute()` that is not any longer available (I found bindings only
for
[`grid.Grid.convolute_with_one`](https://pineappl.readthedocs.io/en/latest/modules/pineappl/pineappl.html#pineappl.grid.Grid.convolute_with_one),
that indeed it is documented).

## LHAPDF

Maybe we should consider spending a few more words on what is an PDF-like
object, if possible explicitly implementing (somewhere in the code) a `PDFlike`
interface.
Not everyone is familiar with LHAPDF API:
https://lhapdf.hepforge.org/modules.html
