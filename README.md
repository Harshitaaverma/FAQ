# FAQ

This project was done as an assessment for **BHARATFD** company.

## Overview

The application is designed to manage and store Frequently Asked Questions (FAQs) in multiple languages. It includes the following features:

- **Multilingual Support**: The FAQ questions and answers can be translated into multiple languages (e.g., English, Hindi, Bengali).
- **WYSIWYG Editor**: The answers are formatted using the CKEditor, which provides a rich text editing experience.
- **REST API**: A RESTful API has been developed to fetch FAQs based on language selection using the `?lang=` query parameter.
- **Caching**: A caching mechanism has been implemented to speed up the API responses, reducing database queries for frequently requested FAQs.

## Features

- FAQ model with multi-language support.
- Support for multilingual translations via Google Translate API.
- Integration with the **django-ckeditor** library for rich text editing.
- Caching using Redis to optimize performance.
- A REST API that serves FAQs based on a `lang` query parameter.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Cache**: Redis
- **Frontend**: N/A (Backend only)
- **Editor**: CKEditor for WYSIWYG editing
- **Containerization**: Docker

