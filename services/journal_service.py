from sqlalchemy.orm import Session
from models.database import JournalEntry, JournalEntryLine, Account
from models.schemas import JournalEntryCreate
from datetime import datetime
from decimal import Decimal
import random
import string

class JournalService:
    
    @staticmethod
    def generate_entry_number() -> str:
        timestamp = datetime.now().strftime("%Y%m%d")
        random_suffix = ''.join(random.choices(string.digits, k=6))
        return f"JE-{timestamp}-{random_suffix}"
    
    @staticmethod
    def create_journal_entry(db: Session, entry_data: JournalEntryCreate, user_id: int) -> JournalEntry:
        total_debit = Decimal(0)
        total_credit = Decimal(0)
        
        for line in entry_data.lines:
            total_debit += line.debit
            total_credit += line.credit
        
        is_balanced = total_debit == total_credit
        
        entry = JournalEntry(
            entry_number=JournalService.generate_entry_number(),
            entry_date=entry_data.entry_date,
            description=entry_data.description,
            reference_number=entry_data.reference_number,
            reference_type=entry_data.reference_type,
            total_debit=total_debit,
            total_credit=total_credit,
            is_balanced=is_balanced,
            created_by=user_id
        )
        
        for line_data in entry_data.lines:
            line = JournalEntryLine(
                account_id=line_data.account_id,
                debit=line_data.debit,
                credit=line_data.credit,
                description=line_data.description
            )
            entry.lines.append(line)
        
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry
    
    @staticmethod
    def get_journal_entry(db: Session, entry_id: int) -> JournalEntry:
        return db.query(JournalEntry).filter(JournalEntry.id == entry_id).first()