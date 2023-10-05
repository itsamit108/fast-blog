# FastBlog

## Introduction

Welcome to FastBlog, your go-to web application for creating and managing blog posts. FastBlog is built with FastAPI, utilizes SQLite as the database, and employs JWT (JSON Web Tokens) and OAuth for authentication.

## Features

- **User Registration:** Create an account with a unique username and password.
- **User Authentication:** Securely log in using JWT and OAuth authentication.
- **Create, Read, Update, Delete (CRUD) Posts:** Write and manage your blog posts.
- **View All Posts:** Browse through all the published blog posts.
- **User Profiles:** Customize your user profile with a profile picture and bio.
- **Commenting:** Engage with other users by leaving comments on blog posts.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/itsamit108/fast-blog
   cd fast-blog
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**

   Create the SQLite database and apply migrations:

   ```bash
   python manage.py migrate
   ```

4. **Run the Application**

   ```bash
   python manage.py runserver
   ```

   The app will be accessible at `http://localhost:8000`.

## Usage

1. **Register a User**

   - Access FastBlog and click on "Register."
   - Fill in the required details and submit the form.

2. **Login**

   - After registration, log in using your credentials.

3. **Create a Post**

   - Once logged in, you can create a new blog post by clicking "Create Post."
   - Fill in the details, including the title and content.

4. **View All Posts**

   - Browse through all the blog posts on the homepage.

5. **User Profile**

   - Customize your profile by clicking on your username.

6. **Comment on Posts**

   - Engage with other users by leaving comments on blog posts.

7. **Logout**

   - Log out when you're done using FastBlog.

## Contribution

If you'd like to contribute to FastBlog, feel free to open issues or submit pull requests. Your help is greatly appreciated!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- [SQLite](https://www.sqlite.org/) for the lightweight database.
- [OAuth](https://oauth.net/) for secure authentication.
- [JWT](https://jwt.io/) for handling authentication tokens.
