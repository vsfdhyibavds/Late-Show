# LateShow

## Description
LateShow is a Python-based application that manages data related to episodes, guests, and appearances. It uses a database with migrations and CSV data files for seeding or data import.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run database migrations:
   ```
   flask db upgrade
   ```
2. Seed the database with initial data:
   ```
   python seed.py
   ```
3. Run the application:
   ```
   python app.py
   ```

## Database
The project uses a database with migrations managed by Alembic. CSV files in the project are used for seeding data related to episodes, guests, and appearances.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.
