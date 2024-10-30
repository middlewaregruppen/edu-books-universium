# 📚 Python apps for training

In this repo we have a few demo apps written in Python that were designed to be
used in training environments.

1. The `books-universium` directory contains a Python app and a Dockerfile to containerise
   it
2. The `demo-comics` directory is another Python app and Dockerfile

These images are built and deployed to Github packages and can be pulled via:

```bash
# books
docker pull ghcr.io/middlewaregruppen/books-universium:0.1.1
# comics
docker pull ghcr.io/middlewaregruppen/comics:0.21
```
