# Rate My Professor

Rate My Professor is a Django-based web application designed to help students evaluate and share feedback on their professors. This project incorporates modern features like Google OAuth login, profanity checking, and session management, making it user-friendly and highly functional.

## Features

- **Google OAuth Integration**: Secure and seamless login using Google accounts.
- **Rate Professors**: Submit ratings and reviews for professors.
- **Profanity Checker**: Automatically filters inappropriate language in reviews.
- **Session Management**: Keeps track of user sessions for better usability.
- **Dynamic UI**: A responsive and interactive interface for users.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (development phase)
- **Authentication**: Google OAuth2

## Installation

Follow these steps to get a local instance of the project up and running:

### Prerequisites

- Python 3.8+
- Pipenv (for dependency management)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RateMyProfessor.git
   cd RateMyProfessor
   ```

2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Open the application in your browser at `http://127.0.0.1:8000`.

## Usage

1. Sign in using your Google account.
2. Search for a professor by name or department.
3. Submit your ratings and reviews.
4. Browse reviews submitted by other users.

## Project Structure

- `RateMyProfessor/` - Core Django project settings and configurations.
- `main/` - App directory containing models, views, templates, and static files.
- `db.sqlite3` - SQLite database file.
- `Pipfile` & `Pipfile.lock` - Dependency definitions.
- `manage.py` - Command-line utility for managing the Django project.

## Screenshots

*(Add screenshots of your application interface here)*

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Django Documentation**: For extensive guidance.
- **Google Developers**: For the OAuth2 authentication integration.
- **Community**: For testing and feedback.
