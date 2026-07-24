LOW_MAX = 4
MEDIUM_MAX = 14
HIGH_MAX = 24

def riskTier(score):
    if score == 0:
        return "No Risk"
    if score <= LOW_MAX:
        return "Low"
    if score <= MEDIUM_MAX:
        return "Medium"
    if score <= HIGH_MAX:
        return "High"
    return "Critical"

def generateReport(userSusScores, outputPath="soc_report.md"):
    rankedUsers = sorted(
        userSusScores.items(),
        key=lambda item: item[1]["totalScore"],
        reverse=True
    )

    lines = ["# Mini SOC Log Analyzer - Report", ""]
    for user, data in rankedUsers:
        tier = riskTier(data["totalScore"])
        lines.append(f"## {user} - {tier} ({data['totalScore']} pts)")
        if data["reasons"]:
            for reason in data["reasons"]:
                lines.append(f"- {reason}")
        else:
            lines.append("- No suspicious activity detected")
        lines.append("")

    reportText = "\n".join(lines)

    with open(outputPath, "w") as f:
        f.write(reportText)

    print(reportText)
