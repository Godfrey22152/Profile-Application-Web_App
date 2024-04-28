# Profile App Documentation

## Introduction

The Profile App is a web application built using Flask, a Python web framework, and MongoDB, a NoSQL database. It provides functionalities for user registration, login, profile display, update, and submission of a single job application.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Dependencies](#dependencies)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Routes](#routes)
    - [1. Landing Page](#1-landing-page)
    - [2. Login](#2-login)
    - [3. Logout](#3-logout)
    - [4. Registration](#4-registration)
    - [5. Profile Index](#5-profile-index)
    - [6. Profile Display](#6-profile-display)
    - [7. Profile Update](#7-profile-update)
    - [8. Job Application](#8-job-application)
    - [9. Application Details](#9-application-details)
7. [Running the Application](#running-the-application)

## Getting Started

To get started with the Profile App, follow the instructions in the [Installation](#installation) section below.

## Dependencies

The following dependencies are required to run the application:

- Flask
- pymongo
- bson
- re
- os
- random

These dependencies can be installed using `pip`:

```bash
pip install Flask pymongo
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Godfrey22152/Profile-Application-Web_App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ProfileApp
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open a web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the Profile App.

## File Structure

- **app.py**: Main application file containing the Flask application and routes.
- **templates**: Directory containing HTML templates for different pages.
- **static**: Directory containing static files such as images.

## Routes

### 1. Landing Page

- **URL**: `/` or `/landing`
- **Description**: Displays a landing page with shuffled images.

### 2. Login

- **URL**: `/login`
- **Methods**: GET, POST
- **Description**: Allows users to log in. If successful, redirects to the index page.

### 3. Logout

- **URL**: `/logout`
- **Description**: Logs out the user and redirects to the login page.

### 4. Registration

- **URL**: `/register`
- **Methods**: GET, POST
- **Description**: Allows users to register. Validates input data and creates an account if valid.

### 5. Profile Index

- **URL**: `/index`
- **Description**: Displays the user's profile index. Requires login.

### 6. Profile Display

- **URL**: `/display`
- **Description**: Displays detailed information about the user's profile. Requires login.

### 7. Profile Update

- **URL**: `/update`
- **Methods**: GET, POST
- **Description**: Allows users to update their profile information. Validates input data and updates the database.

### 8. Job Application

- **URL**: `/application`
- **Methods**: GET, POST
- **Description**: Allows users to submit a job application. Validates input data and stores the application in the database.

### 9. Application Details

- **URL**: `/application_details`
- **Description**: Displays details of the user's submitted job application. Requires login.

## Running the Application

To run the application, execute the following command in the terminal:

```bash
python app.py
```

The application will be accessible at [http://localhost:5000/](http://localhost:5000/).
