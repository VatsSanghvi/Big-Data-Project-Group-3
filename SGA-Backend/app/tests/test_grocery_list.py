from app.database import TestingSessionLocal
from app.schemas.grocery_list_schema import GroceryItemCreate, GroceryListCreate, GroceryListUpdate
from app.crud import grocery_list_crud
from app.models import user_model, grocery_list_model, store_model, product_model, department_model, category_model,budget_model
from app.database import engine

# Setup a test database session
def get_test_db():
    user_model.Base.metadata.create_all(bind=engine)
    category_model.Base.metadata.create_all(bind=engine)
    product_model.Base.metadata.create_all(bind=engine)
    department_model.Base.metadata.create_all(bind=engine)
    store_model.Base.metadata.create_all(bind=engine)
    grocery_list_model.Base.metadata.create_all(bind=engine)
    budget_model.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# def test_insert_grocery_list():
#     # Initialize the test database session
#     db_generator = get_test_db()
#     db = next(db_generator)

#     # Mock data
#     new_list = GroceryListCreate(
#         name="Grocery_1",
#         user_id=1
#     )

#     # Call the function
#     inserted_list = grocery_list_crud.insert_grocery_list(db=db, grocery_list=new_list)

#     # Validate results
#     assert inserted_list.name == new_list.name


def test_update_grocery_list():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    updated_list_data = GroceryListUpdate(
        grocery_list_id=3,
        user_id=1,          
        name="Grocery"
    )

    # Call the function to update the grocery list name
    updated_list = grocery_list_crud.update_grocery_list(
        db=db,
        list_id=updated_list_data.grocery_list_id,
        updates=updated_list_data
    )

    # Validate results
    assert updated_list.name == updated_list_data.name
    assert updated_list.id == updated_list_data.grocery_list_id
    assert updated_list.user_id == updated_list_data.user_id

# def test_get_grocery_list():
#     # Initialize the test database session
#     db_generator = get_test_db()
#     db = next(db_generator)

#     # Mock data
#     new_list = GroceryListCreate(
#         name="Test List",
#         user_id=2
#     )

#     # Insert the grocery list
#     inserted_list = grocery_list_crud.insert_grocery_list(db=db, grocery_list=new_list)

#     # Call the function
#     grocery_list = grocery_list_crud.get_grocery_list(db=db, list_id=inserted_list.id, user_id=new_list.user_id)

#     # Validate results
#     assert len(grocery_list) > 0

# def test_delete_grocery_list():
#     # Initialize the test database session
#     db_generator = get_test_db()
#     db = next(db_generator)

#     # Mock data
#     new_list = GroceryListCreate(
#         name="Test List",
#         user_id=2
#     )

#     # Insert the grocery list
#     inserted_list = grocery_list_crud.insert_grocery_list(db=db, grocery_list=new_list)

#     # Validate results
#     grocery_list_crud.delete_grocery_list(db=db, list_id=inserted_list.id)

# # Testing the function
# def test_insert_item_to_grocery_list():
#     # Initialize the test database session
#     db_generator = get_test_db()
#     db = next(db_generator)

#     # Get the grocery list
#     new_list = GroceryListCreate(
#         name="Test List",
#         user_id=2
#     )

#     # Insert the grocery list
#     inserted_list = grocery_list_crud.insert_grocery_list(db=db, grocery_list=new_list)

#     # Mock data
#     new_item = GroceryItemCreate(
#         name="Test Item",
#         category="Test Category",
#         grocery_list_id=inserted_list.id
#     )

#     # Insert the grocery item
#     inserted_item = grocery_list_crud.insert_item_to_grocery_list(db=db, item=new_item)

#     # Validate results
#     assert inserted_item.name == new_item.name

# def test_get_grocery_item_by_id():
#     # Initialize the test database session
#     db_generator = get_test_db()
#     db = next(db_generator)

#     # Mock data
#     new_list = GroceryListCreate(
#         name="Test List",
#         user_id=2
#     )

#     # Insert the grocery list
#     inserted_list = grocery_list_crud.insert_grocery_list(db=db, grocery_list=new_list)

#     # Mock data
#     new_item = GroceryItemCreate(
#         name="Test Item",
#         category="Test Category",
#         grocery_list_id=inserted_list.id
#     )

#     # Insert the grocery item
#     inserted_item = grocery_list_crud.insert_item_to_grocery_list(db=db, item=new_item)

#     # Call the function
#     item = grocery_list_crud.get_grocery_item_by_id(db, item_id=inserted_item.id)

#     # Validate results
#     assert item.id == inserted_item.id

# def test_update_grocery_list_item():
#     # Initialize the test database session
#     db_generator = get_test_db()
#     db = next(db_generator)

#     # Mock data
#     new_list = GroceryListCreate(
#         name="Test List",
#         user_id=2
#     )

#     # Insert the grocery list
#     inserted_list = grocery_list_crud.insert_grocery_list(db=db, grocery_list=new_list)

#     # Mock data
#     new_item = GroceryItemCreate(
#         name="Test Item",
#         category="Test Category",
#         grocery_list_id=inserted_list.id
#     )

#     # Insert the grocery item
#     inserted_item = grocery_list_crud.insert_item_to_grocery_list(db=db, item=new_item)

#     # Mock updated data
#     updated_item = GroceryItemCreate(
#         name="Updated Item",
#         category="Updated Category",
#         grocery_list_id = inserted_item.grocery_list_id
#     )

#     # Update the grocery item
#     updated_item = grocery_list_crud.update_grocery_list_item(db=db, item_id=inserted_item.id, updates=updated_item)

#     # Validate results
#     assert updated_item.id == inserted_item.id

# def test_delete_grocery_list_item():
#     # Initialize the test database session
#     db_generator = get_test_db()
#     db = next(db_generator)

#     # Mock data
#     new_list = GroceryListCreate(
#         name="Test List",
#         user_id=2
#     )

#     # Insert the grocery list
#     inserted_list = grocery_list_crud.insert_grocery_list(db=db, grocery_list=new_list)

#     # Mock data
#     new_item = GroceryItemCreate(
#         name="Test Item",
#         category="Test Category",
#         grocery_list_id=inserted_list.id
#     )

#     # Insert the grocery item
#     inserted_item = grocery_list_crud.insert_item_to_grocery_list(db=db, item=new_item)

#     # Delete the grocery item
#     grocery_list_crud.delete_grocery_list_item(db=db, item_id=inserted_item.id)

# # Run the tests
# test_insert_grocery_list()
# test_get_grocery_list()

# test_insert_item_to_grocery_list()
# test_get_grocery_item_by_id()
# test_update_grocery_list_item()

# test_delete_grocery_list()
# test_delete_grocery_list_item()


