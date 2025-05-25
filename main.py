from fastapi import FastAPI, File, UploadFile, HTTPException
import nemo.collections.asr as nemo_asr
import torchaudio
import tempfile
import os
import torch

app = FastAPI()

# Load model locally (download 'stt_hi_conformer_ctc_medium.nemo' and place in ./models folder)
model_path = "models/stt_hi_conformer_ctc_medium.nemo"
asr_model = nemo_asr.models.EncDecCTCModel.restore_from(model_path)


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".wav", ".flac", ".mp3", ".m4a", ".ogg")):
        raise HTTPException(status_code=400, detail="Unsupported audio format")

    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp_file_path = tmp.name
        content = await file.read()
        tmp.write(content)

    try:
        # Load audio with torchaudio
        audio, sr = torchaudio.load(tmp_file_path)
        
        # Convert to mono if needed
        if audio.shape[0] > 1:
            audio = torch.mean(audio, dim=0, keepdim=True)
        
        # Resample to 16kHz if needed
        if sr != 16000:
            resampler = torchaudio.transforms.Resample(sr, 16000)
            audio = resampler(audio)

        # Transcribe using model (expects list of audio tensors)
        transcription = asr_model.transcribe([audio.squeeze(0)])[0]

        return {"transcript": transcription}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription error: {str(e)}")

    finally:
        # Clean up temp file
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)
