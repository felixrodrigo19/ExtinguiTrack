# ExtinguiTrack

ExtinguiTrack is a back-end web-based system for efficiently managing fire extinguishers within your organization.
Whether you need to track their locations, inspection dates, or other critical information, ExtinguiTrack provides a
solution to streamline your fire safety management.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Comprehensive Fire Extinguisher Management**: Easily manage all your fire extinguishers' details, including serial
  numbers, manufacturing dates, and last inspection dates.

- **Supplier and Location Management**: Keep track of your suppliers and the locations where extinguishers are placed.

- **Type and Agent Information**: Manage different types of extinguishers and the extinguishing agents they use.

## Getting Started

To get started with ExtinguiTrack, follow these steps:

1. **Clone the Repository**:
   ```shell
   https://github.com/felixrodrigo19/ExtinguiTrack.git

2. **Enter on the project path**:
   ```shell
   cd ExtinguiTrack

3. **Create a .env file and add a SECRET_KEY**
   https://djecrety.ir/

4. **Create a new env with Pipenv and install all project requirements:**
   ```shell
   pipenv shell
   pipenv install

5. **Apply Migrations**:
   ```shell
   python manage.py migrate

6. **Create a Admin User**:
   ```shell
   python manage.py createsuperuser

7. **Run the Dev Server:
   ```shell
   python manage.py runserver 

8. **Access the Application**:
   Open your web browser and go to http://localhost:8000.

## Usage

Data Entry: Add new records and update existing ones as needed.

Efficient Management: Easily keep track of the status and location of your fire extinguishers, helping you ensure safety
compliance.

![home.png](state_of_art%2Fhome.png)
![suppliers.png](state_of_art%2Fsuppliers.png)

## Contributing

We welcome contributions from the open-source community. If you'd like to contribute to ExtinguiTrack, please follow
these guidelines:

1. Fork the repository and create your branch from main.

2. Make your code changes and ensure tests are passing.

3. Open a pull request, providing a detailed description of your changes.

4. We will review your contributions, and once approved, they will be merged.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

