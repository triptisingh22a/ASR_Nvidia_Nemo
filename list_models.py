import nemo.collections.asr as nemo_asr

models = nemo_asr.models.EncDecCTCModel.list_available_models()
for m in models:
    print(m.pretrained_model_name)
