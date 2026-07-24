import csv
import random
import sys

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
random.seed(seed) # deterministic per seed - rerun with the same seed to get the same file

BENIGN_USER_COUNT = 200
EVENTS_PER_BENIGN_USER = 10

def randomTime(startMinutes, endMinutes):
    total = random.randint(startMinutes, endMinutes)
    return f"{total // 60:02d}:{total % 60:02d}"

def benignEvents(user):
    events = []
    for _ in range(EVENTS_PER_BENIGN_USER):
        location = "Unknown" if random.random() < 0.10 else "School"
        result = "failed" if random.random() < 0.05 else "success"
        events.append({
            "time": randomTime(6 * 60, 22 * 60), # normal daytime hours
            "user": user,
            "location": location,
            "event": "login",
            "result": result,
        })
    return events

def bruteForceEvents(user):
    # 5 failed logins within an 8-minute window, from an unfamiliar location, in the unusual-time window
    base = 3 * 60
    return [
        {"time": f"{(base + i * 2) // 60:02d}:{(base + i * 2) % 60:02d}", "user": user,
         "location": "Unknown", "event": "login", "result": "failed"}
        for i in range(5)
    ]

def resetAfterFailEvents(user):
    base = 14 * 60
    return [
        {"time": f"{base // 60:02d}:{base % 60:02d}", "user": user,
         "location": "Unknown", "event": "login", "result": "failed"},
        {"time": f"{base // 60:02d}:{(base + 5) % 60:02d}", "user": user,
         "location": "Unknown", "event": "login", "result": "failed"},
        {"time": f"{base // 60:02d}:{(base + 9) % 60:02d}", "user": user,
         "location": "Unknown", "event": "password_reset", "result": "started"},
    ]

def comboEvents(user):
    # brute force + reset-after-fail, all for one user - worst-case offender
    return bruteForceEvents(user) + resetAfterFailEvents(user)

def main():
    events = []

    for i in range(BENIGN_USER_COUNT):
        events += benignEvents(f"benign_user_{i:03d}")

    events += bruteForceEvents("brute_force_bob")
    events += resetAfterFailEvents("reset_after_fail_rita")
    events += comboEvents("combo_carla")

    events.sort(key=lambda e: e["time"])

    writer = csv.DictWriter(sys.stdout, fieldnames=["time", "user", "location", "event", "result"])
    writer.writeheader()
    writer.writerows(events)

if __name__ == "__main__":
    main()
