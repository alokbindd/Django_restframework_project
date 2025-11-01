# Django REST Framework Learning Project

A comprehensive Django REST Framework (DRF) project covering API development concepts from basics to advanced topics including serializers, views, viewsets, filtering, pagination, and nested relationships.

## 📚 Project Overview

This project demonstrates various Django REST Framework concepts and patterns learned through hands-on implementation. It includes multiple models (Student, Employee, Blog, Comment) and showcases different approaches to building RESTful APIs.

## 🛠️ Technologies Used

- **Python** 3.x
- **Django** 5.2.7
- **Django REST Framework** 3.16.1
- **django-filter** (for advanced filtering)
- **SQLite** (database)

## 📦 Installation

### Prerequisites

- Python 3.x installed on your system
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository** (or navigate to the project directory)
   ```bash
   cd drf-project
   ```

2. **Create and activate virtual environment**
   ```bash
   # On Windows
   python -m venv env
   .\env\Scripts\activate

   # On macOS/Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework django-filter
   ```

4. **Configure Django settings**
   
   Add `rest_framework` to `INSTALLED_APPS` in `django_rest_main/settings.py`:
   ```python
   INSTALLED_APPS = [
       # ... other apps
       'rest_framework',
       'django_filters',
       'students',
       'employees',
       'Blogs',
       'api',
   ]
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
drf-project/
├── api/                    # Main API app
│   ├── serializers.py     # Serializers for all models
│   ├── views.py           # API views (Function-based, Class-based, Viewsets)
│   ├── urls.py            # URL routing
│   └── paginations.py     # Custom pagination classes
├── students/              # Student model app
│   └── models.py         # Student model
├── employees/             # Employee model app
│   ├── models.py         # Employee model
│   └── filters.py        # Custom filtering for employees
├── Blogs/                 # Blog and Comment models app
│   ├── models.py         # Blog and Comment models (with foreign key)
│   └── serializers.py    # Nested serializers
├── django_rest_main/      # Main Django project settings
│   ├── settings.py       # Django configuration
│   └── urls.py           # Main URL configuration
└── manage.py             # Django management script
```

## 📖 Learning Topics Covered

### 1. Introduction & Setup
- **What is an API?** - Understanding Application Programming Interfaces
- **What is REST API?** - RESTful architecture principles
- **Software Installation** - Setting up development environment
- **Django Installation** - Project initialization
- **Django Rest Framework Installation** - Installing and configuring DRF

### 2. Basic API Development
- **Web Application Endpoint** - Creating simple endpoints
- **Simple API Endpoint** - First API endpoint implementation
- **Create Model** - Django model creation and database setup
- **Manual Serialization** - Serializing data without serializers

### 3. Serializers
- **Serializers Introduction** - Understanding DRF serializers
- **ModelSerializer** - Using ModelSerializer for automatic serialization
- **Serializer Validation** - Data validation and error handling

### 4. Function-Based Views (FBV)
- **GET Method** - Retrieving all objects using function-based views
- **POST Method** - Creating new objects
- **Primary Key-Based Operations** - Getting single object by ID
- **PUT Method** - Updating existing objects
- **DELETE Method** - Deleting objects

**Example Endpoints:**
- `GET /api/v1/students/` - List all students
- `POST /api/v1/students/` - Create a new student
- `GET /api/v1/students/<id>/` - Get student by ID
- `PUT /api/v1/students/<id>/` - Update student
- `DELETE /api/v1/students/<id>/` - Delete student

### 5. Class-Based Views (CBV)
- **Class-Based Views Introduction** - Advantages of CBV over FBV
- **Employee Model** - Creating Employee model
- **Employee Serializer** - Serializer for Employee model
- **GET All Employees** - ListView implementation
- **Creating Employee** - CreateView implementation
- **Getting Single Object** - DetailView implementation
- **Update And Delete Employee** - UpdateView and DeleteView

### 6. Mixins
- **Mixins Overview** - Understanding reusable mixin classes
- **ListModelMixin** - Listing objects
- **CreateModelMixin** - Creating objects
- **RetrieveModelMixin** - Retrieving single object
- **UpdateModelMixin** - Updating objects
- **DestroyModelMixin** - Deleting objects

### 7. Generic Views
- **Generics Overview** - Pre-built generic view classes
- **ListCreateAPIView** - Combined list and create operations
- **RetrieveUpdateDestroyAPIView** - Combined retrieve, update, and delete operations

### 8. ViewSets
- **Viewsets Introduction** - Understanding ViewSets and their benefits
- **List And Create Data** - Implementing list and create operations
- **Retrieving Single Object** - Implementing retrieve operation
- **ModelViewSet** - Complete CRUD operations in one class
- **Router Configuration** - Using DefaultRouter for automatic URL routing

**Example:**
```python
# ViewSet automatically creates all CRUD endpoints
router.register('employees', views.EmployeesViewset)
# Creates:
# GET /api/v1/employees/ - List
# POST /api/v1/employees/ - Create
# GET /api/v1/employees/<id>/ - Retrieve
# PUT /api/v1/employees/<id>/ - Update
# DELETE /api/v1/employees/<id>/ - Delete
```

### 9. Nested Serializers
- **Nested Serializers Introduction** - Handling relationships between models
- **Blog And Comment Model** - One-to-many relationship setup
- **Creating Serializers** - Parent and child serializers
- **Nested Serializers Implementation** - Embedding related objects in responses
- **Primary Key-Based Operations On Blog Comment** - CRUD operations on related models

