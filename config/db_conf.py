from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

ASYNC_DATABASE_URL = "mysql+aiomysql://root:ECNUsei123@172.31.84.169:3306/fastapi_study"

async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()  # 如果操作成功，自动提交事务
        except Exception:
            await session.rollback() # 如果出错，自动回滚
            raise
        finally:
            await session.close()    # 确保无论是否成功，最后都会关闭连接