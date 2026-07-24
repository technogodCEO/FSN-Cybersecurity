**Cybersecurity Summer Course Capstone Guide**

Mathematical Projects, Simple Python Projects, and Complex Python Projects

**For High School Students | Defensive, Safe, Practical, and Presentation-Friendly**

This guide converts the cybersecurity summer course into practical capstone projects that students can measure, calculate, and demonstrate. The projects are intentionally defensive and safe. Students should use fake data, sample logs, and controlled classroom scenarios only. No project requires attacking real systems, collecting real passwords, scanning networks, or accessing accounts without permission.

| Safety rule: Every project must protect people, respect privacy, use permission-based data, and avoid harmful instructions. Use sample/fake data whenever possible. |
| :---- |

# **Quick Project Categories**

| Category | Best For | Student Output | Recommended Difficulty |
| :---- | :---- | :---- | :---- |
| Mathematical Capstone Projects | Students who like formulas, scoring, charts, and risk models | Spreadsheet, table, chart, short report | Beginner to Medium |
| Simple Python Projects | Students learning variables, input, if/else, loops, lists, and functions | Small program \+ screenshot/output \+ explanation | Beginner |
| Complex Python Projects | Students ready for files, CSV, dictionaries, functions, scoring engines, and reports | Program \+ sample data \+ generated report/dashboard | Medium to Advanced |

# **Common Capstone Workflow**

1\. Choose a safe cybersecurity problem from the course, such as phishing, password risk, privacy exposure, account takeover, backups, or suspicious login activity.

2\. Define the input data. Use fake survey answers, fake log entries, fake messages, or a sample spreadsheet.

3\. Build a scoring model using points, weights, likelihood x impact, before/after comparison, or benefit divided by effort.

4\. Create the output: a risk score, ranked list, recommendation, chart, or incident report.

5\. Explain what the result means and recommend safe actions.

6\. Present the project in 5-7 minutes using one visual: table, chart, sample output, or simple diagram.

# **Category A: Mathematical Capstone Projects**

These projects can be completed with a calculator, spreadsheet, or simple tables. Python is optional.

## **A1. Personal Cyber Risk Score Calculator**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Mathematical | Beginner | Measure a student or family cyber-risk score using weighted habits. |

**Objective: Measure a student or family cyber-risk score using weighted habits.**

**Mathematical or analytical model: Final Score \= sum(Weight x Risk Score); classify as Low, Medium, or High.**

**How to do it:**

1\. Choose 8-12 safety factors such as MFA, backups, screen lock, privacy settings, password reuse, updates, and suspicious-link behavior.

2\. Assign each factor a weight that totals 100%.

3\. Score each factor from 0-5 where 0 is safe and 5 is risky.

4\. Calculate the weighted score and classify the result.

5\. Recommend the top three improvements.

**Deliverables:**

• Weighted risk table

• Final risk score

• Top three recommendations

## **A2. Phishing Probability Scoring Model**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Mathematical | Beginner | Score a sample message based on phishing warning signs. |

**Objective: Score a sample message based on phishing warning signs.**

**Mathematical or analytical model: Phishing Score \= sum(Warning Sign Points).**

**How to do it:**

1\. Create 5-8 warning signs such as urgency, suspicious link, strange sender, password request, MFA-code request, attachment, and spelling errors.

2\. Assign points to each warning sign.

3\. Evaluate 3 fake messages.

4\. Classify messages as low, medium, or high suspicion.

5\. Recommend a safe response: do not click, verify, and report.

**Deliverables:**

• Scoring checklist

• Three scored fake messages

• Safe action recommendation

## **A3. School Account Risk Ranking Matrix**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Mathematical | Beginner | Rank school accounts by risk using likelihood and impact. |

**Objective: Rank school accounts by risk using likelihood and impact.**

**Mathematical or analytical model: Risk \= Likelihood x Impact.**

**How to do it:**

1\. List accounts such as school email, LMS, phone, cloud storage, social media, and gaming.

2\. Score likelihood from 1-5 and impact from 1-5.

3\. Multiply to calculate risk.

4\. Sort from highest to lowest risk.

5\. Suggest controls for the highest-risk accounts.

**Deliverables:**

• Risk matrix

• Ranked account list

• Protection plan

## **A4. MFA Impact Calculator**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Mathematical | Medium | Estimate how much MFA reduces account takeover risk. |

**Objective: Estimate how much MFA reduces account takeover risk.**

