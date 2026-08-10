from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .account import NodeAccount
    from .farm_set import NodeFarmSet


# =========================================================
# BANK
# =========================================================

class NodeBankBase(SQLModel):
    status: Optional[str] = None

    bank_code: Optional[str] = None
    bank_name: Optional[str] = None
    bank_type: Optional[str] = None
    bank_desc: Optional[str] = None
    bank_abbr: Optional[str] = None

    display_order: Optional[int] = None

    create_date: Optional[datetime] = None
    close_date: Optional[datetime] = None


class NodeBank(NodeBankBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    branches: List["NodeBankBranch"] = Relationship(
        back_populates="bank"
    )

    bank_accounts: List["NodeBankAccount"] = Relationship(
        back_populates="bank"
    )


# =========================================================
# BANK BRANCH
# =========================================================

class NodeBankBranchBase(SQLModel):
    bank_id: Optional[int] = Field(
        default=None,
        foreign_key="nodebank.id"
    )

    status: Optional[str] = None

    branch_code: Optional[str] = None
    branch_name: Optional[str] = None
    branch_type: Optional[str] = None
    branch_desc: Optional[str] = None
    branch_abbr: Optional[str] = None

    province_name: Optional[str] = None
    district_name: Optional[str] = None
    county_name: Optional[str] = None

    display_order: Optional[int] = None

    create_date: Optional[datetime] = None
    close_date: Optional[datetime] = None


class NodeBankBranch(NodeBankBranchBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    bank: Optional["NodeBank"] = Relationship(
        back_populates="branches"
    )

    bank_accounts: List["NodeBankAccount"] = Relationship(
        back_populates="bank_branch"
    )


# =========================================================
# BANK ACCOUNT
# =========================================================

class NodeBankAccountBase(SQLModel):
    account_id: Optional[int] = Field(
        default=None,
        foreign_key="nodeaccount.id"
    )

    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    bank_id: Optional[int] = Field(
        default=None,
        foreign_key="nodebank.id"
    )

    bank_branch_id: Optional[int] = Field(
        default=None,
        foreign_key="nodebankbranch.id"
    )

    higher_bank_account_id: Optional[int] = Field(
        default=None,
        foreign_key="nodebankaccount.id"
    )

    merged_bank_account_id: Optional[int] = Field(
        default=None,
        foreign_key="nodebankaccount.id"
    )

    status: Optional[str] = None

    bank_account_code: Optional[str] = None
    bank_account_name: Optional[str] = None
    bank_account_type: Optional[str] = None
    bank_account_desc: Optional[str] = None

    currency_type: Optional[str] = None
    iban: Optional[str] = None

    current_balance: Optional[float] = None
    min_balance: Optional[float] = None
    max_balance: Optional[float] = None

    sum_transaction: Optional[float] = None
    last_transaction_amount: Optional[float] = None

    cnt_transaction: Optional[int] = None
    display_order: Optional[int] = None

    create_date: Optional[datetime] = None
    close_date: Optional[datetime] = None

    current_balance_date: Optional[datetime] = None
    first_transaction_date: Optional[datetime] = None
    last_transaction_date: Optional[datetime] = None


class NodeBankAccount(NodeBankAccountBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    account: Optional["NodeAccount"] = Relationship()

    bank: Optional["NodeBank"] = Relationship(
        back_populates="bank_accounts"
    )

    bank_branch: Optional["NodeBankBranch"] = Relationship(
        back_populates="bank_accounts"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="bank_accounts"
    )

    higher_bank_account: Optional["NodeBankAccount"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeBankAccount.higher_bank_account_id]",
            "remote_side": "[NodeBankAccount.id]",
        }
    )

    merged_bank_account: Optional["NodeBankAccount"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeBankAccount.merged_bank_account_id]",
            "remote_side": "[NodeBankAccount.id]",
        }
    )


# =========================================================
# CONTRACT TYPE
# =========================================================

class NodeContractTypeBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    status: Optional[str] = None

    contract_type_name: Optional[str] = None
    contract_type_desc: Optional[str] = None

    display_order: Optional[int] = None


class NodeContractType(NodeContractTypeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    contracts: List["NodeContract"] = Relationship(
        back_populates="contract_type"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="contract_types"
    )


# =========================================================
# CONTRACT
# =========================================================

class NodeContractBase(SQLModel):
    farm_set_id: Optional[int] = Field(
        default=None,
        foreign_key="nodefarmset.id"
    )

    account_id1: Optional[int] = Field(
        default=None,
        foreign_key="nodeaccount.id"
    )

    account_id2: Optional[int] = Field(
        default=None,
        foreign_key="nodeaccount.id"
    )

    bank_account_id1: Optional[int] = Field(
        default=None,
        foreign_key="nodebankaccount.id"
    )

    bank_account_id2: Optional[int] = Field(
        default=None,
        foreign_key="nodebankaccount.id"
    )

    contract_type_id: Optional[int] = Field(
        default=None,
        foreign_key="nodecontracttype.id"
    )

    status: Optional[str] = None

    contract_name: Optional[str] = None
    contract_desc: Optional[str] = None
    contract_code: Optional[str] = None
    contract_summary: Optional[str] = None

    display_order: Optional[int] = None

    contract_payment: Optional[str] = None
    contract_price: Optional[float] = None
    contract_vat: Optional[float] = None
    contract_price_term: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class NodeContract(NodeContractBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    creation_date: datetime = Field(default_factory=datetime.utcnow)
    modification_date: datetime = Field(default_factory=datetime.utcnow)

    contract_type: Optional["NodeContractType"] = Relationship(
        back_populates="contracts"
    )

    farm_set: Optional["NodeFarmSet"] = Relationship(
        back_populates="contracts"
    )

    account1: Optional["NodeAccount"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeContract.account_id1]"
        }
    )

    account2: Optional["NodeAccount"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeContract.account_id2]"
        }
    )

    bank_account1: Optional["NodeBankAccount"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeContract.bank_account_id1]"
        }
    )

    bank_account2: Optional["NodeBankAccount"] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[NodeContract.bank_account_id2]"
        }
    )