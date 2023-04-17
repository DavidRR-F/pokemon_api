# Use the official PostgreSQL image as the base
FROM postgres:latest

# Set environment variables for the database
ENV POSTGRES_DB=mydb
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Copy the SQL script to create tables
COPY pokemon.csv /csv/
COPY create_tables.sql /docker-entrypoint-initdb.d/
