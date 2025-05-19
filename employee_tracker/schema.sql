DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE activities (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    activity TEXT,
    type TEXT,
    duration INTEGER,
    timestamp TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);