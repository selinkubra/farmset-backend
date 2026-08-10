from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import (
    NodeBuilding,
    NodeKml,
    NodeKmz,
    NodeUserLogin,
    NodeUserType,
    NodePerson,
    NodePersonInfo,
    NodeLanguage,
    NodeFamily,
    NodeJuridical,
)


router = APIRouter(
    prefix="/core",
    tags=["Core Extra"],
)


# =========================================================
# GENERIC HELPERS
# =========================================================

def get_or_404(session: Session, model, item_id: int, detail: str):
    item = session.get(model, item_id)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )

    return item


def update_model(db_item, data):
    update_data = data.model_dump(
        exclude_unset=True,
        exclude={
            "id",
            "creation_date",
            "modification_date",
        },
    )

    for field, value in update_data.items():
        setattr(db_item, field, value)

    db_item.modification_date = datetime.utcnow()

    return db_item


# =========================================================
# BUILDING CRUD
# =========================================================

@router.post(
    "/buildings/",
    response_model=NodeBuilding,
    status_code=status.HTTP_201_CREATED,
)
def create_building(
    data: NodeBuilding,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/buildings/",
    response_model=List[NodeBuilding],
)
def read_buildings(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeBuilding)
    ).all()


@router.get(
    "/buildings/{item_id}",
    response_model=NodeBuilding,
)
def read_building(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodeBuilding,
        item_id,
        "Bina bulunamadı",
    )


@router.patch(
    "/buildings/{item_id}",
    response_model=NodeBuilding,
)
def update_building(
    item_id: int,
    data: NodeBuilding,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeBuilding,
        item_id,
        "Bina bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/buildings/{item_id}",
)
def delete_building(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeBuilding,
        item_id,
        "Bina bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Bina başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# KML CRUD
# =========================================================

@router.post(
    "/kml/",
    response_model=NodeKml,
    status_code=status.HTTP_201_CREATED,
)
def create_kml(
    data: NodeKml,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/kml/",
    response_model=List[NodeKml],
)
def read_kml_list(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeKml)
    ).all()


@router.get(
    "/kml/{item_id}",
    response_model=NodeKml,
)
def read_kml(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodeKml,
        item_id,
        "KML kaydı bulunamadı",
    )


@router.patch(
    "/kml/{item_id}",
    response_model=NodeKml,
)
def update_kml(
    item_id: int,
    data: NodeKml,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeKml,
        item_id,
        "KML kaydı bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/kml/{item_id}",
)
def delete_kml(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeKml,
        item_id,
        "KML kaydı bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "KML kaydı başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# KMZ CRUD
# =========================================================

@router.post(
    "/kmz/",
    response_model=NodeKmz,
    status_code=status.HTTP_201_CREATED,
)
def create_kmz(
    data: NodeKmz,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/kmz/",
    response_model=List[NodeKmz],
)
def read_kmz_list(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeKmz)
    ).all()


@router.get(
    "/kmz/{item_id}",
    response_model=NodeKmz,
)
def read_kmz(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodeKmz,
        item_id,
        "KMZ kaydı bulunamadı",
    )


@router.patch(
    "/kmz/{item_id}",
    response_model=NodeKmz,
)
def update_kmz(
    item_id: int,
    data: NodeKmz,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeKmz,
        item_id,
        "KMZ kaydı bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/kmz/{item_id}",
)
def delete_kmz(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeKmz,
        item_id,
        "KMZ kaydı bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "KMZ kaydı başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# USER LOGIN CRUD
# =========================================================

@router.post(
    "/user-logins/",
    response_model=NodeUserLogin,
    status_code=status.HTTP_201_CREATED,
)
def create_user_login(
    data: NodeUserLogin,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/user-logins/",
    response_model=List[NodeUserLogin],
)
def read_user_logins(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeUserLogin)
    ).all()


@router.get(
    "/user-logins/{item_id}",
    response_model=NodeUserLogin,
)
def read_user_login(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodeUserLogin,
        item_id,
        "Kullanıcı giriş kaydı bulunamadı",
    )


@router.patch(
    "/user-logins/{item_id}",
    response_model=NodeUserLogin,
)
def update_user_login(
    item_id: int,
    data: NodeUserLogin,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeUserLogin,
        item_id,
        "Kullanıcı giriş kaydı bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/user-logins/{item_id}",
)
def delete_user_login(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeUserLogin,
        item_id,
        "Kullanıcı giriş kaydı bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Kullanıcı giriş kaydı başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# USER TYPE CRUD
# =========================================================

@router.post(
    "/user-types/",
    response_model=NodeUserType,
    status_code=status.HTTP_201_CREATED,
)
def create_user_type(
    data: NodeUserType,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/user-types/",
    response_model=List[NodeUserType],
)
def read_user_types(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeUserType)
    ).all()


@router.get(
    "/user-types/{item_id}",
    response_model=NodeUserType,
)
def read_user_type(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodeUserType,
        item_id,
        "Kullanıcı tipi bulunamadı",
    )


