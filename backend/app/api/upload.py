from pathlib import Path
import shutil

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from app.services.ingestion_service import IngestionService

router = APIRouter(
    prefix="/api/v2/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path(__file__).resolve().parents[3] / "data" / "uploads"

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)

ALLOWED_EXTENSIONS = {
    ".txt",
    ".md",
    ".pdf"
}


@router.post("/")
def upload_file(
    file: UploadFile = File(...)
):

    suffix = Path(file.filename).suffix.lower()

    if suffix not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    ingestor = IngestionService()

    chunks = ingestor.ingest_file(file_path)

    return {

        "status": "success",

        "filename": file.filename,

        "chunks_indexed": chunks,

        "location": str(file_path)

    }