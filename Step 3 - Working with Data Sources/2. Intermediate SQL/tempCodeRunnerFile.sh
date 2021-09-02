sqlite3 new_database.db <<'EOF'
.tables
.headers on
.mode column
CREATE TABLE user(
    user_id INTEGER,
    first_name TEXT,
    last_name TEXT
);
.schema user
.quit
EOF