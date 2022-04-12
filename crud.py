from sqlalchemy.orm.session import Session
from models import Product
from sqlalchemy.orm import Session


def create_product(db: Session, name):
    new_product = Product(
        name=name,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product(db: Session):
    return db.query(Product).all()