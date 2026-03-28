# Elective Project

This repository focuses on the integration of a CI/CD pipeline. It ensures that all code updates are automatically tested for syntax errors before being deployed.

## 👥 Project Members
* **Anthony Aries C. Andal**
* **Christine Racar**
* **Charles Halili (4B)**

## 📋 Project Requirements
* **CI/CD Integration**: Implementation of a functional automated pipeline.
* **Collaborative Environment**: Shared repository access for team updates.
* **Automated Testing**: Validation of code quality through syntax checks.
* **Deployment Guardrails**: Automatic rejection of invalid commits with error feedback.

## 🛠️ Technical Implementation
- **Workflow**: GitHub Actions (`syntax-check.yml`).
- **Linter Tools**: HTMLHint and JSHint for error detection.
- **Version Control**: Git-based workflow using VS Code.

## 🚦 How to Test
1. Make a change to the code in VS Code.
2. Commit and Push the changes to GitHub.
3. Monitor the **Actions** tab to see if the build passes (Green) or fails (Red).
