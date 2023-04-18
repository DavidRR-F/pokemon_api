# Use the official PostgreSQL image as the base
ARG PG_MAJOR=15
FROM postgres:$PG_MAJOR
ARG PG_MAJOR

# Set environment variables for the database
ENV PGVECTOR_VERSION=0.4.1
ENV POSTGRES_DB=mydb
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        git \
        postgresql-server-dev-$PG_MAJOR \
    && cd /tmp \
    && git clone --branch v${PGVECTOR_VERSION} https://github.com/pgvector/pgvector.git \
    && cd pgvector \
    && make && make install \
    && cd / \
    && apt-get purge -y --auto-remove \
        build-essential \
        ca-certificates \
        git \
        postgresql-server-dev-$PG_MAJOR \
    && rm -rf /tmp/pgvector \
    && rm -rf /var/lib/apt/lists/*

COPY pokemon.csv /csv/
COPY create_tables.sql /docker-entrypoint-initdb.d/
