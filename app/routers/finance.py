from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import (
    NodeBank,
    NodeBankBranch,
    NodeBankAccount,
    NodeContract,
    NodeContractType,
)

router = APIRouter(
    prefix="/finance",
    tags=["Finance (Finans)"],
)


# =========================================================
# BANK CRUD
# =========================================================

@router.post(
    "/banks/",
    response_model=NodeBank,
    status_code=status.HTTP_201_CREATED,
)
def create_bank(
    data: NodeBank,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/banks/",
    response_model=List[NodeBank],
)
def read_banks(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeBank)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/banks/{bank_id}",
    response_model=NodeBank,
)
def read_bank(
    bank_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBank, bank_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka bulunamadı",
        )

    return db_item


@router.patch(
    "/banks/{bank_id}",
    response_model=NodeBank,
)
def update_bank(
    bank_id: int,
    data: NodeBank,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBank, bank_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka bulunamadı",
        )

    update_data = data.model_dump(
        exclude_unset=True,
        exclude={"id", "creation_date", "modification_date"},
    )

    for field, value in update_data.items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/banks/{bank_id}",
    status_code=status.HTTP_200_OK,
)
def delete_bank(
    bank_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBank, bank_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Banka başarıyla silindi",
        "id": bank_id,
    }


# =========================================================
# BANK BRANCH CRUD
# =========================================================

@router.post(
    "/branches/",
    response_model=NodeBankBranch,
    status_code=status.HTTP_201_CREATED,
)
def create_bank_branch(
    data: NodeBankBranch,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/branches/",
    response_model=List[NodeBankBranch],
)
def read_bank_branches(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeBankBranch)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/branches/{branch_id}",
    response_model=NodeBankBranch,
)
def read_bank_branch(
    branch_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBankBranch, branch_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka şubesi bulunamadı",
        )

    return db_item


@router.patch(
    "/branches/{branch_id}",
    response_model=NodeBankBranch,
)
def update_bank_branch(
    branch_id: int,
    data: NodeBankBranch,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBankBranch, branch_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka şubesi bulunamadı",
        )

    update_data = data.model_dump(
        exclude_unset=True,
        exclude={"id", "creation_date", "modification_date"},
    )

    for field, value in update_data.items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/branches/{branch_id}",
    status_code=status.HTTP_200_OK,
)
def delete_bank_branch(
    branch_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBankBranch, branch_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka şubesi bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Banka şubesi başarıyla silindi",
        "id": branch_id,
    }


# =========================================================
# BANK ACCOUNT CRUD
# =========================================================

@router.post(
    "/bank-accounts/",
    response_model=NodeBankAccount,
    status_code=status.HTTP_201_CREATED,
)
def create_bank_account(
    data: NodeBankAccount,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/bank-accounts/",
    response_model=List[NodeBankAccount],
)
def read_bank_accounts(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeBankAccount)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/bank-accounts/{bank_account_id}",
    response_model=NodeBankAccount,
)
def read_bank_account(
    bank_account_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBankAccount, bank_account_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka hesabı bulunamadı",
        )

    return db_item


@router.patch(
    "/bank-accounts/{bank_account_id}",
    response_model=NodeBankAccount,
)
def update_bank_account(
    bank_account_id: int,
    data: NodeBankAccount,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBankAccount, bank_account_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka hesabı bulunamadı",
        )

    update_data = data.model_dump(
        exclude_unset=True,
        exclude={"id", "creation_date", "modification_date"},
    )

    for field, value in update_data.items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/bank-accounts/{bank_account_id}",
    status_code=status.HTTP_200_OK,
)
def delete_bank_account(
    bank_account_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeBankAccount, bank_account_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Banka hesabı bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Banka hesabı başarıyla silindi",
        "id": bank_account_id,
    }


# =========================================================
# CONTRACT TYPE CRUD
# =========================================================

@router.post(
    "/contract-types/",
    response_model=NodeContractType,
    status_code=status.HTTP_201_CREATED,
)
def create_contract_type(
    data: NodeContractType,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/contract-types/",
    response_model=List[NodeContractType],
)
def read_contract_types(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeContractType)
    ).all()


@router.get(
    "/contract-types/{contract_type_id}",
    response_model=NodeContractType,
)
def read_contract_type(
    contract_type_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeContractType, contract_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sözleşme tipi bulunamadı",
        )

    return db_item


@router.patch(
    "/contract-types/{contract_type_id}",
    response_model=NodeContractType,
)
def update_contract_type(
    contract_type_id: int,
    data: NodeContractType,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeContractType, contract_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sözleşme tipi bulunamadı",
        )

    update_data = data.model_dump(
        exclude_unset=True,
        exclude={"id", "creation_date", "modification_date"},
    )

    for field, value in update_data.items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/contract-types/{contract_type_id}",
    status_code=status.HTTP_200_OK,
)
def delete_contract_type(
    contract_type_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeContractType, contract_type_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sözleşme tipi bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Sözleşme tipi başarıyla silindi",
        "id": contract_type_id,
    }


# =========================================================
# CONTRACT CRUD
# =========================================================

@router.post(
    "/contracts/",
    response_model=NodeContract,
    status_code=status.HTTP_201_CREATED,
)
def create_contract(
    data: NodeContract,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/contracts/",
    response_model=List[NodeContract],
)
def read_contracts(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeContract)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get(
    "/contracts/{contract_id}",
    response_model=NodeContract,
)
def read_contract(
    contract_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeContract, contract_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sözleşme bulunamadı",
        )

    return db_item


@router.patch(
    "/contracts/{contract_id}",
    response_model=NodeContract,
)
def update_contract(
    contract_id: int,
    data: NodeContract,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeContract, contract_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sözleşme bulunamadı",
        )

    update_data = data.model_dump(
        exclude_unset=True,
        exclude={"id", "creation_date", "modification_date"},
    )

    for field, value in update_data.items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/contracts/{contract_id}",
    status_code=status.HTTP_200_OK,
)
def delete_contract(
    contract_id: int,
    session: Session = Depends(get_session),
):
    db_item = session.get(NodeContract, contract_id)

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sözleşme bulunamadı",
        )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Sözleşme başarıyla silindi",
        "id": contract_id,
    }