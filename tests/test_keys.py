import pytest

from pyelliptic-wrapper.curve import Curve
from pyelliptic-wrapper.keypair import KeyPair

def test_keypair():
    c = Curve('secp256r1')
    assert c 
