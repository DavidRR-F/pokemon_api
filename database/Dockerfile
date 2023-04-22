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
    && cd pgvector && \
    make clean && \
    make OPTFLAGS="" && \
    make install && \
    mkdir /usr/share/doc/pgvector && \
    cp LICENSE README.md /usr/share/doc/pgvector && \
    rm -r /tmp/pgvector && \
    apt-get remove -y build-essential postgresql-server-dev-$PG_MAJOR && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN echo "CREATE EXTENSION vector;" > /docker-entrypoint-initdb.d/anable_pg_vector.sql
COPY pokemon-info.csv /csv/
COPY create_tables.sql /docker-entrypoint-initdb.d/
