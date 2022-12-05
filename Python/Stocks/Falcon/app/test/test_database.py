import database as db
import pytest
import sqlite3


@pytest.mark.database
def test_connection():
    b = db.DatabaseConnection()
    assert b.connection is not None


@pytest.mark.database
def test_cursor():
    b = db.DatabaseConnection()
    assert b.cursor is not None
