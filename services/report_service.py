from sqlalchemy.orm import Session
from models.database import Account, JournalEntry, JournalEntryLine, Invoice, Payment
from datetime import datetime, date
from decimal import Decimal
from typing import Dict, List

class ReportService:
    
    @staticmethod
    def get_trial_balance(db: Session, as_of_date: date = None) -> Dict:
        if as_of_date is None:
            as_of_date = datetime.now().date()
        
        accounts = db.query(Account).filter(Account.is_active == True).all()
        
        total_debit = Decimal(0)
        total_credit = Decimal(0)
        accounts_data = []
        
        for account in accounts:
            debit_balance = Decimal(0)
            credit_balance = Decimal(0)
            
            lines = db.query(JournalEntryLine).join(
                JournalEntry
            ).filter(
                JournalEntryLine.account_id == account.id,
                JournalEntry.entry_date <= as_of_date,
                JournalEntry.is_posted == True
            ).all()
            
            for line in lines:
                debit_balance += line.debit
                credit_balance += line.credit
            
            if debit_balance > 0 or credit_balance > 0:
                total_debit += debit_balance
                total_credit += credit_balance
                
                accounts_data.append({
                    'account_code': account.code,
                    'account_name': account.name_ar,
                    'debit': debit_balance,
                    'credit': credit_balance
                })
        
        return {
            'report_date': as_of_date,
            'total_debit': total_debit,
            'total_credit': total_credit,
            'is_balanced': total_debit == total_credit,
            'accounts': accounts_data
        }
    
    @staticmethod
    def get_balance_sheet(db: Session, as_of_date: date = None) -> Dict:
        if as_of_date is None:
            as_of_date = datetime.now().date()
        
        assets = []
        liabilities = []
        equity = []
        
        total_assets = Decimal(0)
        total_liabilities = Decimal(0)
        total_equity = Decimal(0)
        
        accounts = db.query(Account).filter(Account.is_active == True).all()
        
        for account in accounts:
            lines = db.query(JournalEntryLine).join(
                JournalEntry
            ).filter(
                JournalEntryLine.account_id == account.id,
                JournalEntry.entry_date <= as_of_date,
                JournalEntry.is_posted == True
            ).all()
            
            balance = Decimal(0)
            for line in lines:
                balance += line.debit - line.credit
            
            if balance != 0:
                account_info = {
                    'code': account.code,
                    'name': account.name_ar,
                    'balance': balance
                }
                
                account_type = account.account_type.name if account.account_type else None
                if account_type == 'asset':
                    assets.append(account_info)
                    total_assets += balance
                elif account_type == 'liability':
                    liabilities.append(account_info)
                    total_liabilities += balance
                elif account_type == 'equity':
                    equity.append(account_info)
                    total_equity += balance
        
        return {
            'report_date': as_of_date,
            'assets': assets,
            'total_assets': total_assets,
            'liabilities': liabilities,
            'total_liabilities': total_liabilities,
            'equity': equity,
            'total_equity': total_equity,
            'total_liabilities_and_equity': total_liabilities + total_equity,
            'is_balanced': total_assets == (total_liabilities + total_equity)
        }