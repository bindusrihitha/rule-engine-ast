# Rule Engine with AST

## Overview
This project implements a simple 3-tier rule engine application that determines user eligibility based on attributes such as age, department, income, and experience. The system uses an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic creation, combination, and modification of these rules.

## Features
- **Rule Creation:** Define rules using a simple syntax.
- **Rule Combination:** Combine multiple rules into a single AST for efficient evaluation.
- **Rule Evaluation:** Evaluate rules against user data to determine eligibility.
- **Error Handling:** Robust error handling for invalid rule strings and data formats.
- **Data Storage:** Store rules and metadata in a SQLite database.

## Technologies Used
- Python
- Flask (for API and backend)
- SQLite (for data storage)
- JSON (for data interchange)

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github
