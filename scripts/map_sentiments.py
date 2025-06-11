import torch


def map_sentiment(rating):
    if rating in [1, 2]:
        return "Negative"
    elif rating == 3:
        return "Neutral"
    elif rating in [4, 5]:
        return "Positive"
    else:
        return None


def predict_sentiment(texts, model, tokenizer, device="cpu", batch_size=16):
    model.eval()
    results = []
    with torch.no_grad():
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i : i + batch_size]
            inputs = tokenizer(
                [f"sentiment: {t}" for t in batch_texts],
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=128,
            ).to(device)
            outputs = model.generate(**inputs, max_length=10)
            decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)
            results.extend(decoded)
    return results
