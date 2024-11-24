from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.department_model import Department
from app.schemas.department_schema import DepartmentCreate, DepartmentResponse

def insert_department(db: Session, department: DepartmentCreate) -> DepartmentResponse:
    """
    Insert a Department record into the database.

    :param db: SQLAlchemy database session.
    :param department: DepartmentInsert DTO to be inserted.
    :return: DepartmentResponse object representing the inserted department.
    """
    try:
        # Map DTO to SQLAlchemy Department object
        department_obj = Department(
            department_name=department.department_name,
            store_id=department.store_id
        )

        # Add and commit the department
        db.add(department_obj)
        db.commit()

        # Refresh the object to get updated values
        db.refresh(department_obj)
        return DepartmentResponse.model_validate(department_obj)
    except SQLAlchemyError as e:
        db.rollback() # Rollback transaction in case of error
        raise RuntimeError(f"Failed to insert department: {str(e)}") from e
    
def get_all_departments(db: Session) -> List[DepartmentResponse]:
    """
    Retrieve all Department records from the database.

    :param db: SQLAlchemy database session.
    :return: List of DepartmentResponse objects.
    """
    departments = db.query(Department).all()
    return [DepartmentResponse.model_validate(department) for department in departments]

def get_department_by_id(db: Session, department_id: int) -> DepartmentResponse:
    """
    Retrieve a single Department record by its ID.

    :param db: SQLAlchemy database session.
    :param department_id: ID of the department to retrieve.
    :return: DepartmentResponse object if found.
    :raises: RuntimeError if the department is not found.
    """
    department = db.query(Department).filter(Department.department_id == department_id).first()
    if not department:
        raise RuntimeError(f"Department with ID {department_id} not found.")
    return DepartmentResponse.model_validate(department)

def update_department(db: Session, department_id: int, updates: DepartmentCreate) -> DepartmentResponse:
    """
    Update a Department record in the database.

    :param db: SQLAlchemy database session.
    :param department_id: ID of the department to update.
    :param updates: DepartmentInsert DTO containing the updated data.
    :return: DepartmentResponse object representing the updated department.
    :raises: RuntimeError if the department is not found.
    """
    department = db.query(Department).filter(Department.department_id == department_id).first()
    if not department:
        raise RuntimeError(f"Department with ID {department_id} not found.")

    # Apply updates
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(department, key, value)
    
    try:
        db.commit()
        db.refresh(department)
        return DepartmentResponse.model_validate(department)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update department: {str(e)}") from e

def delete_department(db: Session, department_id: int) -> None:
    """
    Delete a Department record from the database.

    :param db: SQLAlchemy database session.
    :param department_id: ID of the department to delete.
    :raises: RuntimeError if the department is not found.
    """
    department = db.query(Department).filter(Department.department_id == department_id).first()
    if not department:
        raise RuntimeError(f"Department with ID {department_id} not found.")
    
    try:
        db.delete(department)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete department: {str(e)}") from e