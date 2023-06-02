from faster_orm import FastModel, Field
import pytest

class A(FastModel):
    num: int

class B(FastModel):
    num: int = Field(gt=-1000)

class C(FastModel):
    num: int = Field(zero=True)

def test_no_db():
    a1 = A(num=1)
    with pytest.raises(Exception) as e_info:
        a2 = A(num=0)
    with pytest.raises(Exception) as e_info:
        a3 = A(num=-1)

    b1 = B(num=1)
    b2 = B(num=0)
    b3 = B(num=-1)

    c1 = C(num=1)
    c2 = C(num=0)
    c3 = C(num=-1)
