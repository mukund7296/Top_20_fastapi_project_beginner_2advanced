from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/patients", tags=["Patients"])


# ── CREATE ──────────────────────────────────────────────────────────
@router.post(
    "/",
    response_model=schemas.PatientResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new patient",
)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    """Create a new patient record in the database."""
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


# ── READ ALL ─────────────────────────────────────────────────────────
@router.get(
    "/",
    response_model=List[schemas.PatientResponse],
    summary="List all patients",
)
def get_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve all patients with pagination (skip/limit)."""
    return db.query(models.Patient).offset(skip).limit(limit).all()


# ── READ ONE ─────────────────────────────────────────────────────────
@router.get(
    "/{patient_id}",
    response_model=schemas.PatientResponse,
    summary="Get a patient by ID",
)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    """Retrieve a single patient by their ID."""
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with id {patient_id} not found",
        )
    return patient


# ── UPDATE ───────────────────────────────────────────────────────────
@router.patch(
    "/{patient_id}",
    response_model=schemas.PatientResponse,
    summary="Update a patient",
)
def update_patient(
    patient_id: int,
    updates: schemas.PatientUpdate,
    db: Session = Depends(get_db),
):
    """Partially update a patient record. Only send fields you want to change."""
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with id {patient_id} not found",
        )
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(patient, field, value)
    db.commit()
    db.refresh(patient)
    return patient


# ── DELETE ───────────────────────────────────────────────────────────
@router.delete(
    "/{patient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a patient",
)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    """Permanently delete a patient record."""
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with id {patient_id} not found",
        )
    db.delete(patient)
    db.commit()
