from sqlalchemy.orm import Session
import models

# -------- Sandwich CRUD --------
def create_sandwich(db: Session, sandwich):
    db_sandwich = models.Sandwich(**sandwich.dict())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def get_sandwiches(db: Session):
    return db.query(models.Sandwich).all()

def update_sandwich(db: Session, sandwich_id, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich:
        for key, value in sandwich.dict().items():
            setattr(db_sandwich, key, value)
        db.commit()
        return db_sandwich
    return None

def delete_sandwich(db: Session, sandwich_id):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db.delete(db_sandwich)
        db.commit()
    return db_sandwich

# -------- Resource CRUD --------
def create_resource(db, resource):
    obj = models.Resource(**resource.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_resources(db):
    return db.query(models.Resource).all()

def update_resource(db, id, resource):
    obj = db.query(models.Resource).filter(models.Resource.id == id).first()
    if obj:
        for k, v in resource.dict().items():
            setattr(obj, k, v)
        db.commit()
    return obj

def delete_resource(db, id):
    obj = db.query(models.Resource).filter(models.Resource.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# -------- Recipe CRUD --------
def create_recipe(db, recipe):
    obj = models.Recipe(**recipe.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_recipes(db):
    return db.query(models.Recipe).all()

def delete_recipe(db, id):
    obj = db.query(models.Recipe).filter(models.Recipe.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# -------- Order CRUD --------
def create_order(db, order):
    obj = models.OrderDetail(**order.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_orders(db):
    return db.query(models.OrderDetail).all()

def delete_order(db, id):
    obj = db.query(models.OrderDetail).filter(models.OrderDetail.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj