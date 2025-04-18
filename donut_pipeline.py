
from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import json

processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")

model.eval()

image_path = "data/prescription_01.jpg"
image = Image.open(image_path).convert("RGB")

prompt = "<s_docvqa><s_question>Extract structured fields from the prescription:</s_question><s_answer>"

pixel_values = processor(image, return_tensors="pt").pixel_values
decoder_input_ids = processor.tokenizer(prompt, add_special_tokens=False, return_tensors="pt")["input_ids"]

with torch.no_grad():
    outputs = model.generate(
        pixel_values,
        decoder_input_ids=decoder_input_ids,
        max_length=512,
        early_stopping=True,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
    )

output_text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
print("Extracted JSON:")
print(output_text)

with open("outputs/prescription_01_output.json", "w") as f:
    json.dump({"output": output_text}, f, indent=2)
