from sqlalchemy.orm import Session
from models.database import Invoice, InvoiceLine, Customer, Supplier, User
from models.schemas import InvoiceCreate, InvoiceResponse
from datetime import datetime
from decimal import Decimal
import random
import string

class InvoiceService:
    
    @staticmethod
    def generate_invoice_number() -> str:
        timestamp = datetime.now().strftime("%Y%m%d")
        random_suffix = ''.join(random.choices(string.digits, k=6))
        return f"INV-{timestamp}-{random_suffix}"
    
    @staticmethod
    def create_invoice(db: Session, invoice_data: InvoiceCreate, user_id: int) -> Invoice:
        subtotal = Decimal(0)
        tax_total = Decimal(0)
        
        for line in invoice_data.lines:
            line_subtotal = line.quantity * line.unit_price
            line_tax = line_subtotal * (line.tax_rate / 100)
            subtotal += line_subtotal
            tax_total += line_tax
        
        total = subtotal - invoice_data.discount + tax_total
        
        invoice = Invoice(
            invoice_number=InvoiceService.generate_invoice_number(),
            invoice_type=invoice_data.invoice_type,
            invoice_date=invoice_data.invoice_date,
            customer_id=invoice_data.customer_id,
            supplier_id=invoice_data.supplier_id,
            subtotal=subtotal,
            discount=invoice_data.discount,
            tax_amount=tax_total,
            total=total,
            notes=invoice_data.notes,
            created_by=user_id
        )
        
        for line_data in invoice_data.lines:
            line_subtotal = line_data.quantity * line_data.unit_price
            line_tax = line_subtotal * (line_data.tax_rate / 100)
            
            line = InvoiceLine(
                item_code=line_data.item_code,
                description=line_data.description,
                quantity=line_data.quantity,
                unit_price=line_data.unit_price,
                line_total=line_subtotal,
                tax_rate=line_data.tax_rate,
                tax_amount=line_tax
            )
            invoice.lines.append(line)
        
        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        return invoice
    
    @staticmethod
    def get_invoice(db: Session, invoice_id: int) -> Invoice:
        return db.query(Invoice).filter(Invoice.id == invoice_id).first()
    
    @staticmethod
    def get_all_invoices(db: Session, skip: int = 0, limit: int = 100) -> list:
        return db.query(Invoice).offset(skip).limit(limit).all()