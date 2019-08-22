@ECHO OFF
ECHO .:[ JADWAL SHOLAT wilayah JAKARTA ]:.
ECHO versi PKPU.OR.ID
ECHO.
ECHO Mengambil Data...
ECHO.

@PYTHON JadwalSholatPKPU.py "https://jadwalsholat.pkpu.or.id/?id=83" > JadwalSholatPKPU.LOG

ECHO Jadwal di simpan ke File "JadwalSholatPKPU.html"