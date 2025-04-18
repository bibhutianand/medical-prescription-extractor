# medical-prescription-extractor
Pipeline to extract structured data from handwritten medical prescriptions using a multimodal LLM.
# Medical Prescription Extractor

This project builds a multimodal LLM pipeline (using Donut or Pix2Struct) to extract structured information from scanned handwritten medical prescriptions.

## 🔧 Tech Stack
- Python
- HuggingFace Transformers
- Donut or Pix2Struct
- PyTorch / TensorFlow

## 📁 Folder Structure

- `model/`: Model pipeline code
- `utils/`: Preprocessing utilities
- `data/`: Sample input images
- `outputs/`: Generated structured outputs
- `evaluation/`: Evaluation metrics and scripts

## 🧠 Model Used

Donut (OCR-free Vision+Language model for document parsing)

## 📊 Evaluation Strategy

- Field-level accuracy
- Manual validation
