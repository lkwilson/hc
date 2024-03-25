# HC

# Building conda pkg

```bash
export CONDA_SSH_ALIAS=conda_server
export INDEX_CMD='~/bin/pull_conda'
./upload.sh
```

# Building docker

```bash
docker build -t hc --build-arg CONDA_REPO=http://my_conda_repo.example.com/conda/channel .
```

# Running in docker

```
docker compose up
```