**Mathematical or analytical model: New Risk \= Original Risk x (1 \- Control Effectiveness).**

**How to do it:**

1\. Choose sample accounts and assign original risk scores out of 100\.

2\. Assume MFA reduces risk by a selected percentage such as 50%, 60%, or 70%.

3\. Calculate new risk after MFA.

4\. Compare before and after.

5\. Explain why MFA helps but does not replace careful behavior.

**Deliverables:**

• Before/after table

• Risk reduction calculation

• Short interpretation

## **A5. Cybersecurity Control Cost-Benefit Ranking**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Mathematical | Medium | Rank security controls by protection value compared with effort. |

**Objective: Rank security controls by protection value compared with effort.**

**Mathematical or analytical model: Value Score \= Benefit / Effort.**

**How to do it:**

1\. Choose controls such as MFA, backups, updates, passphrase, privacy review, phishing training, and screen lock.

2\. Score benefit from 1-5 and effort from 1-5.

3\. Calculate value score for each control.

4\. Rank the controls.

5\. Recommend the first three controls students should implement.

**Deliverables:**

• Control ranking table

• Value score calculation

• Best-first action list

# **Category B: Python-Based Simple Projects**

These projects are good for students beginning Python. They use input(), variables, if/else, loops, and simple lists/dictionaries.

## **B1. Password Strength Estimator**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Simple Python | Beginner | Check sample passwords or passphrases against basic safety rules. |

**Objective: Check sample passwords or passphrases against basic safety rules.**

**Mathematical or analytical model: Score \= length points \+ character variety points \+ uniqueness guidance.**

**How to do it:**

1\. Create fake password examples only.

2\. Give points for length, symbols, numbers, and mixed case.

3\. Classify the sample as weak, moderate, or strong.

4\. Explain that students should not type real passwords into classroom tools.

**Deliverables:**

• Python script

• Screenshot of sample results

• Short explanation

## **B2. Phishing Score Calculator**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Simple Python | Beginner | Calculate whether a fake message looks suspicious. |

**Objective: Calculate whether a fake message looks suspicious.**

**Mathematical or analytical model: Score \= sum of warning-sign points.**

**How to do it:**

1\. Ask yes/no questions about warning signs.

2\. Add points for each warning sign.

3\. Classify the message by suspicion level.

4\. Recommend safe action based on score.

**Deliverables:**

• Python script

• Three fake message tests

• Safe response explanation

## **B3. Social Media Privacy Exposure Index**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Simple Python | Beginner | Calculate exposure from a fake or self-reviewed social profile. |

**Objective: Calculate exposure from a fake or self-reviewed social profile.**

**Mathematical or analytical model: Exposure Index \= sum of visible-data points.**

**How to do it:**

1\. Use a fake profile template or safe self-assessment.

2\. Add points for visible personal data.

3\. Classify exposure level.

4\. Recommend privacy settings to change.

**Deliverables:**

• Python script

• Privacy score

• Recommendations

## **B4. Backup Schedule Planner**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Simple Python | Beginner-Medium | Recommend backup frequency based on importance and change frequency. |

**Objective: Recommend backup frequency based on importance and change frequency.**

**Mathematical or analytical model: Backup Priority \= Importance x Change Frequency.**

**How to do it:**

1\. List file categories such as homework, photos, notes, and projects.

2\. Score importance and change frequency.

3\. Calculate priority.

4\. Recommend daily, weekly, or monthly backups.

**Deliverables:**

• Python script

• Backup plan table

• Availability explanation

## **B5. Security Control Recommendation Engine**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Simple Python | Beginner-Medium | Recommend controls for common student cyber risks. |

**Objective: Recommend controls for common student cyber risks.**

**Mathematical or analytical model: Rule-based mapping from risk type to recommended controls.**

**How to do it:**

1\. Create a dictionary of risks and controls.

2\. Ask the user to choose a risk.

3\. Print recommended defensive actions.

4\. Explain why the selected controls reduce risk.

**Deliverables:**

• Python script

• Risk-control table

• Short explanation

# **Category C: Python-Based Complex Projects**

These projects are stronger capstones for students with more programming experience. They use CSV files, functions, dictionaries, sorting, generated reports, and simple analytics.

## **C1. Mini SOC Log Analyzer**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Complex Python | Medium-Advanced | Analyze fake login logs and identify suspicious accounts. |

**Objective: Analyze fake login logs and identify suspicious accounts.**

