-- Restricted read-only role for student SQL execution.
-- This user must never exist on the production Django database.

DO
$$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'sandbox_reader') THEN
        CREATE ROLE sandbox_reader LOGIN PASSWORD 'change-me-sandbox-password';
    END IF;
END
$$;

GRANT CONNECT ON DATABASE sql_sandbox TO sandbox_reader;
GRANT USAGE ON SCHEMA public TO sandbox_reader;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO sandbox_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON SEQUENCES TO sandbox_reader;

REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE CREATE ON SCHEMA public FROM sandbox_reader;
