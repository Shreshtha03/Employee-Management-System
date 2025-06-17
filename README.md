# Employee Management System

A Django-based web application for managing employee and department records. Administrators can create, update, view, and delete data through the Django admin panel. The `Department` model features a dropdown for selecting employees, simplifying department assignments.

## Features

- **Employee Management**:
  - Fields: First Name, Last Name, Email (unique, validated), Contact (10-digit phone number), Date of Joining.
  - Admin panel: List view, filter by date of joining, search by name/email, sort by date.
- **Department Management**:
  - Fields: Employee (dropdown with employee names), Department Name.
  - Admin panel: List view, filter by department name, search by employee name/department name, sort by employee.
- **Validations**:
  - Email format validation.
  - 10-digit phone number validation.
- **User-Friendly Admin Interface**:
  - Built-in Django admin panel for data management.

## Technologies Used

- **Framework**: Django 5.2.2
- **Language**: Python 3.13
- **Database**: SQLite
- **Validators**: Django’s `EmailValidator` and `RegexValidator`

## Prerequisites

- Python 3.13+
- pip
- Git
- Virtualenv (recommended)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shreshtha03/employee-management.git
   cd employee-management
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Server**:
   ```bash
   python manage.py runserver
   ```
   Access the admin panel at `http://localhost:8000/admin/`.

## Project Structure

- **myapp/models.py**: Defines `Employee` and `Department` models.
- **myapp/admin.py**: Configures admin panel for models.
- **employee_management/settings.py**: Project settings.
- **db.sqlite3**: SQLite database.

## Usage

1. **Access Admin Panel**:
   - Go to `http://localhost:8000/admin/` and log in with superuser credentials.

2. **Manage Employees**:
   - Add/edit employee records with validated fields.
   - Filter by date of joining, search by name/email.

3. **Manage Departments**:
   - Add/edit departments, selecting employees from the dropdown.
   - Add employees first to populate the dropdown.
   - Filter by department name, search by employee/department.

## Troubleshooting

- **Error: `no such table: myapp_employee`**:
  - Run `python manage.py makemigrations` and `python manage.py migrate`.
  - If persistent, delete `db.sqlite3` and `myapp/migrations/*` (except `__init__.py`), then rerun migrations.

- **Empty Dropdown**:
  - Add `Employee` records before adding departments.

- **Forgot Password**:
  - Reset with:
    ```bash
    python manage.py changepassword <username>
    ```

## Contributing

1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push: `git push origin feature/your-feature`.
5. Open a pull request.


