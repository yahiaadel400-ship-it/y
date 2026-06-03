from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, DECIMAL, Date, Text, JSONB, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from config.settings import settings
import enum

# Create Database Engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=settings.DEBUG
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(200))
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)

class AccountType(Base):
    __tablename__ = "account_types"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    debit_increase = Column(Boolean, default=True)

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    name_ar = Column(String(200), nullable=False)
    name_en = Column(String(200))
    account_type_id = Column(Integer, ForeignKey("account_types.id"), nullable=False)
    parent_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)
    balance = Column(DECIMAL(15, 2), default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class JournalEntry(Base):
    __tablename__ = "journal_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    entry_date = Column(Date, nullable=False, index=True)
    entry_number = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    reference_number = Column(String(100))
    reference_type = Column(String(50))
    total_debit = Column(DECIMAL(15, 2), default=0)
    total_credit = Column(DECIMAL(15, 2), default=0)
    is_balanced = Column(Boolean, default=True)
    is_posted = Column(Boolean, default=False, index=True)
    posted_at = Column(DateTime, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class JournalEntryLine(Base):
    __tablename__ = "journal_entry_lines"
    
    id = Column(Integer, primary_key=True, index=True)
    journal_entry_id = Column(Integer, ForeignKey("journal_entries.id"), nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    debit = Column(DECIMAL(15, 2), default=0)
    credit = Column(DECIMAL(15, 2), default=0)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    name_ar = Column(String(200), nullable=False)
    name_en = Column(String(200))
    email = Column(String(120))
    phone = Column(String(20))
    address = Column(Text)
    city = Column(String(100))
    country = Column(String(100))
    tax_number = Column(String(50))
    credit_limit = Column(DECIMAL(15, 2))
    contact_person = Column(String(200))
    payment_terms = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Supplier(Base):
    __tablename__ = "suppliers"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    name_ar = Column(String(200), nullable=False)
    name_en = Column(String(200))
    email = Column(String(120))
    phone = Column(String(20))
    address = Column(Text)
    city = Column(String(100))
    country = Column(String(100))
    tax_number = Column(String(50))
    contact_person = Column(String(200))
    payment_terms = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Invoice(Base):
    __tablename__ = "invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(50), unique=True, nullable=False, index=True)
    invoice_type = Column(String(20), nullable=False)
    invoice_date = Column(Date, nullable=False, index=True)
    due_date = Column(Date)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    subtotal = Column(DECIMAL(15, 2), default=0)
    discount = Column(DECIMAL(15, 2), default=0)
    tax_amount = Column(DECIMAL(15, 2), default=0)
    total = Column(DECIMAL(15, 2), default=0)
    paid_amount = Column(DECIMAL(15, 2), default=0)
    status = Column(String(50), default='draft', index=True)
    description = Column(Text)
    notes = Column(Text)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class InvoiceLine(Base):
    __tablename__ = "invoice_lines"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    item_code = Column(String(100))
    description = Column(Text)
    quantity = Column(DECIMAL(10, 2), default=1)
    unit_price = Column(DECIMAL(15, 2))
    line_total = Column(DECIMAL(15, 2))
    tax_rate = Column(DECIMAL(5, 2), default=0)
    tax_amount = Column(DECIMAL(15, 2), default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    payment_number = Column(String(50), unique=True, nullable=False)
    payment_date = Column(Date, nullable=False, index=True)
    payment_type = Column(String(50))
    amount = Column(DECIMAL(15, 2), nullable=False)
    currency = Column(String(10), default='EGP')
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    reference_number = Column(String(100))
    notes = Column(Text)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    item_code = Column(String(100), unique=True, nullable=False, index=True)
    name_ar = Column(String(200), nullable=False)
    name_en = Column(String(200))
    description = Column(Text)
    unit_of_measure = Column(String(50))
    quantity_on_hand = Column(DECIMAL(10, 2), default=0)
    reorder_level = Column(DECIMAL(10, 2))
    unit_cost = Column(DECIMAL(15, 2))
    selling_price = Column(DECIMAL(15, 2))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"
    
    id = Column(Integer, primary_key=True, index=True)
    movement_date = Column(Date, nullable=False, index=True)
    movement_type = Column(String(50), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity = Column(DECIMAL(10, 2))
    unit_cost = Column(DECIMAL(15, 2))
    total_cost = Column(DECIMAL(15, 2))
    reference_number = Column(String(100))
    notes = Column(Text)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class Budget(Base):
    __tablename__ = "budgets"
    
    id = Column(Integer, primary_key=True, index=True)
    name_ar = Column(String(200), nullable=False)
    name_en = Column(String(200))
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String(100))
    entity_type = Column(String(100))
    entity_id = Column(Integer)
    old_values = Column(JSONB)
    new_values = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()