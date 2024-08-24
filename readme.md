

---

# Pokémon API Backend

Welcome to the Pokémon API Backend! This project provides a backend API for managing Pokémon data, including types, shapes, colors, and various attributes. It is designed to be used with a frontend application or other client applications that need to interact with Pokémon data.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- **CRUD Operations:** Create, read, update, and delete Pokémon and related data.
- **Customizable Pokémon Data:** Support for Pokémon types, shapes, colors, and growth rates.
- **Superuser Management:** Ability to create and manage a superuser with default parameters.
- **Automated Data Initialization:** Command to initialize default Pokémon-related data.

## Technologies

- **Django:** A high-level Python web framework.
- **Django REST Framework:** A powerful toolkit for building Web APIs.
- **PostgreSQL/MySQL:** Relational database management system (adjustable based on configuration).
- **Python 3.8+**

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/BhargavPabbaraju/PokemonAPIBackend.git
   cd PokemonAPIBackend
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database:**

   Update the `DATABASES` settings in `settings.py` to match your database configuration.

5. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional):**

   Run the command below to create a superuser with default parameters:

   ```bash
   python manage.py create_superuser --username admin --email admin@admin.com
   ```

7. **Initialize Default Data:**

   ```bash
   python manage.py initialize_data
   ```

8. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser to access the API.

## Usage

- **Access the API:** Once the server is running, you can access the API at `http://127.0.0.1:8000/api/`.
- **Explore Endpoints:** Use tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/) to interact with the API endpoints.

## API Endpoints

- **Pokémon Endpoints:**
  - `GET /api/pokemon/` - List all Pokémon
  - `POST /api/pokemon/` - Create a new Pokémon
  - `GET /api/pokemon/{id}/` - Retrieve a specific Pokémon
  - `PUT /api/pokemon/{id}/` - Update a specific Pokémon
  - `DELETE /api/pokemon/{id}/` - Delete a specific Pokémon

- **Type Endpoints:**
  - `GET /api/type/` - List all Pokémon types
  - `POST /api/type/` - Create a new Pokémon type
  - `GET /api/type/{id}/` - Retrieve a specific Pokémon type
  - `PUT /api/type/{id}/` - Update a specific Pokémon type
  - `DELETE /api/type/{id}/` - Delete a specific Pokémon type

- **Shape Endpoints:**
  - `GET /api/shape/` - List all Pokémon shapes
  - `POST /api/shape/` - Create a new Pokémon shape
  - `GET /api/shape/{id}/` - Retrieve a specific Pokémon shape
  - `PUT /api/shape/{id}/` - Update a specific Pokémon shape
  - `DELETE /api/shape/{id}/` - Delete a specific Pokémon shape

- **Color Endpoints:**
  - `GET /api/color/` - List all Pokémon colors
  - `POST /api/color/` - Create a new Pokémon color
  - `GET /api/color/{id}/` - Retrieve a specific Pokémon color
  - `PUT /api/color/{id}/` - Update a specific Pokémon color
  - `DELETE /api/color/{id}/` - Delete a specific Pokémon color

- **Growth Rate Endpoints:**
  - `GET /api/growth-rate/` - List all growth rates
  - `POST /api/growth-rate/` - Create a new growth rate
  - `GET /api/growth-rate/{id}/` - Retrieve a specific growth rate
  - `PUT /api/growth-rate/{id}/` - Update a specific growth rate
  - `DELETE /api/growth-rate/{id}/` - Delete a specific growth rate

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
