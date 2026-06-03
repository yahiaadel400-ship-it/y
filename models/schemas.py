from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime, date
from decimal import Decimal
from enum import Enum

# =============================================
# Enums
# =============================================

class InvoiceType(str, Enum):
    SALES = "sales"
    PURCHASE = "purchase"

class InvoiceStatus(str, Enum):
    DRAFT = "draft"
    POSTED = "posted"
    PAID = "paid"
    PARTIAL = "partial"
    CANCELLED = "cancelled"

class PaymentType(str, Enum):
    CASH = "cash"
    CHECK = "check"
    TRANSFER = "transfer"
    CARD = "card"

class MovementType(str, Enum):
    PURCHASE = "purchase"
    SALE = "sale"
    ADJUSTMENT = "adjustment"
    TRANSFER = "transfer"

class AccountType(str, Enum):
    ASSET = "asset"
    LIABILITY = "liability"
    EQUITY = "equity"
    REVENUE = "revenue"
    EXPENSE = "expense"

# =============================================
# User Schemas
# =============================================

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_admin: bool
    created_at: datetime
    last_login: Optional[datetime]

    class Config:
        from_attributes = True

# =============================================
# Account Schemas
# =============================================

class AccountBase(BaseModel):
    code: str
    name_ar: str
    name_en: Optional[str] = None
    account_type: AccountType
    parent_account_id: Optional[int] = None
    is_active: bool = True

class AccountCreate(AccountBase):
    pass

class AccountResponse(AccountBase):
    id: int
    balance: Decimal
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# =============================================
# Invoice Schemas
# =============================================

class InvoiceLineCreate(BaseModel):
    item_code: Optional[str] = None
    description: str
    quantity: Decimal = Decimal(1)
    unit_price: Decimal
    tax_rate: Decimal = Decimal(0)

class InvoiceLineResponse(InvoiceLineCreate):
    id: int
    line_total: Decimal
    tax_amount: Decimal

    class Config:
        from_attributes = True

class InvoiceCreate(BaseModel):
    invoice_type: InvoiceType
    invoice_date: date
    customer_id: Optional[int] = None
    supplier_id: Optional[int] = None
    lines: List[InvoiceLineCreate]
    discount: Decimal = Decimal(0)
    notes: Optional[str] = None

class InvoiceResponse(InvoiceCreate):
    id: int
    invoice_number: str
    status: InvoiceStatus
    subtotal: Decimal
    tax_amount: Decimal
    total: Decimal
    paid_amount: Decimal
    created_at: datetime
    lines: List[InvoiceLineResponse]

    class Config:
        from_attributes = True

# =============================================
# Customer & Supplier Schemas
# =============================================

class CustomerBase(BaseModel):
    code: str
    name_ar: str
    name_en: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    tax_number: Optional[str] = None
    credit_limit: Optional[Decimal] = None
    is_active: bool = True

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class SupplierBase(BaseModel):
    code: str
    name_ar: str
    name_en: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    tax_number: Optional[str] = None
    is_active: bool = True

class SupplierCreate(SupplierBase):
    pass

class SupplierResponse(SupplierBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True