FROM python:latest

ARG OUTPUT_PATH=/text-to-text/output

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  INPUT_PATH=/text-to-text/input.pptx \
  OUTPUT_PATH=$OUTPUT_PATH \
  API_KEY=xyz \
  OPENAI_MODEL=gpt-3.5-turbo-16k \
  MODEL_TEMPERATURE=0.3 \
  OUTPUT_LANGUAGE=en \
  PROMPT_ADDITION=""

# System deps:
RUN pip install "poetry"

# Copy only requirements to cache them in docker layer
WORKDIR /text-to-text

COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY src/ ./

RUN mkdir -p $OUTPUT_PATH

ENTRYPOINT ["sh", "-c", "python3", "main.py", "${INPUT_PATH}", "${API_KEY}", "-o ${OUTPUT_PATH}", "-m ${OPENAI_MODEL}", "-t ${MODEL_TEMPERATURE}", "-l ${OUTPUT_LANGUAGE}", "-p ${PROMPT_ADDITION}", "-d"]

#CMD ["${INPUT_PATH}", "${API_KEY}", "-o ${OUTPUT_PATH}", "-m ${OPENAI_MODEL}", "-t ${MODEL_TEMPERATURE}", "-l ${OUTPUT_LANGUAGE}", "-p ${PROMPT_ADDITION}", "-d"]
