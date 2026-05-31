# RoadWatch Dataset Repository

Dataset repository for the **RoadWatch AI** project developed for the **National Road Safety Hackathon 2026 (IIT Madras)**.

This repository contains the structured datasets used by the backend services for road information retrieval, infrastructure transparency, budget tracking, authority lookup, contractor mapping, and complaint management.

---

## Repository Structure

```text
roadwatch-dataset/

├── data/
│   ├── roads.csv
│   ├── authorities.csv
│   ├── contractors.csv
│   ├── budgets.csv
│   └── complaints.csv
│
├── generators/
│   └── generate_all.py
│
├── schema.md
├── requirements.txt
└── README.md
```

---

## Purpose

The dataset is designed to support the following RoadWatch AI features:

* Road Information Lookup
* Infrastructure Transparency
* Authority Identification
* Contractor Mapping
* Budget Monitoring
* Complaint Tracking
* AI-powered Citizen Assistance

The generated data follows realistic road infrastructure management workflows and is intended for demonstration, testing, and prototype development purposes.

---

## Dataset Files

### roads.csv

Contains road-level information.

| Column           | Description             |
| ---------------- | ----------------------- |
| road_id          | Unique road identifier  |
| road_name        | Road name               |
| road_type        | Road category           |
| city             | City name               |
| state            | State name              |
| latitude         | Geographic latitude     |
| longitude        | Geographic longitude    |
| condition        | Current road condition  |
| last_repair_date | Most recent repair date |
| contractor_id    | Assigned contractor     |
| authority_id     | Responsible authority   |
| budget_id        | Linked budget record    |

---

### authorities.csv

Contains government authority information.

| Column         | Description                 |
| -------------- | --------------------------- |
| authority_id   | Unique authority identifier |
| authority_name | Authority officer name      |
| designation    | Official designation        |
| department     | Department name             |
| email          | Contact email               |
| phone          | Contact number              |

---

### contractors.csv

Contains contractor details.

| Column          | Description                  |
| --------------- | ---------------------------- |
| contractor_id   | Unique contractor identifier |
| contractor_name | Contractor company name      |
| email           | Contact email                |
| phone           | Contact number               |
| rating          | Performance rating           |

---

### budgets.csv

Contains budget allocation information.

| Column           | Description              |
| ---------------- | ------------------------ |
| budget_id        | Unique budget identifier |
| road_id          | Linked road              |
| allocated_budget | Allocated amount         |
| spent_budget     | Amount spent             |
| financial_year   | Financial year           |

---

### complaints.csv

Contains citizen complaint records.

| Column       | Description                 |
| ------------ | --------------------------- |
| complaint_id | Unique complaint identifier |
| road_id      | Related road                |
| issue_type   | Complaint category          |
| description  | Complaint description       |
| status       | Current status              |
| created_at   | Date of creation            |

---

## Data Generation

The repository includes an automated dataset generation script.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Dataset

```bash
python generators/generate_all.py
```

Generated CSV files will be placed inside:

```text
data/
```

---

## Data Relationships

```text
Road
 ├── Authority
 ├── Contractor
 ├── Budget
 └── Complaints
```

Relationship Mapping:

```text
roads.authority_id  -> authorities.authority_id
roads.contractor_id -> contractors.contractor_id
roads.budget_id     -> budgets.budget_id

budgets.road_id     -> roads.road_id
complaints.road_id  -> roads.road_id
```

---

## Usage

These datasets are intended to be consumed by:

* FastAPI Backend
* SQLite Database Seeder
* AI Context Retrieval Layer
* Dashboard Analytics Module
* Complaint Management Module

---

## Technology Stack

* Python
* Pandas
* CSV
* SQLite

---

## Notes

* Data is generated for prototype and hackathon demonstration purposes.
* Dataset structure is fixed and should remain consistent with the backend API contract.
* Any schema changes should be coordinated across frontend, backend, AI, and dataset repositories before implementation.

---

## RoadWatch AI

National Road Safety Hackathon 2026

Theme: AI in Road Safety

Problem Statement: RoadWatch
