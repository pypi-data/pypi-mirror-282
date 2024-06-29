from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

class Signing(object):

    def __init__(self, pkcs, password):
        with open(pkcs, 'rb') as pkcs_file:
            pkcs12_data = pkcs_file.read()
        
        self._key, self._cert, _ = pkcs12.load_key_and_certificates(pkcs12_data, password.encode(), default_backend())

    def sign_text(self, data, digest=hashes.SHA256()):
        return self._key.sign(
            data,
            padding.PKCS1v15(),
            digest
        )

    def get_cert_subject(self):
        return self._cert.subject

    def get_cert_binary(self):
        return self._cert.public_bytes(encoding=serialization.Encoding.DER)
