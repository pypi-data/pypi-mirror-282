import psycopg2
import os


def close_conn(conn, cur):
    """
    Close the connection to the database.
    """
    cur.close()
    conn.close()


def get_conn():
    """
    Get a connection to the database.
    """
    db_host = os.environ.get("POSTGRES_HOST")
    db_password = os.environ.get("POSTGRES_PASSWORD")
    db_username = os.environ.get("POSTGRES_USER")
    return psycopg2.connect(
        database=os.environ.get("POSTGRES_DATABASE"),
        host=db_host,
        user=db_username,
        password=db_password,
        port=int(os.environ.get("POSTGRES_PORT")),
    )
