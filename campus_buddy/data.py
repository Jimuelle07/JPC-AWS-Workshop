"""Small, hardcoded campus data for the workshop.

IMPORTANT: this is SAMPLE DATA for learning only. It is not official JPC
information. Replace it with real details before anyone relies on it.

The lookup functions are plain Python with no AWS code, so they are easy to
read and easy to test. The agent tools in campus_buddy/tools.py just call them.
"""

REQUIREMENTS = {
    "BSIT": [
        "Form 138 (report card)",
        "Certificate of good moral character",
        "PSA birth certificate (photocopy)",
        "2x2 ID pictures (4 pcs)",
        "Accomplished enrollment form",
    ],
    "BSCS": [
        "Form 138 (report card)",
        "Certificate of good moral character",
        "PSA birth certificate (photocopy)",
        "2x2 ID pictures (4 pcs)",
        "Accomplished enrollment form",
    ],
    "BSCPE": [
        "Form 138 (report card)",
        "Certificate of good moral character",
        "PSA birth certificate (photocopy)",
        "2x2 ID pictures (4 pcs)",
        "Accomplished enrollment form",
    ],
}

SCHEDULES = {
    "BSIT": [
        "Mon 8:00-10:00 AM  Introduction to Computing (Room 101)",
        "Tue 10:00-12:00 PM  Programming 1 (Computer Lab 1)",
        "Thu 1:00-3:00 PM  Understanding the Self (Room 204)",
        "Fri 8:00-10:00 AM  Programming 1 Lab (Computer Lab 1)",
    ],
    "BSCS": [
        "Mon 10:00-12:00 PM  Discrete Mathematics (Room 102)",
        "Wed 8:00-10:00 AM  Programming 1 (Computer Lab 2)",
        "Thu 10:00-12:00 PM  Introduction to Computing (Room 101)",
    ],
    "BSCPE": [
        "Tue 8:00-10:00 AM  Calculus 1 (Room 103)",
        "Wed 1:00-3:00 PM  Computer Engineering Orientation (Room 201)",
        "Fri 10:00-12:00 PM  Programming 1 (Computer Lab 1)",
    ],
}

CANTEEN = {
    "chicken adobo with rice": 65,
    "pancit canton": 35,
    "sinigang na baboy with rice": 75,
    "turon": 15,
    "iced tea": 20,
}


def _clean_course(course):
    """Make 'bs it', 'BSIT ' and 'bsit' all look the same."""
    return "".join(course.upper().split())


def lookup_requirements(course):
    """Return the enrollment requirements for a course, or a helpful message."""
    key = _clean_course(course)
    if key in REQUIREMENTS:
        items = "\n".join("- " + item for item in REQUIREMENTS[key])
        return "Enrollment requirements for " + key + " (sample data):\n" + items
    known = ", ".join(sorted(REQUIREMENTS))
    return "No data for '" + course + "'. Courses I know: " + known + "."


def lookup_schedule(course):
    """Return the sample class schedule for a course, or a helpful message."""
    key = _clean_course(course)
    if key in SCHEDULES:
        return "Class schedule for " + key + " (sample data):\n" + "\n".join(SCHEDULES[key])
    known = ", ".join(sorted(SCHEDULES))
    return "No schedule for '" + course + "'. Courses I know: " + known + "."


def lookup_canteen_price(item):
    """Return the price of a canteen item, or the menu if it is not found."""
    name = item.strip().lower()
    if name in CANTEEN:
        return item.strip() + " costs PHP " + str(CANTEEN[name]) + " (sample data)."
    menu = ", ".join(name + " (PHP " + str(price) + ")" for name, price in CANTEEN.items())
    return "I do not have '" + item + "'. Canteen menu: " + menu + "."
