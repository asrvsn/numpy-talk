# Building

Ubuntu:
```bash
sudo apt-get install build-essential libomp-dev -y
```

Docker:
```bash
# Build
docker build --platform linux/amd64 . -f docker/Dockerfile -t kuramoto
```

# Running

Profile time:
```bash
./bin/main -N 100 -K 2 -T 1000 -p
```

Profile memory:
```bash
mprof run ./bin/main -N 100 -K 2 -T 1000
mprof plot --flame
```

Docker:
```bash
docker run -it kuramoto 
```