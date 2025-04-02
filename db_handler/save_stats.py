from .create_db import SessionLocal, Statistics

def save_stats(model, view_count, req_count, date):
    db = SessionLocal()
    try:
        db_stats = Statistics(model=model, view_count=view_count, req_count=req_count, date=date)
        db.add(db_stats)
        db.commit()
        db.refresh(db_stats)
    finally:
        db.close()