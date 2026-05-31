import os
import random
import pandas as pd
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

random.seed(42)

# =====================================================
# AUTHORITIES
# =====================================================

authorities = [
    ["A001", "Rajesh Kumar", "Executive Engineer", "NHAI", "rajesh.kumar@nhai.gov.in", "9876543210"],
    ["A002", "Priya Sharma", "Assistant Engineer", "Tamil Nadu Highways", "priya.sharma@tn.gov.in", "9876543211"],
    ["A003", "Arun Prakash", "Executive Engineer", "Greater Chennai Corporation", "arun.prakash@gcc.gov.in", "9876543212"],
    ["A004", "Vijay Narayanan", "Regional Officer", "NHAI", "vijay.n@nhai.gov.in", "9876543213"],
    ["A005", "Suresh Babu", "Chief Engineer", "Tamil Nadu Highways", "suresh.babu@tn.gov.in", "9876543214"]
]

pd.DataFrame(
    authorities,
    columns=[
        "authority_id",
        "authority_name",
        "designation",
        "department",
        "email",
        "phone"
    ]
).to_csv(os.path.join(DATA_DIR, "authorities.csv"), index=False)

# =====================================================
# CONTRACTORS
# =====================================================

contractors = [
    ["C001", "ABC Infra", "contact@abcinfra.com", "9123456780", 4.5],
    ["C002", "South Roads Pvt Ltd", "info@southroads.com", "9123456781", 4.3],
    ["C003", "Tamil Infra Works", "admin@tamilinfra.com", "9123456782", 4.1],
    ["C004", "Urban BuildTech", "support@urbanbuildtech.com", "9123456783", 4.7],
    ["C005", "National Road Projects", "contact@nrp.com", "9123456784", 4.2]
]

pd.DataFrame(
    contractors,
    columns=[
        "contractor_id",
        "contractor_name",
        "email",
        "phone",
        "rating"
    ]
).to_csv(os.path.join(DATA_DIR, "contractors.csv"), index=False)

# =====================================================
# ROADS
# =====================================================

road_templates = [
    ("OMR", "NH", 12.9121, 80.2279),
    ("ECR", "SH", 12.9568, 80.2540),
    ("GST Road", "NH", 12.9850, 80.1870),
    ("Anna Salai", "City Road", 13.0604, 80.2735),
    ("Mount Road", "City Road", 13.0569, 80.2747),
    ("Poonamallee High Road", "NH", 13.0827, 80.2707),
    ("Velachery Main Road", "City Road", 12.9784, 80.2215),
    ("Rajiv Gandhi Salai", "NH", 12.9140, 80.2295),
    ("Arcot Road", "SH", 13.0521, 80.2020),
    ("100 Feet Road", "City Road", 13.0418, 80.2201)
]

roads = []

for i in range(1, 101):

    road = road_templates[(i - 1) % len(road_templates)]

    roads.append([
        f"R{i:03d}",
        road[0],
        road[1],
        "Chennai",
        "Tamil Nadu",
        round(road[2] + random.uniform(-0.005, 0.005), 6),
        round(road[3] + random.uniform(-0.005, 0.005), 6),
        random.choice(["Good", "Fair", "Poor"]),
        (
            datetime.now()
            - timedelta(days=random.randint(30, 365))
        ).strftime("%Y-%m-%d"),
        f"C{random.randint(1,5):03d}",
        f"A{random.randint(1,5):03d}",
        f"B{i:03d}"
    ])

pd.DataFrame(
    roads,
    columns=[
        "road_id",
        "road_name",
        "road_type",
        "city",
        "state",
        "latitude",
        "longitude",
        "condition",
        "last_repair_date",
        "contractor_id",
        "authority_id",
        "budget_id"
    ]
).to_csv(os.path.join(DATA_DIR, "roads.csv"), index=False)

# =====================================================
# BUDGETS
# =====================================================

budgets = []

for i in range(1, 101):

    allocated = random.randint(
        5_000_000,
        25_000_000
    )

    spent = random.randint(
        int(allocated * 0.5),
        allocated
    )

    budgets.append([
        f"B{i:03d}",
        f"R{i:03d}",
        allocated,
        spent,
        "2025-26"
    ])

pd.DataFrame(
    budgets,
    columns=[
        "budget_id",
        "road_id",
        "allocated_budget",
        "spent_budget",
        "financial_year"
    ]
).to_csv(os.path.join(DATA_DIR, "budgets.csv"), index=False)

# =====================================================
# COMPLAINTS
# =====================================================

issue_types = [
    "Pothole",
    "Waterlogging",
    "Road Crack",
    "Road Damage",
    "Streetlight Failure"
]

complaints = []

for i in range(1, 151):

    complaints.append([
        f"CMP{i:03d}",
        f"R{random.randint(1,100):03d}",
        random.choice(issue_types),
        "Citizen reported issue",
        random.choice([
            "Open",
            "In Progress",
            "Resolved"
        ]),
        (
            datetime.now()
            - timedelta(days=random.randint(1, 90))
        ).strftime("%Y-%m-%d")
    ])

pd.DataFrame(
    complaints,
    columns=[
        "complaint_id",
        "road_id",
        "issue_type",
        "description",
        "status",
        "created_at"
    ]
).to_csv(os.path.join(DATA_DIR, "complaints.csv"), index=False)

print("Dataset generated successfully.")
print("Files:")
print("roads.csv")
print("authorities.csv")
print("contractors.csv")
print("budgets.csv")
print("complaints.csv")