### 🎓 Online Exam Generator

An AI-powered web application that dynamically generates exam questions based on user input. This tool allows students, teachers, and developers to quickly create customized practice exams for learning or testing purposes.

### Pitch Deck

https://www.canva.com/design/DAGx0gJ_Gd4/f4ABd0WqAXQq__5pC9DaGg/edit

### Contributors
Enock M Kahogo - kahogotech@gmail.com 
Paul Siameto - siametopaul2@gmail.com 
Joseph Kamau - iamjosephkamau@gmail.com 
Mitchell Jerop - mitchelljerop09@gmail.com                
Emmanuel Kichinda - manuelkichy001@gmail.com  
### Deployment Link
http://102.220.23.165/onlineexam

## Key Features

- **AI-Powered Question Generation**: Utilizes Hugging Face models to create diverse question types
- **Role-Based Access**: Separate interfaces for learners and teachers
- **Exam Management**: Create, schedule, and administer online exams
- **Results Analytics**: Detailed performance tracking and analytics
- **Subscription System**: Tiered access to premium features
- **Responsive Design**: Works seamlessly across desktop and mobile devices

## Technology Stack

### Backend
- **Framework**: Django (Python)
- **Database**: MySQL
- **AI Integration**: Hugging Face Transformers
- **Authentication**: Django AllAuth

### Frontend
- **HTML5/CSS3**: Responsive layout with Bootstrap
- **JavaScript**: Interactive elements and data handling
- **Data Visualization**: Chart.js for analytics
- **Data Tables**: Advanced table functionality with DataTables

## Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL 5.7+
- pip (Python package manager)
- Virtualenv (recommended)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd edu-exam-ai
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL database**
   ```sql
   CREATE DATABASE eduexamai;
   CREATE USER 'eduexamai_user'@'localhost' IDENTIFIED BY 'secure_password';
   GRANT ALL PRIVILEGES ON eduexamai.* TO 'eduexamai_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   DATABASE_NAME=eduexamai
   DATABASE_USER=eduexamai_user
   DATABASE_PASSWORD=secure_password
   DATABASE_HOST=localhost
   DATABASE_PORT=3306
   HUGGINGFACE_API_KEY=your-huggingface-api-key
   ```

6. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
eduexamai/
├── accounts/                 # User authentication and management
├── exams/                   # Exam creation and management
├── subscriptions/           # Subscription handling
├── ai_integration/          # Hugging Face AI integration
├── static/                  # Static files (CSS, JS, images)
│   ├── static_assets/       # Theme assets
│   └── assets/              # Custom assets
├── templates/               # HTML templates
└── manage.py               # Django management script
```

## Key Functionalities

### For Teachers
- Create exams with AI-assisted question generation
- Manage question banks
- Schedule and monitor exams
- Review student performance analytics
- Generate detailed reports

### For Learners
- Take scheduled exams
- View exam results and analytics
- Access subscription features
- Track learning progress

### AI Integration
- Context-based question generation
- Multiple question types (MCQ, descriptive, etc.)
- Difficulty level adjustment
- Topic-based question suggestions

## Database Schema

The application uses a MySQL database with the following main tables:
- Users (extended Django User model)
- Exams
- Questions
- Options
- Results
- Subscriptions
- Payments

## API Integration

### Hugging Face API
The platform integrates with Hugging Face's inference API for:
- Text generation for question creation
- Natural language processing for answer evaluation
- Context understanding for relevant question generation

### Payment Gateway
Integration with popular payment providers for subscription management.

## Customization

### Styling
The platform uses a custom color scheme with primary color #02953e and secondary color #E10716. These can be modified in the CSS files.

### Adding New Question Types
1. Extend the Question model in `models.py`
2. Create appropriate templates in `templates/exams/`
3. Update the AI integration to handle the new question type

## Deployment

### Production Checklist
- Set DEBUG=False
- Configure proper database settings
- Set up SSL certificate
- Configure static files serving (Whitenoise or CDN)
- Set up production-ready web server (Gunicorn + Nginx)
- Configure email backend
- Set up monitoring and logging

### Docker Deployment (Optional)
A `Dockerfile` and `docker-compose.yml` are provided for containerized deployment.

## Troubleshooting

### Common Issues
1. **MySQL connection errors**: Verify database credentials in settings.py
2. **Static files not loading**: Run `collectstatic` and check STATIC_ROOT setting
3. **Hugging Face API errors**: Verify API key and internet connectivity
4. **Migration conflicts**: Try resetting migrations or checking model consistency

### Performance Optimization
- Enable database caching
- Use CDN for static assets
- Implement query optimization
- Set up background tasks for AI processing


## License

This project is proprietary software. All rights reserved.

## Contributing

We welcome contributions! Please see our contributing guidelines for more information.

---

*Note: This README provides an overview of the EduExamAI platform. For detailed technical documentation, please refer to the internal documentation wiki.*
