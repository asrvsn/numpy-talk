```bash
kernprof -l ./bin/main -N 100 -K 2
python -m line_profiler main.lprof
```