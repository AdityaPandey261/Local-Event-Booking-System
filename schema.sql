-- Drop tables if they already exist (for reset purposes)
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS events;

-- Create events table
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    location TEXT NOT NULL,
    category TEXT,
    total_seats INTEGER NOT NULL,
    available_seats INTEGER NOT NULL
);

-- Create bookings table
CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    user_email TEXT NOT NULL,
    event_id INTEGER NOT NULL,
    num_tickets INTEGER NOT NULL,
    booking_time TEXT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events (id) ON DELETE CASCADE
);
