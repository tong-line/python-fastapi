from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from routers import news
# 导入你之前写的 get_db
# from database import get_db 

app = FastAPI()

@app.get("/check-db")
async def check_db(db: AsyncSession = Depends(get_db)):
    try:
        # 执行一条最简单的 SQL 查询
        result = await db.execute(text("SELECT 1"))
        return {"status": "success", "message": "数据库连接正常", "data": result.scalar()}
    except Exception as e:
        # 如果报错，返回详细原因
        raise HTTPException(status_code=500, detail=f"数据库连接失败: {str(e)}")
@app.get("/")
async def root():
    return {"message": "hello world"}

app.include_router(news.router)
