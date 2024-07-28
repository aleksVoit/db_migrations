from sqlalchemy.engine import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

engine: AsyncEngine = create_async_engine('postgresql+asyncpg://postgres:0000@localhost:5432/school_db')
AsyncDBSession = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
async_session = AsyncDBSession()
