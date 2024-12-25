# selenium-week5-framework

## Week 5: Hybrid Automation Framework Development

This repository contains my work for Week 5 of the Python Selenium Learning Journey. The focus was on developing a Hybrid Automation Framework combining Data-Driven and Keyword-Driven approaches, with an emphasis on modularity, reusability, and scalability.

---

### Key Tasks and Highlights

#### Task 1: Hybrid Framework Setup
- **Goal**: Design the basic structure of the Hybrid Framework.
- **Implementation**:
  - Created directories for `test cases`, `keywords`, `test data`, `config`, and `reports`.
  - Initialized `config.json` for environment variables and framework settings.
  - Added reusable modules for logging and configuration management.

#### Task 2: Integrate Keyword-Driven Logic
- **Goal**: Develop keyword functions to interact with web elements.
- **Implementation**:
  - Implemented actions like `click_element`, `input_text`, and `verify_text` as independent keywords.
  - Used a mapping system to associate test steps with corresponding keywords.

#### Task 3: Parameterized Data Handling
- **Goal**: Enable test scripts to read test steps and data from external files.
- **Implementation**:
  - Loaded test cases from Excel and JSON files using `openpyxl` and `json` libraries.
  - Ensured smooth integration with the Hybrid Framework.

#### Task 4: Reporting and Logs
- **Goal**: Generate detailed HTML reports and logs.
- **Implementation**:
  - Configured `pytest-html` for customized reports saved in the `reports` folder.
  - Added Python logging for debugging and test tracking.

#### Task 5: End-to-End Framework Validation
- **Goal**: Test framework efficiency by automating a complex login workflow.
- **Implementation**:
  - Automated login for multiple users using parameterized test cases.
  - Validated successful logins and error messages for invalid credentials.

---

### Technologies Used
- **Python**: Core scripting language.
- **Selenium WebDriver**: Web automation tool.
- **pytest**: Test runner for parameterized testing.
- **openpyxl**: Excel data handling.
- **json**: Configuration and test data storage.
- **pytest-html**: HTML reporting.
- **Logger**: Logging test execution details.

---

### How to Run the Framework
1. **Clone the Repository**:
   ```bash
   git clone <repository-link>
   cd selenium-week5-hybrid-framework
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Framework**:
   - Update the `config.json` file with browser, URL, and other settings.

4. **Run Tests**:
   ```bash
   pytest --html=reports/report.html
   ```

---

### Key Learnings
- Building a modular and reusable Hybrid Automation Framework.
- Efficiently combining Data-Driven and Keyword-Driven testing.
- Advanced usage of pytest, including parameterization and custom reporting.
- Implementing robust logging and error handling for scalable automation.

---

### Future Enhancements
- Add cross-browser testing capabilities.
- Integrate the framework with CI/CD tools like Jenkins.
- Expand keyword libraries for complex scenarios.

---