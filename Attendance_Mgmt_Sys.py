attendance_records = [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),
    (104, "2025-03-01", "Present"),
    (105, "2025-03-01", "Absent"),
]

employees = [
    (101, "Alice Johnson", "HR"),
    (102, "Bob Smith", "IT"),
    (103, "Charlie Brown", "Finance"),
    (104, "David White", "IT"),
    (105, "Eve Black", "Marketing")
]

def attendance_mark(emp_id, date, status):
    attendance_records.append((emp_id, date, status))
    print(f"\nAttendance marked for Employee {emp_id}: {status}")

def attendance_search(emp_id):
    print(f"\nSearching Attendance for Employee ID {emp_id}:")
    for record in attendance_records:
        if record[0] == emp_id:
            print(f"Date: {record[1]}, Status: {record[2]}")


attendance_mark(102, "2025-03-02", "Present")
attendance_search(102)