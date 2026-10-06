"""Modul fungsi kongsi — Latihan Pengaturcaraan Python (Asas), Kursus A1.

tukar_kos(), kira_status() dan ringkasan() telah disediakan (Latihan 1.4).
Lengkapkan bersih() dalam Latihan 2.3; fungsi ini digunakan semula dalam Latihan 3.1 dan mini projek.
"""
from __future__ import annotations

import re


def tukar_kos(nilai) -> float | None:
    """Tukar teks kos berformat "RM1,234,567.00" kepada float. Pulangkan None jika gagal."""
    if isinstance(nilai, (int, float)):
        return float(nilai)
    try:
        bersih = re.sub(r"[^0-9.]", "", str(nilai))
        return float(bersih) if bersih else None
    except (TypeError, ValueError):
        return None


def kira_status(peratus_jadual: float, peratus_fizikal: float, had: float = 20) -> str:
    """Tentukan status projek daripada jurang antara % jadual dan % fizikal."""
    if peratus_fizikal is None or peratus_jadual is None:
        return "Tidak Diketahui"
    if peratus_fizikal >= 100:
        return "Siap"
    if peratus_jadual - peratus_fizikal > had:
        return "Lewat"
    return "Dalam Pelaksanaan"


def ringkasan(rekod: list[dict]) -> dict:
    """Ringkaskan senarai rekod projek (list of dict) kepada statistik asas."""
    jumlah_kos = sum(tukar_kos(r.get("kos_diluluskan", 0)) or 0 for r in rekod)
    bil_lewat = sum(1 for r in rekod if r.get("status") == "Lewat")
    return {
        "bilangan_projek": len(rekod),
        "jumlah_kos": jumlah_kos,
        "bilangan_lewat": bil_lewat,
    }


def bersih(df):
    """Pipeline pembersihan data MyProjek - LENGKAPKAN DALAM LATIHAN 2.3 (nota Bab 5).

    Langkah (ikut turutan nota Bab 5.4):
      1. buang rekod berganda   -> drop_duplicates(subset="id_projek")
      2. teks tidak konsisten   -> negeri: .str.strip().str.title(), betulkan "Wp " -> "WP "
      3. kos sebagai teks       -> kos_diluluskan: .map(tukar_kos)
      4. tarikh format campuran -> tarikh_mula: pd.to_datetime(..., format="mixed")
      5. nilai hilang           -> kementerian: fillna("Tidak Dinyatakan");
                                   peratus_fizikal: median ikut kategori (groupby().transform("median"))
      6. lajur terbitan         -> jurang = peratus_jadual - peratus_fizikal
    Lajur `status` asal dikekalkan. Hasil: 500 baris, 14 lajur, 0 nilai hilang.
    Pulangkan DataFrame baharu (jangan ubah df asal) dengan reset_index(drop=True).
    """
    import pandas as pd  # noqa: F401

    df = df.copy()
    # TODO: langkah 1-6 di atas
    raise NotImplementedError("Lengkapkan bersih() dalam Latihan 2.3")
