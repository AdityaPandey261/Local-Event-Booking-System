# 📍 Local Event Finder & Ticket Booking System

A full-stack web application that allows users to find local events and book tickets online. Admins can schedule new events, and users can register, browse events, and book available seats instantly.

---

## 🎯 Features

### 👤 User Side:
- 📝 User Registration and Login
- 📅 Browse Events by Date/Category/Location
- 🎟 Book Tickets for Events
- 📄 View Booking History
- 🖼 Event Details Page

### 🛠 Admin Side:
- ➕ Add/Edit/Delete Events
- 📊 View Bookings
- 📂 Manage Event Listings

---

## 🧱 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite3
- **Templating**: Jinja2

---

## 📁 Project Structure

Local-event-booking/
├── app.py
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── events.html
│ ├── book_ticket.html
│ ├── admin_dashboard.html
│ └── add_event.html
├── database.db
└── README.md


---

## ⚙️ How to Run the Project

1. **Clone the repository or extract ZIP**  
   ```bash
   cd Local-event-booking
(Optional) Create virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies


pip install Flask
Run the application

python app.py
Open browser and go to: http://127.0.0.1:5000/
