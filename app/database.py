# database.py
from sqlmodel import SQLModel, create_engine, Session

# SQLite yerel veritabanı dosyasının adı
sqlite_file_name = "farm_database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# SQLite için thread güvenlik ayarıyla engine oluşturma
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})


def create_db_and_tables():
    """models.py içinde tanımlı tüm SQLModel tablolarını SQLite veritabanında otomatik oluşturur."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """FastAPI uç noktalarında (endpoints) veritabanı oturumu açmak ve iş bitince kapatmak için kullanılır."""
    with Session(engine) as session:
        yield session