# Subscription Billing System

This is a full-stack billing system that supports:
- Multiple subscriptions
- Tax and discount logic (including coupons)
- Multi-currency support
- JSON bill generation
- Clean UI for bill presentation using React and TailwindCSS

## How to Run

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (React + TailwindCSS)
```bash
cd frontend
npm install
npm run dev
```