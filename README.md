# LateShow API

This is a Flask API for the LateShow project. It manages Episodes, Guests, and Appearances with relationships and validations.

## Setup

1. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run database migrations:

```bash
flask db init
flask db migrate
flask db upgrade
```

4. Seed the database:

Make sure you have the CSV files (`episodes.csv`, `guests.csv`, `appearances.csv`) in the project root.

```bash
python seed.py
```

5. Run the app:

```bash
python app.py
```

## API Endpoints

- `GET /episodes` - List all episodes
- `GET /episodes/:id` - Get episode details with appearances and guests
- `GET /guests` - List all guests
- `POST /appearances` - Create a new appearance

## Testing

Import the provided Postman collection `challenge-4-lateshow.postman_collection.json` into Postman to test the API endpoints.

## Notes

