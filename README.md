# medical-prescription-extractor
Pipeline to extract structured data from handwritten medical prescriptions using a multimodal LLM.
# 🧠 Medical Prescription Extractor

A pipeline that uses a multimodal large language model (Donut) to extract structured data from scanned handwritten medical prescriptions.

---

## 📌 Objective

To extract key fields like patient name, date, doctor info, medicines, dosage, frequency, and instructions from handwritten prescriptions using open-source multimodal LLMs.

---

## 📊 Dataset

- **Name:** Medical Prescription Images Dataset
- **Description:** Scanned images of handwritten medical prescriptions
- **Sample Image Used:** `prescription_01.jpg`

---

## 🔍 Model & Pipeline

I used the `Donut` model (`naver-clova-ix/donut-base-finetuned-docvqa`) for its ability to perform document visual QA and structured extraction.

### Steps:
1. Load and preprocess the scanned image
2. Use a prompt to guide Donut to extract structured data
3. Parse and store the generated JSON output

### Folder Structure:
medical-prescription-extractor/
│
├── model/
│   └── donut_pipeline.py          
│
├── evaluation/
│   └── evaluate.py                # Code to evaluate the model
│
├── README.md                      
├── presentation.pdf               
└── requirements.txt 

## ✅ Sample Output (JSON)

```json
{
  "patient_name": "Aarav",
  "date": "13/11/19",
  "doctor_name": "Dr. Sanjeev Kumar Sharma",
  "medications": [
    {
      "name": "Cef",
      "dosage": "92.5mg",
      "frequency": "1/2 tsp",
      "duration": "6 hours"
    },
    ...
  ],
  "note": "Nebul. On advice of dr. Doscor – oral syrup"
}
