#1
speed = int(input("Hur fort ska du köra? (km/h): "))
distance = 470
speed_mps = speed / 3.6
time_seconds = (distance * 1000) / speed_mps #tid i sekunder

print(f"Det tar {time_seconds} sekunder att köra från stockholm till Göteborg.")


