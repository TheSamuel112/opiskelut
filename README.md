# Opiskelut

Smuelin opiskelu-appi (deadlinet, lukkari, tenttien ilmot, pisteet). Avautuu koko näytön appina, kun sen lisää puhelimen aloitusnäyttöön.

- `data.enc.json` on salattu (AES-GCM, avain PIN-koodista). Ilman PIN-koodia sitä ei voi lukea.
- Iltapäivitys ajaa: `python3 encrypt.py <PIN> data.json extra.json grades.json > data.enc.json` ja pushaa.
