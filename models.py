# ==============================================================
# DATABASE TABLES (SCHEMA DEFINITION)
# ==============================================================
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    subscription_plan = Column(String, default="UNLIMITED_ENTERPRISE")
    created_at = Column(DateTime, default=datetime.utcnow)

    products = relationship("Product", back_populates="vendor")
    orders = relationship("Order", back_populates="vendor")


class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    vendor_id = Column(String, ForeignKey("vendors.id"), nullable=False)
    title = Column(String, nullable=False)
    category = Column(String, index=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)

    vendor = relationship("Vendor", back_populates="products")


class Order(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    vendor_id = Column(String, ForeignKey("vendors.id"), nullable=False)
    customer_phone = Column(String, index=True, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, default="PENDING")
    fraud_risk_score = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    vendor = relationship("Vendor", back_populates="orders")