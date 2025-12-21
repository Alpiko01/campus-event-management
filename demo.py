# demo.py

from students import add_student
from events import add_event, register
from reports import popular_events, active_students, club_statistics

print("=== ÖĞRENCİ EKLEME ===")
# İsimler güncellendi, ilgi alanları OOP temasına uygun bırakıldı
add_student("2025001", "Melek Efe", "Makine", 2, ["OOP", "Müzik"])
add_student("2025002", "Alpay Kızılkaya", "Bilgisayar", 3, ["OOP"])
add_student("2025003", "Mehmet Ege", "Endüstri", 1, ["Java"])

print("\n=== ETKİNLİK OLUŞTURMA ===")
add_event("OOP101", "Nesne Yönelimli Programlama", "Yazılım", "2025-03-10", "14:00", "D-305", 50)
add_event("DP202", "Tasarım Desenleri Atölyesi", "Yazılım", "2025-03-11", "10:00", "B-201", 30)

print("\n=== ETKİNLİK KAYITLARI ===")
register("2025001", "OOP101")
register("2025002", "OOP101")
register("2025003", "DP202")

print("\n=== RAPORLAR ===")

print("\nEn Popüler Etkinlikler:")
for code, event in popular_events():
    print(code, "-", len(event["participants"]), "katılımcı")

print("\nEn Aktif Öğrenciler:")
for id, student in active_students():
    print(id, "-", len(student["events"]), "etkinlik")

print("\nKulüp İstatistikleri:")
stats = club_statistics()
for club, info in stats.items():
    print(club, "->", info)