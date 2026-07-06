from app.services.ingestion_service import IngestionService


if __name__ == "__main__":

    ingestor = IngestionService()

    ingestor.ingest_all()