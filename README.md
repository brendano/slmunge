Scripts to munge certain machine learning sparse data formats, specifically the
common pattern of a sparse feature matrix plus a column of labels/predictions.  

Formats are

* `sl` -- the SVMLight/LibSVM format, loosely as described at http://svmlight.joachims.org/
* `coord` -- 1-indexed i,j,val coordinate-format triples.  (matlab-compatible)
* `mm` -- MatrixMarket header file, as required by R's Matrix package.  http://math.nist.gov/MatrixMarket/formats.html
* `megam` -- one of the variants described at http://www.cs.utah.edu/~hal/megam/
* `dense` -- delimited
