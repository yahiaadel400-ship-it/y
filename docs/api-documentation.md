# توثيق واجهات البرمجة (API)

## 🔗 نقاط النهاية الرئيسية

### المصادقة والمستخدمون

#### تسجيل مستخدم جديد
```
POST /api/v1/auth/register
Content-Type: application/json

{
  "username": "user@example.com",
  "email": "user@example.com",
  "password": "secure_password",
  "full_name": "User Name"
}
```

#### تسجيل الدخول
```
POST /api/v1/auth/login
Content-Type: application/json

{
  "username": "user@example.com",
  "password": "secure_password"
}
```

**الاستجابة:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

### إدارة الحسابات

#### إنشاء حساب
```
POST /api/v1/accounts
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "code": "1000",
  "name_ar": "الأصول الجارية",
  "name_en": "Current Assets",
  "account_type": "asset",
  "is_active": true
}
```

#### الحصول على جميع الحسابات
```
GET /api/v1/accounts
Authorization: Bearer {access_token}
```

#### الحصول على حساب محدد
```
GET /api/v1/accounts/{account_id}
Authorization: Bearer {access_token}
```

### القيود اليومية

#### إنشاء قيد يومي
```
POST /api/v1/journal-entries
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "entry_date": "2024-01-15",
  "description": "تسجيل فاتورة بيع",
  "reference_number": "INV-001",
  "reference_type": "invoice",
  "lines": [
    {
      "account_id": 1,
      "debit": 10000,
      "credit": 0,
      "description": "ذمم العملاء"
    },
    {
      "account_id": 2,
      "debit": 0,
      "credit": 10000,
      "description": "إيرادات المبيعات"
    }
  ]
}
```

### الفواتير

#### إنشاء فاتورة
```
POST /api/v1/invoices
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "invoice_type": "sales",
  "invoice_date": "2024-01-15",
  "customer_id": 1,
  "lines": [
    {
      "item_code": "ITEM001",
      "description": "منتج 1",
      "quantity": 2,
      "unit_price": 100,
      "tax_rate": 14
    }
  ],
  "discount": 10,
  "notes": "ملاحظات إضافية"
}
```

#### الحصول على الفواتير
```
GET /api/v1/invoices
Authorization: Bearer {access_token}

// معاملات اختيارية:
// ?skip=0
// ?limit=50
// ?status=paid
// ?customer_id=1
```

### الدفعات

#### إنشاء دفعة
```
POST /api/v1/payments
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "payment_date": "2024-01-15",
  "payment_type": "transfer",
  "amount": 10000,
  "invoice_id": 1,
  "reference_number": "TRN-001",
  "notes": "تحويل بنكي"
}
```

### العملاء والمورديين

#### إنشاء عميل
```
POST /api/v1/customers
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "code": "CUST001",
  "name_ar": "اسم العميل",
  "name_en": "Customer Name",
  "email": "customer@example.com",
  "phone": "+201001234567",
  "address": "العنوان",
  "city": "المدينة",
  "country": "الدولة",
  "credit_limit": 50000
}
```

### المخزون

#### إنشاء صنف
```
POST /api/v1/items
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "item_code": "ITEM001",
  "name_ar": "اسم الصنف",
  "name_en": "Item Name",
  "unit_of_measure": "وحدة",
  "quantity_on_hand": 100,
  "reorder_level": 20,
  "unit_cost": 1000,
  "selling_price": 1500
}
```

#### تسجيل حركة مخزن
```
POST /api/v1/inventory-movements
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "movement_date": "2024-01-15",
  "movement_type": "purchase",
  "item_id": 1,
  "quantity": 50,
  "unit_cost": 1000,
  "reference_number": "PO-001",
  "notes": "استقبال من المورديين"
}
```

### التقارير

#### الميزانية العمومية
```
GET /api/v1/reports/balance-sheet
Authorization: Bearer {access_token}

// معاملات اختيارية:
// ?as_of_date=2024-01-31
```

#### بيان الدخل
```
GET /api/v1/reports/income-statement
Authorization: Bearer {access_token}

// معاملات مطلوبة:
// ?start_date=2024-01-01
// ?end_date=2024-01-31
```

#### الرصيد التجريبي
```
GET /api/v1/reports/trial-balance
Authorization: Bearer {access_token}

// معاملات اختيارية:
// ?as_of_date=2024-01-31
```

## 🔒 رموز الأخطاء

| الكود | المعنى |
|------|--------|
| 200 | نجاح العملية |
| 201 | تم الإنشاء بنجاح |
| 400 | طلب غير صحيح |
| 401 | لم يتم المصادقة |
| 403 | ممنوع الوصول |
| 404 | لم يتم العثور على المورد |
| 409 | تعارض |
| 422 | بيانات غير صالحة |
| 500 | خطأ في الخادم |