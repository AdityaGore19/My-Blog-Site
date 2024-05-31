# My-Blog-Site

This is a fully functional blog site built using Django. Users can register, create, read, update, and delete blog posts. The site also supports user authentication, profile management, and password reset functionalities. Media files are stored using AWS S3.

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- User profile management with profile pictures
- Password reset via email
- Pagination for blog posts
- Media file storage using AWS S3

## Technologies Used

- Django
- Django Crispy Forms
- Django Storages
- Boto3
- AWS S3
- SQLite (default database)

## Getting Started

### Prerequisites

- Python 3.8+
- Django 5.0.6
- AWS account with S3 bucket set up
- Email account for sending password reset emails

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root directory and add the following:

    ```env
    SECRET_KEY=your_secret_key
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_email_password
    AWS_ACCESS_KEY_ID=your_aws_access_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret_key
    AWS_STORAGE_BUCKET_NAME=your_bucket_name
    ```

5. **Run migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

7. **Start the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Access the site:**

    Open your web browser and go to `http://localhost:8000`.

### AWS S3 Configuration

1. **Set up CORS Configuration in your S3 bucket:**

    ```json
    [
        {
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["GET", "POST", "PUT"],
            "AllowedOrigins": ["*"],
            "ExposeHeaders": []
        }
    ]
    ```

2. **Bucket Policy:**

    Ensure your bucket has the correct policy to allow your Django application to access it.

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::your_bucket_name/*"
            }
        ]
    }
    ```

## Usage

- Register a new user or login with an existing account.
- Create new blog posts, edit or delete your posts.
- View all blog posts on the homepage with pagination.
- Update your profile, including uploading a profile picture.
- Reset your password if you forget it via email.

## Project Structure

