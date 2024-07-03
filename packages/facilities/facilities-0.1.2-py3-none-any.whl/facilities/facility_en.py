from transformers import MarianMTModel, MarianTokenizer

def translate(text, src_lang="cs", target_lang="en"):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{target_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    # Generate translation
    translated = model.generate(**inputs)
    # Decode the translated tokens
    translation = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return translation[0]

print(translate("dům", 'cs', 'en'))
