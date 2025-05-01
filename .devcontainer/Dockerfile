# .devcontainer/Dockerfile
ARG VARIANT=3.12
FROM --platform=linux/arm64 python:${VARIANT}-slim

# ---------- OS パッケージ ----------
#   * geopandas / pyogrio → GDAL, PROJ, GEOS
#   * openpyxl などは pure-python
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    build-essential g++ \
    gdal-bin libgdal-dev \
    libproj-dev proj-data proj-bin \
    libgeos-dev && \
    rm -rf /var/lib/apt/lists/*

# ---------- Python パッケージ ----------
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# ---------- デフォルト ----------
WORKDIR /workspace
CMD ["bash"]