**Example:**
```python
class BlogSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
```

### 10. Pagination
- **Pagination Overview** - Breaking large datasets into pages
- **Global Pagination** - Setting pagination at project level
- **Custom Pagination** - Creating custom pagination classes

**Custom Pagination Example:**
```python
class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    page_query_param = 'page'
```

### 11. Filtering
- **Filtering Overview** - Filtering querysets
- **Custom Filter By Designation** - Filtering employees by designation
- **Custom Filter By Name And ID** - Multiple filter criteria
- **Advanced Filtering** - Complex filtering with django-filter
- **Search Filter** - Full-text search across multiple fields
- **Ordering Filter** - Sorting results by fields

**Filter Examples:**
```python
# Custom filter
filterset_class = EmployeeFilter

# Search filter
search_fields = ['blog_title', 'blog_body']

# Ordering filter
ordering_fields = ['id']
```

## 🗂️ Models

### Student Model
```python
- student_id: CharField
- Name: CharField
- Branch: CharField
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)
```

### Employee Model
```python
- emp_id: CharField
- emp_name: CharField
- Designation: CharField
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)
```

### Blog Model
```python
- blog_title: CharField
- blog_body: TextField
```

### Comment Model
```python
- blog: ForeignKey (Blog)
- comment: TextField
```

## 🔗 API Endpoints

### Students (Function-Based Views)
- `GET /api/v1/students/` - List all students
- `POST /api/v1/students/` - Create student
- `GET /api/v1/students/<id>/` - Get student by ID
- `PUT /api/v1/students/<id>/` - Update student
- `DELETE /api/v1/students/<id>/` - Delete student

### Employees (ViewSet)
- `GET /api/v1/employees/` - List all employees (with pagination & filtering)
- `POST /api/v1/employees/` - Create employee
- `GET /api/v1/employees/<id>/` - Get employee by ID
- `PUT /api/v1/employees/<id>/` - Update employee
- `PATCH /api/v1/employees/<id>/` - Partial update
- `DELETE /api/v1/employees/<id>/` - Delete employee

**Filter Parameters:**
- `?Designation=<value>` - Filter by designation
- `?emp_name=<value>` - Filter by name (contains)
- `?id_min=<value>&id_max=<value>` - Filter by ID range

### Blogs (Generic Views)
- `GET /api/v1/blogs/` - List all blogs (with search & ordering)
- `POST /api/v1/blogs/` - Create blog
- `GET /api/v1/blogs/<id>/` - Get blog by ID (with nested comments)
- `PUT /api/v1/blogs/<id>/` - Update blog
- `DELETE /api/v1/blogs/<id>/` - Delete blog

**Search Parameters:**
- `?search=<query>` - Search in blog_title and blog_body
- `?ordering=<field>` - Order by field (e.g., `?ordering=id`)

### Comments (Generic Views)
- `GET /api/v1/comments/` - List all comments
- `POST /api/v1/comments/` - Create comment
- `GET /api/v1/comments/<id>/` - Get comment by ID
- `PUT /api/v1/comments/<id>/` - Update comment
- `DELETE /api/v1/comments/<id>/` - Delete comment

## 🧪 Testing the API

### Using Browser
Navigate to `http://127.0.0.1:8000/api/v1/students/` in your browser to see the API response.

### Using curl
```bash
# Get all students
curl http://127.0.0.1:8000/api/v1/students/

# Create a student
curl -X POST http://127.0.0.1:8000/api/v1/students/ \
  -H "Content-Type: application/json" \
  -d '{"student_id": "S001", "Name": "John Doe", "Branch": "CS"}'

# Get employee with filters
curl "http://127.0.0.1:8000/api/v1/employees/?Designation=Developer&page=1"
```

### Using Django REST Framework Browsable API
DRF provides a browsable API interface. Visit any endpoint in your browser to see an interactive API explorer.

## 📝 Key Concepts Demonstrated

1. **Serializers**: Convert complex data types to/from JSON
2. **Function-Based Views**: Simple view functions with decorators
3. **Class-Based Views**: Reusable view classes
4. **Mixins**: Reusable functionality for views
5. **Generic Views**: Pre-built views for common patterns
6. **ViewSets**: Actions-based views that work with routers
7. **ModelViewSet**: Complete CRUD operations
8. **Nested Serializers**: Handle model relationships
9. **Pagination**: Manage large datasets
10. **Filtering**: Filter querysets by various criteria
11. **Search**: Full-text search across fields
12. **Ordering**: Sort results dynamically

## 🎯 Best Practices Implemented

- ✅ Model serializers for automatic field handling
- ✅ Proper HTTP status codes
- ✅ Error handling and validation
- ✅ RESTful URL patterns
- ✅ Separation of concerns (models, serializers, views)
- ✅ Reusable pagination classes
- ✅ Custom filtering for complex queries
- ✅ Nested serializers for relationships

## 📚 Additional Resources

- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [REST API Design Best Practices](https://restfulapi.net/)

## 🚀 Next Steps

Consider exploring:
- Authentication and Permissions
- Token Authentication
- JWT Authentication
- API Versioning
- Throttling
- API Documentation with drf-yasg or drf-spectacular
- Testing with Django TestCase
- Caching strategies
- API rate limiting

## 📄 License

This project is for educational purposes.

## 👤 Author

Created as a learning project to master Django REST Framework concepts.

---

**Happy Coding! 🎉**