**Mathematical or analytical model: Suspicion Score \= failed-login points \+ unknown-location points \+ unusual-time points \+ password-reset points.**

**How to do it:**

1\. Create a CSV file with fake login activity.

2\. Write functions to score each row.

3\. Group scores by user.

4\. Sort users from highest to lowest suspicion.

5\. Write safe response recommendations.

**Deliverables:**

• CSV sample logs

• Python analyzer

• Ranked SOC-style report

## **C2. Cyber Hygiene Survey Analyzer**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Complex Python | Medium-Advanced | Analyze class cyber-safety survey results and find improvement priorit... |

**Objective: Analyze class cyber-safety survey results and find improvement priorities.**

**Mathematical or analytical model: Average category score \= total category points / number of students.**

**How to do it:**

1\. Create a fake or anonymous survey CSV.

2\. Calculate average scores for MFA, backups, screen lock, privacy, and updates.

3\. Identify the weakest category.

4\. Generate a short text report.

5\. Recommend class improvement actions.

**Deliverables:**

• CSV survey

• Python analyzer

• Text report

## **C3. Incident Report Generator**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Complex Python | Medium | Generate a structured incident report from user input. |

**Objective: Generate a structured incident report from user input.**

**Mathematical or analytical model: Structured data collection and formatted report generation.**

**How to do it:**

1\. Ask safe incident-report questions.

2\. Store answers in variables or a dictionary.

3\. Generate a formatted report.

4\. Save it as a text file.

5\. Explain why documentation matters.

**Deliverables:**

• Python script

• Generated incident report

• Reflection

## **C4. Access Control Role Checker**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Complex Python | Medium | Simulate school role-based access control and least privilege. |

**Objective: Simulate school role-based access control and least privilege.**

**Mathematical or analytical model: Decision logic: access allowed only if requested action is in the role permission set.**

**How to do it:**

1\. Define roles such as student, teacher, IT staff, and principal.

2\. Define allowed actions for each role.

3\. Ask for role and requested action.

4\. Return Access Allowed or Access Denied.

5\. Explain why least privilege reduces risk.

**Deliverables:**

• Python script

• Role-permission table

• Least privilege explanation

## **C5. Rule-Based Phishing Email Classifier**

| Category | Difficulty | Main Skill |
| :---- | :---- | :---- |
| Complex Python | Medium-Advanced | Classify fake email messages using keyword scoring and reason tracking... |

**Objective: Classify fake email messages using keyword scoring and reason tracking.**

**Mathematical or analytical model: Email Score \= sum(keyword points \+ link/sender warning points).**

**How to do it:**

1\. Create fake email examples.

2\. Create a keyword scoring dictionary.

3\. Write a function that returns score and reasons.

4\. Classify each email as probably safe, review, or likely phishing.

5\. Explain false positives and why human verification still matters.

**Deliverables:**

• Fake email dataset

• Python classifier

• Classification report

# **Suggested Capstone Grading Rubric**

| Criteria | Excellent | Good | Needs Improvement |
| :---- | :---- | :---- | :---- |
| Cybersecurity relevance | Clearly connects to course topics and defensive safety. | Mostly connected to cybersecurity concepts. | Connection is unclear or too generic. |
| Mathematical model | Formula/scoring model is clear and justified. | Formula is present but needs better explanation. | No clear measurable model. |
| Implementation | Works correctly and uses appropriate data safely. | Mostly works with minor issues. | Incomplete or unsafe data use. |
| Explanation | Student explains inputs, outputs, limitations, and safe actions. | Student explains most parts. | Explanation is unclear. |
| Presentation | Clear 5-7 minute demo with table/chart/output. | Understandable but could be better organized. | Hard to follow. |

# **Appendix: Sample Data Students Can Use**

Sample login log CSV:

time,user,location,event,result  
08:10,student01,School,login,success  
02:14,student01,Unknown,login,failed  
02:16,student01,Unknown,password\_reset,started  
23:45,student04,Unknown,login,failed  
23:46,student04,Unknown,login,failed

Sample survey CSV:

student,mfa,backup,screen\_lock,privacy,updates  
A,5,3,5,2,4  
B,2,1,4,1,3  
C,5,5,5,4,5  
D,3,2,3,2,2

# **Final Submission Checklist**

• Project title and problem statement

• Formula or scoring model

• Input data or sample data

• Output table, chart, report, or program result

• Safe recommendations

• Limitations of the model

• Short reflection on what the student learned