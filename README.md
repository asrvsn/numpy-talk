```bash
./bin/main -N 100 -K 2 -T 1000 -p
```

Profiling (time and memory)
```bash
mprof run ./bin/main -N 100 -K 2 -T 1000
mprof plot --flame
```