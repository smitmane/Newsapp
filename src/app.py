from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models import News
import requests


app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello, Fastapi"}

@app.get("/get_news/")
def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()

@app.delete('/delete-partial-records/')
def delete_partial_records(db: Session=Depends(get_db)):
    total_records = db.query(News).filter(News.id%2==0).delete()
    db.commit()
    return {"message": f"{total_records} Records deleted"}

@app.post("/fetch_news/")
def fetch_news(db:Session=Depends(get_db)):
    try:
        response = news_api()
        if response:
            json_data = response.json()
            if json_data.get('status') == "ok":
                articles = json_data.get('articles')
                article = News(result = articles)
                db.add(article)
                db.commit()
                db.refresh(article)
                return JSONResponse(content={"message":"data inserted successfully"},status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": "Failed to fetch news"}, status_code=400)

def news_api():
    try:

        url = "https://newsapi.org/v2/everything?q=apple&from=2025-03-25&to=2025-03-25&sortBy=popularity&apiKey=cba17de97a244d659909501cacba115c"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        # print(response.text)
        return response
    except Exception as e:
        print(e)
        return False


# from database import engine, Base

# # Create database tables
# Base.metadata.create_all(bind=engine)