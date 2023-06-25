# Project Name: passCBAP

## Description
passCBAP is a web application designed to help users prepare for the CBAP (Certified Business Analysis Professional) exams. It provides a mock exam environment where users can practice and test their knowledge. The application includes features such as login and signup functionality, a forget password feature, and a functional contact form integrated with Mailtrap. Users have the option to take the default exam mode, which consists of 120 questions to be answered within 210 minutes. Alternatively, they can customize their own exam mode with a minimum requirement of 30 questions to be completed within 5 minutes. The user's exam history is displayed on the dashboard, allowing them to review and analyze their past exam performances.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)
- [Live Demo](#live-demo)

## Installation
To install and run the passCBAP project locally on your machine, follow these steps:

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/your-username/passCBAP.git
   ```

2. Navigate to the project directory:
   ```
   cd passCBAP
   ```

3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Configure your database settings in the `settings.py` file, located in the `passCBAP` directory.
   - Apply database migrations:
     ```
     python manage.py migrate
     ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the application by visiting `http://localhost:8000` in your web browser.

## Usage
1. Register a new account or login if you already have one.
2. Use the forget password feature if you need to reset your password.
3. Navigate to the exam section to start practicing for CBAP exams.
4. Choose the default exam mode (120 questions in 210 minutes) or customize your own mode.
5. Submit your answers within the allotted time and receive instant feedback on your performance.
6. Access your exam history on the dashboard to review and analyze your past exam results.
7. Contact the support team using the contact form for any inquiries or issues.

## Features
- User authentication (signup, login, forget password)
- Customizable exam modes (number of questions and time limit)
- Exam history and performance tracking
- Contact form with integration to Mailtrap

## Technologies
- HTML
- CSS
- SCSS
- Bootstrap
- jQuery
- Django

## Contributing
Contributions to the passCBAP project are welcome! If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request detailing your changes.

## License
The passCBAP project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Live Demo
A live demo of passCBAP is available at [passCBAP Live Demo](https://web-production-be78.up.railway.app/). The project has been deployed using Railway. Feel free to explore the application and test its features.
