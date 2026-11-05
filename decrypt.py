"""Purkaa salauksen: python3 decrypt.py <PIN> data.enc.json  -> kirjoittaa data.json, extra.json, grades.json"""
import sys, json, base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
pin, path = sys.argv[1], sys.argv[2]
b = json.load(open(path)); d = lambda s: base64.b64decode(s)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=d(b["salt"]), iterations=b["iter"]).derive(pin.encode())
p = json.loads(AESGCM(key).decrypt(d(b["iv"]), d(b["ct"]), None))
for k in ("data", "extra", "grades"):
    json.dump(p.get(k) or {}, open(k + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
