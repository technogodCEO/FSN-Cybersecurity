import csv
import sys

import report

MAX_FAILED_LOGIN_WINDOW = 15 # largest window any rule checks against failedLoginTimes

FAILED_LOGIN_POINTS = 2
UNKNOWN_LOCATION_POINTS = 3
UNUSUAL_TIME_POINTS = 2
PASSWORD_RESET_POINTS = 5
BRUTE_FORCE_BONUS = 6
RESET_AFTER_FAIL_BONUS = 5

BRUTE_FORCE_STREAK_COUNT = 3
BRUTE_FORCE_WINDOW = 10
RESET_AFTER_FAIL_WINDOW = 15
UNUSUAL_TIME_START = 0
UNUSUAL_TIME_END = 5 * 60 # 05:00

userSusScores = {}

def ensureUser(user):
    if user not in userSusScores:
        userSusScores[user] = {
            "totalScore": 0,
            "reasons": [],
            "failedLoginTimes": [],
            "lastStreakTriggerTime": None, # last failed-login time already counted toward a scored streak
        }

def removeReason(user, reason): # use to replace failed login attempt with multiple failed login attempts
    ensureUser(user)
    userSusScores[user]["reasons"].remove(reason)

def addReason(user, reason):
    ensureUser(user)
    userSusScores[user]["reasons"].append(reason)

def addOrUpgradeReason(user, baseReason):
    ensureUser(user)
    reasons = userSusScores[user]["reasons"]
    multipleReason = "multiple " + baseReason + "s"
    if multipleReason in reasons:
        return
    if baseReason in reasons:
        removeReason(user, baseReason)
        addReason(user, multipleReason)
    else:
        addReason(user, baseReason)

def addScore(user, amount):
    ensureUser(user)
    userSusScores[user]["totalScore"] += amount

def parseTime(t): # "HH:MM" -> minutes since midnight (a raw int for calculation)
    hours, minutes = t.split(":")
    return int(hours) * 60 + int(minutes)

def trimFailedLogins(user, currentMinutes):
    # bounds memory growth only - safe because no rule ever needs an entry older than the largest window in use
    ensureUser(user)
    userSusScores[user]["failedLoginTimes"] = [
        t for t in userSusScores[user]["failedLoginTimes"]
        if currentMinutes - t <= MAX_FAILED_LOGIN_WINDOW
    ]

def countRecentFailedLogins(user, currentMinutes, windowMinutes, sinceTime=None):
    # non-destructive: just counts, never mutates failedLoginTimes
    ensureUser(user)
    return sum(
        1 for t in userSusScores[user]["failedLoginTimes"]
        if currentMinutes - t <= windowMinutes and (sinceTime is None or t > sinceTime)
    )

def processRow(row):
    # NOTE: assumes rows arrive already sorted by time (true of the sample logs) -
    # pattern rules below rely on that ordering.
    user = row["user"]
    currentMinutes = parseTime(row["time"])
    ensureUser(user)

    # Rule 1: failed login
    if row["event"] == "login" and row["result"] == "failed":
        addScore(user, FAILED_LOGIN_POINTS)
        addOrUpgradeReason(user, "failed login attempt")

        userSusScores[user]["failedLoginTimes"].append(currentMinutes)
        trimFailedLogins(user, currentMinutes) # bound growth only - never removes anything a rule still needs

        # Rule 5: brute-force streak (3+ failed logins within 10 min, not already counted in a prior streak)
        streakCount = countRecentFailedLogins(user, currentMinutes, BRUTE_FORCE_WINDOW, userSusScores[user]["lastStreakTriggerTime"])
        if streakCount >= BRUTE_FORCE_STREAK_COUNT:
            addScore(user, BRUTE_FORCE_BONUS)
            addOrUpgradeReason(user, "brute force login streak")
            userSusScores[user]["lastStreakTriggerTime"] = currentMinutes

    # Rule 2: unknown location
    if row["location"] == "Unknown":
        addScore(user, UNKNOWN_LOCATION_POINTS)
        addOrUpgradeReason(user, "unknown location login")

    # Rule 3: unusual time (00:00-05:00 inclusive)
    if UNUSUAL_TIME_START <= currentMinutes <= UNUSUAL_TIME_END:
        addScore(user, UNUSUAL_TIME_POINTS)
        addOrUpgradeReason(user, "unusual time login")

    # Rule 4: password reset started
    if row["event"] == "password_reset" and row["result"] == "started":
        addScore(user, PASSWORD_RESET_POINTS)
        addOrUpgradeReason(user, "password reset")

        # Rule 6: reset after failed login(s) within 15 min
        if countRecentFailedLogins(user, currentMinutes, RESET_AFTER_FAIL_WINDOW) >= 1:
            addScore(user, RESET_AFTER_FAIL_BONUS)
            addOrUpgradeReason(user, "password reset after failed login")

def main():
    csvChart = csv.DictReader(sys.stdin)
    for row in csvChart:
        processRow(row)
    report.generateReport(userSusScores)

if __name__ == "__main__":
    main()
