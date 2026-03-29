from pydantic import BaseModel

# -------- Sandwich --------
class SandwichBase(BaseModel):
    name: str
    price: int

class SandwichCreate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int
    class Config:
        orm_mode = True

# -------- Resource --------
class ResourceBase(BaseModel):
    name: str
    quantity: int

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    class Config:
        orm_mode = True

# -------- Recipe --------
class RecipeBase(BaseModel):
    sandwich_id: int
    resource_id: int
    amount: int

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    class Config:
        orm_mode = True

# -------- Order Details --------
class OrderDetailBase(BaseModel):
    sandwich_id: int
    quantity: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetail(OrderDetailBase):
    id: int
    class Config:
        orm_mode = True