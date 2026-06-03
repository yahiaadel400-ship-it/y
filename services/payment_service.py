from sqlalchemy.orm import Session
from models.database import Payment, Invoice, Customer, Supplier
from models.schemas import PaymentCreate
from datetime import datetime
from decimal import Decimal
import random
import string

class PaymentService:
    
    @staticmethod
    def generate_payment_number() -> str:
        timestamp = datetime.now().strftime("%Y%m%d")
        random_suffix = ''.join(random.choices(string.digits, k=6))
        return f"PAY-{timestamp}-{random_suffix}"
    
    @staticmethod
    def create_payment(db: Session, payment_data: PaymentCreate, user_id: int) -> Payment:
        payment = Payment(
            payment_number=PaymentService.generate_payment_number(),
            payment_date=payment_data.payment_date,
            payment_type=payment_data.payment_type,
            amount=payment_data.amount,
            invoice_id=payment_data.invoice_id,
            customer_id=payment_data.customer_id,
            supplier_id=payment_data.supplier_id,
            reference_number=payment_data.reference_number,
            notes=payment_data.notes,
            created_by=user_id
        )
        
        if payment_data.invoice_id:
            invoice = db.query(Invoice).filter(Invoice.id == payment_data.invoice_id).first()
            if invoice:
                invoice.paid_amount += payment_data.amount
                
                if invoice.paid_amount >= invoice.total:
                    invoice.status = 'paid'
                elif invoice.paid_amount > 0:
                    invoice.status = 'partial'
                
                invoice.updated_at = datetime.utcnow()
        
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment
    
    @staticmethod
    def get_payment(db: Session, payment_id: int) -> Payment:
        return db.query(Payment).filter(Payment.id == payment_id).first()