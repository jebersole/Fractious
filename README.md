# Fractious

This is the world's best fractal generator. Fully unit-tested, with an MVC architecture. Most Probably.

## Testing

So far, a rudimentary complex number class has been implemented in Complex.py. To test it, use `python complextest.py`.  To measure test coverage, install `python-coverage` and run `python-coverage -x complextest.py` followed by `python-coverage -rm -o /usr`. Current output:

```
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
Complex          17      0   100%   
complextest      68      0   100%   
-------------------------------------------
TOTAL            85      0   100%
```