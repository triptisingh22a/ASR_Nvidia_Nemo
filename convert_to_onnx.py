# convert_to_onnx.py
import nemo.collections.asr as nemo_asr

# Load the pretrained Hindi ASR model
model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_hi_conformer_ctc_medium")

# Export to ONNX format
model.export(output_path="asr_model.onnx")
