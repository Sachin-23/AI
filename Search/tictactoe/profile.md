Profiling Function calls

```python
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()

# ... do something ...

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
```

0. w/o AB pruning:
   as O
     59142936 
     787392
     21192
     1408
     118

1. AB pruning: 
   as O
     2585560
     106151
     7117
     991
     119
