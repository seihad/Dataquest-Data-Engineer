#### 1.The SQLite Shell

# sqlite3 chinook.db <<'EOF'
# .tables
# .headers on
# .mode column
# SELECT name, track_id, composer FROM track LIMIT 3;
# .quit
# EOF

#### 2.Creating Tables
# sqlite3 new_database.db <<'EOF'
# .tables
# .headers on
# .mode column
# CREATE TABLE user(
#     user_id INTEGER,
#     first_name TEXT,
#     last_name TEXT
# );
# .schema user
# .quit
# EOF

#### 3.Primary and Foreign Keys
# sqlite3 chinook.db <<EOF
# CREATE TABLE wishlist (
#     wishlist_id INTEGER PRIMARY KEY,
#     customer_id INTEGER,
#     name TEXT,
#     FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
# );
# .quit
# EOF

#### 4.Database Normalization
# sqlite3 chinook.db <<EOF
# CREATE TABLE wishlist_track(
#     wishlist_id INTEGER,
#     track_id INTEGER,
#     PRIMARY KEY (wishlist_id, track_id),
#     FOREIGN KEY (wishlist_id) REFERENCES wishlist(wishlist_id),
#     FOREIGN KEY (track_id) REFERENCES track(track_id)
# );
# .schema wishlist_track
# .quit
# EOF

#### 5.Inserting and Deleting Rows
# sqlite3 chinook.db <<EOF
# INSERT INTO wishlist
# VALUES
#     (1, 34, "Joao's awesome wishlist"),
#     (2, 18, "Amy loves pop");
# INSERT INTO wishlist_track
# VALUES
#     (1, 1158),
#     (1, 2646),
#     (1, 1990),
#     (2, 3272),
#     (2, 3470);
# EOF

#### 6.Adding Columns to a Table
# sqlite3 chinook.db <<EOF
# ALTER TABLE wishlist
# ADD COLUMN active NUMERIC;
# ALTER TABLE wishlist_track
# ADD COLUMN active NUMERIC;
# EOF

#### 7.Adding Values to Existing Rows
# sqlite3 chinook.db <<EOF
# UPDATE wishlist
# SET active = 1;
# UPDATE wishlist_track
# SET active = 1;
# EOF

#### 8.Challenge: Adding Sales Tax Capabilities
# sqlite3 chinook.db <<EOF
# ALTER TABLE invoice
# ADD COLUMN tax NUMERIC; 
# ALTER TABLE invoice           
# ADD COLUMN subtotal NUMERIC;
# UPDATE invoice
# SET tax = 0,
#     subtotal = total;
# EOF
