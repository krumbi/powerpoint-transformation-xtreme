FROM python:latest

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  INPUT="" \
  NAME=""

# Copy only requirements to cache them in docker layer
WORKDIR /test

# Creating folders, and files for a project:
COPY src/ ./

ENTRYPOINT python3 docker.py ${INPUT} ${NAME}
