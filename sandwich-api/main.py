from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- Sandwich Endpoints --------
@app.post("/sandwiches/")
def create(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return crud.create_sandwich(db, sandwich)

@app.get("/sandwiches/")
def read(db: Session = Depends(get_db)):
    return crud.get_sandwiches(db)

@app.put("/sandwiches/{id}")
def update(id: int, sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    result = crud.update_sandwich(db, id, sandwich)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@app.delete("/sandwiches/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_sandwich(db, id)

# -------- Resource Endpoints --------
@app.post("/resources/")
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return crud.create_resource(db, resource)

@app.get("/resources/")
def read_resources(db: Session = Depends(get_db)):
    return crud.get_resources(db)

@app.put("/resources/{id}")
def update_resource(id: int, resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return crud.update_resource(db, id, resource)

@app.delete("/resources/{id}")
def delete_resource(id: int, db: Session = Depends(get_db)):
    return crud.delete_resource(db, id)

# -------- Recipe Endpoints --------
@app.post("/recipes/")
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe)

@app.get("/recipes/")
def read_recipes(db: Session = Depends(get_db)):
    return crud.get_recipes(db)

@app.delete("/recipes/{id}")
def delete_recipe(id: int, db: Session = Depends(get_db)):
    return crud.delete_recipe(db, id)

# -------- Order Endpoints --------
@app.post("/orders/")
def create_order(order: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.get("/orders/")
def read_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@app.delete("/orders/{id}")
def delete_order(id: int, db: Session = Depends(get_db)):
    return crud.delete_order(db, id)