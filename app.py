from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

DATABASE = 'database.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Home Page - List of all events
@app.route('/')
def index():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events ORDER BY date').fetchall()
    conn.close()
    return render_template('index.html', events=events)


# Event Detail Page
@app.route('/event/<int:event_id>')
def event_detail(event_id):
    conn = get_db_connection()
    event = conn.execute('SELECT * FROM events WHERE id = ?', (event_id,)).fetchone()
    conn.close()
    if event is None:
        return "Event Not Found", 404
    return render_template('event_detail.html', event=event)


# Booking Form
@app.route('/book/<int:event_id>', methods=['GET', 'POST'])
def book_event(event_id):
    conn = get_db_connection()
    event = conn.execute('SELECT * FROM events WHERE id = ?', (event_id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        num_tickets = int(request.form['num_tickets'])

        if num_tickets > event['available_seats']:
            flash('Not enough seats available!', 'error')
        else:
            booking_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                conn.execute('''
                    INSERT INTO bookings (user_name, user_email, event_id, num_tickets, booking_time)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, email, event_id, num_tickets, booking_time))
                conn.execute('UPDATE events SET available_seats = available_seats - ? WHERE id = ?',
                             (num_tickets, event_id))
                conn.commit()
                flash('Booking successful!', 'success')
            except Exception as e:
                flash(f'Error saving booking: {e}', 'error')
            finally:
                conn.close()
            return redirect(url_for('index'))

    conn.close()
    return render_template('booking_form.html', event=event)


# Admin Login
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple hardcoded login
        if username == 'admin' and password == 'admin123':
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('admin_login.html')


# Admin Dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events ORDER BY date').fetchall()
    conn.close()
    return render_template('admin_dashboard.html', events=events)


# Add Event
@app.route('/admin/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        category = request.form['category']
        total_seats = int(request.form['total_seats'])

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO events (title, description, date, time, location, category, total_seats, available_seats)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, description, date, time, location, category, total_seats, total_seats))
        conn.commit()
        conn.close()
        flash('Event added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('add_event.html')


# Delete Event
@app.route('/admin/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM events WHERE id = ?', (event_id,))
    conn.commit()
    conn.close()
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


# View all bookings
@app.route('/admin/bookings')
def view_bookings():
    conn = get_db_connection()
    bookings = conn.execute('''
        SELECT b.*, e.title AS event_title
        FROM bookings b
        JOIN events e ON b.event_id = e.id
        ORDER BY booking_time DESC
    ''').fetchall()
    conn.close()
    return render_template('view_bookings.html', bookings=bookings)


# Run App
if __name__ == '__main__':
    app.run(debug=True)