@router.patch(
    "/user-types/{item_id}",
    response_model=NodeUserType,
)
def update_user_type(
    item_id: int,
    data: NodeUserType,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeUserType,
        item_id,
        "Kullanıcı tipi bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/user-types/{item_id}",
)
def delete_user_type(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeUserType,
        item_id,
        "Kullanıcı tipi bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Kullanıcı tipi başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# PERSON CRUD
# =========================================================

@router.post(
    "/persons/",
    response_model=NodePerson,
    status_code=status.HTTP_201_CREATED,
)
def create_person(
    data: NodePerson,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/persons/",
    response_model=List[NodePerson],
)
def read_persons(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodePerson)
    ).all()


@router.get(
    "/persons/{item_id}",
    response_model=NodePerson,
)
def read_person(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodePerson,
        item_id,
        "Kişi bulunamadı",
    )


@router.patch(
    "/persons/{item_id}",
    response_model=NodePerson,
)
def update_person(
    item_id: int,
    data: NodePerson,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodePerson,
        item_id,
        "Kişi bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/persons/{item_id}",
)
def delete_person(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodePerson,
        item_id,
        "Kişi bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Kişi başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# PERSON INFO CRUD
# =========================================================

@router.post(
    "/person-infos/",
    response_model=NodePersonInfo,
    status_code=status.HTTP_201_CREATED,
)
def create_person_info(
    data: NodePersonInfo,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/person-infos/",
    response_model=List[NodePersonInfo],
)
def read_person_infos(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodePersonInfo)
    ).all()


@router.get(
    "/person-infos/{item_id}",
    response_model=NodePersonInfo,
)
def read_person_info(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodePersonInfo,
        item_id,
        "Kişi bilgisi bulunamadı",
    )


@router.patch(
    "/person-infos/{item_id}",
    response_model=NodePersonInfo,
)
def update_person_info(
    item_id: int,
    data: NodePersonInfo,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodePersonInfo,
        item_id,
        "Kişi bilgisi bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/person-infos/{item_id}",
)
def delete_person_info(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodePersonInfo,
        item_id,
        "Kişi bilgisi bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Kişi bilgisi başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# LANGUAGE CRUD
# =========================================================

@router.post(
    "/languages/",
    response_model=NodeLanguage,
    status_code=status.HTTP_201_CREATED,
)
def create_language(
    data: NodeLanguage,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/languages/",
    response_model=List[NodeLanguage],
)
def read_languages(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeLanguage)
    ).all()


@router.get(
    "/languages/{item_id}",
    response_model=NodeLanguage,
)
def read_language(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodeLanguage,
        item_id,
        "Dil bulunamadı",
    )


@router.patch(
    "/languages/{item_id}",
    response_model=NodeLanguage,
)
def update_language(
    item_id: int,
    data: NodeLanguage,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeLanguage,
        item_id,
        "Dil bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/languages/{item_id}",
)
def delete_language(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeLanguage,
        item_id,
        "Dil bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Dil başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# FAMILY CRUD
# =========================================================

@router.post(
    "/families/",
    response_model=NodeFamily,
    status_code=status.HTTP_201_CREATED,
)
def create_family(
    data: NodeFamily,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/families/",
    response_model=List[NodeFamily],
)
def read_families(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeFamily)
    ).all()


@router.get(
    "/families/{item_id}",
    response_model=NodeFamily,
)
def read_family(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodeFamily,
        item_id,
        "Aile bulunamadı",
    )


@router.patch(
    "/families/{item_id}",
    response_model=NodeFamily,
)
def update_family(
    item_id: int,
    data: NodeFamily,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeFamily,
        item_id,
        "Aile bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/families/{item_id}",
)
def delete_family(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeFamily,
        item_id,
        "Aile bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Aile başarıyla silindi",
        "id": item_id,
    }


# =========================================================
# JURIDICAL CRUD
# =========================================================

@router.post(
    "/juridicals/",
    response_model=NodeJuridical,
    status_code=status.HTTP_201_CREATED,
)
def create_juridical(
    data: NodeJuridical,
    session: Session = Depends(get_session),
):
    session.add(data)
    session.commit()
    session.refresh(data)

    return data


@router.get(
    "/juridicals/",
    response_model=List[NodeJuridical],
)
def read_juridicals(
    session: Session = Depends(get_session),
):
    return session.exec(
        select(NodeJuridical)
    ).all()


@router.get(
    "/juridicals/{item_id}",
    response_model=NodeJuridical,
)
def read_juridical(
    item_id: int,
    session: Session = Depends(get_session),
):
    return get_or_404(
        session,
        NodeJuridical,
        item_id,
        "Tüzel kişi bulunamadı",
    )


@router.patch(
    "/juridicals/{item_id}",
    response_model=NodeJuridical,
)
def update_juridical(
    item_id: int,
    data: NodeJuridical,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeJuridical,
        item_id,
        "Tüzel kişi bulunamadı",
    )

    update_model(db_item, data)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@router.delete(
    "/juridicals/{item_id}",
)
def delete_juridical(
    item_id: int,
    session: Session = Depends(get_session),
):
    db_item = get_or_404(
        session,
        NodeJuridical,
        item_id,
        "Tüzel kişi bulunamadı",
    )

    session.delete(db_item)
    session.commit()

    return {
        "message": "Tüzel kişi başarıyla silindi",
        "id": item_id,
    }