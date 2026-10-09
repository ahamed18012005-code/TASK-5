# PhishAware — Project Methodology

## 1. Objective

To demonstrate basic phishing-indicator detection and document a simulated incident response workflow using Python.

## 2. Environment

* Python 3
* Kali Linux or another Python-compatible operating system
* GitHub for source code and documentation
* A fictional email stored in a text file

## 3. Procedure

### Step 1: Prepare the Sample

Create `samples/mock_phishing_email.txt` containing a fictional email with predefined test indicators.

### Step 2: Run the Detector

Execute:

```bash
python phishing_detector.py
```

The program reads the sample and checks for:

* Urgent or threatening language
* Account verification phrases
* HTTP or HTTPS URL prefixes

Record the actual terminal output if screenshots or evidence are required.

### Step 3: Run the Incident Response Simulation

Execute:

```bash
python incident_response.py
```

The script prints six incident response stages and writes a timestamped log to `evidence/incident-response-log.txt`.

### Step 4: Review the Evidence

Check that the generated log contains the timestamp, all six stages, and the simulation completion messages.

### Step 5: Document Findings

Record the actual observations, limitations, and recommended security measures in the project documentation and final report.

## 4. Expected Observations

The provided sample contains the configured urgency terms, account verification language, and an HTTPS URL. Therefore, the detector is expected to report three categories of indicators.

The incident response script is expected to print six stages and create the evidence log.

These are expected results; verify them by running the scripts before reporting them as observed outcomes.

## 5. Limitations

* Detection uses predefined text matching.
* URL detection does not determine whether a URL is safe or malicious.
* Sender authenticity is not verified.
* No real containment, eradication, or recovery operations are performed.
* The simulation does not replace professional incident response procedures.

## 6. Ethical Considerations

Only fictional sample content is used. The project does not require real credentials, access to third-party systems, or delivery of phishing emails.
