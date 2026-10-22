# rsmify host service image (bead rsm-ddx.12).
#
# The build context is the rsm repo root, because rsmify depends on rsm-lang
# (this repo) and the tree-sitter-rsm submodule. Build from the repo root:
#
#   docker build -f packages/rsmify/Dockerfile -t rsmify:local .
#
# pandoc runs the LaTeX-to-RSM conversion. The container runs non-root and
# writes only under /scratch (TMPDIR), which the systemd unit mounts as a
# tmpfs, so it needs no host filesystem beyond that scratch dir.

FROM python:3.13-slim

# build-essential compiles the tree-sitter-rsm native parser during uv sync;
# pandoc is the importer; curl is only for the container healthcheck.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential pandoc curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Pinned uv, copied from the official image.
COPY --from=ghcr.io/astral-sh/uv:0.9.9 /uv /usr/local/bin/uv

WORKDIR /app

# Only the parts needed to build rsm-lang and rsmify, to keep the context small.
COPY pyproject.toml uv.lock README.md LICENSE.md ./
COPY rsm/ ./rsm/
COPY braiid/ ./braiid/
COPY tree-sitter-rsm/ ./tree-sitter-rsm/
COPY packages/rsmify/ ./packages/rsmify/

WORKDIR /app/packages/rsmify
# rsm-lang resolves via its path source (../..); --frozen pins to the lockfile.
RUN uv sync --no-dev --frozen

# Non-root, with a scratch dir for the arXiv tarballs the fetcher extracts.
RUN useradd --create-home --uid 10001 rsmify \
    && mkdir -p /scratch && chown rsmify:rsmify /scratch
ENV TMPDIR=/scratch \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
USER rsmify

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD curl -fsS http://127.0.0.1:8000/healthz || exit 1

# Invoke the venv's uvicorn directly: uv at runtime would try to write a cache
# under $HOME, which the read-only rootfs forbids.
CMD ["/app/packages/rsmify/.venv/bin/uvicorn", "rsmify.main:app", "--host", "0.0.0.0", "--port", "8000"]
