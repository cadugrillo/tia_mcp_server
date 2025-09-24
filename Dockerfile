FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install Mono
# Add the Mono Project GPG key and repository
RUN apt-get update && \
    apt-get install -y gnupg ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/debian stable-buster main" | tee /etc/apt/sources.list.d/mono-official-stable.list

# Update package lists and install mono-complete
RUN apt-get update && \
    apt-get install -y mono-complete && \
    rm -rf /var/lib/apt/lists/*

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "main.py"]