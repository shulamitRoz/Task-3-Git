# convert_coordinates.py

# --- דאטה קואורדינטות במעלות עשרוניות (DD) ---
coordinates = {
    "anchorage": {"dd": [-149.9002, 61.2181, 22]},
    "los_angeles": {"dd": [-118.2437, 34.0522]}
}

# --- פונקציה להמרת DD ל-DMS ---
def dd_to_dms(dd, is_latitude=False):
    degrees = int(abs(dd))  # החלק השלם של המעלות
    minutes_float = (abs(dd) - degrees) * 60
    minutes = int(minutes_float)  # החלק השלם של הדקות
    seconds = round((minutes_float - minutes) * 60, 2)  # שניות עם 2 ספרות אחרי הנקודה

    # כיוון
    if is_latitude:
        direction = "N" if dd >= 0 else "S"
    else:
        direction = "E" if dd >= 0 else "W"

    return [degrees, minutes, seconds, direction]

# --- המרת כל הקואורדינטות ---
dms_coordinates = {}

for city, data in coordinates.items():
    dd_list = data["dd"]
    dms_list = []

    # Longitude → קו אורך
    dms_list.append(dd_to_dms(dd_list[0], is_latitude=False))
    # Latitude → קו רוחב
    dms_list.append(dd_to_dms(dd_list[1], is_latitude=True))

    # אם יש רכיב של גובה (altitude)
    if len(dd_list) > 2:
        dms_list.append(dd_list[2])

    dms_coordinates[city] = {"dms": dms_list}

# --- הצגת התוצאה ---
print("DMS coordinates:")
print(dms_coordinates)
