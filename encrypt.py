"""Salaa appin datan: python3 encrypt.py <PIN> data.json [extra.json] [grades.json] > data.enc.json
data.json = sama rakenne kuin artifaktin app/data (deadlines, registrations, notices, lessons, updated)."""
import sys, json, os, base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
pin = sys.argv[1]
load = lambda p: json.load(open(p, encoding="utf-8")) if p and os.path.exists(p) else None
payload = {"data": load(sys.argv[2]), "extra": load(sys.argv[3] if len(sys.argv) > 3 else None) or {},
           "grades": load(sys.argv[4] if len(sys.argv) > 4 else None) or {"courses": []}}
ITER = 210000
salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(pin.encode())
ct = AESGCM(key).encrypt(iv, json.dumps(payload, ensure_ascii=False).encode("utf-8"), None)
b = lambda x: base64.b64encode(x).decode()
print(json.dumps({"v": 1, "iter": ITER, "salt": b(salt), "iv": b(iv), "ct": b(ct)}))
