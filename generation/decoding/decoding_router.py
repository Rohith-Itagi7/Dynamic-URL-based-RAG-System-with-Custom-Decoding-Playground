# generation/decoding/decoding_router.py

def decode(model, tokenizer, prompt, params):

    inputs = tokenizer(prompt, return_tensors="pt")

    strategy = params["strategy"]

    if strategy == "greedy":
        output_ids = model.generate(
            **inputs,
            max_new_tokens=params["max_tokens"],
            do_sample=False
        )

    elif strategy == "beam":
        output_ids = model.generate(
            **inputs,
            max_new_tokens=params["max_tokens"],
            num_beams=params["num_beams"],
            early_stopping=True,
            do_sample=False
        )

    elif strategy == "top_k":
        output_ids = model.generate(
            **inputs,
            max_new_tokens=params["max_tokens"],
            do_sample=True,
            temperature=params["temperature"],
            top_k=params["top_k"],
            repetition_penalty=params["repetition_penalty"]
        )

    elif strategy == "top_p":
        output_ids = model.generate(
            **inputs,
            max_new_tokens=params["max_tokens"],
            do_sample=True,
            temperature=params["temperature"],
            top_p=params["top_p"],
            repetition_penalty=params["repetition_penalty"]
        )

    else:
        raise ValueError("Invalid decoding strategy")

    return output_ids
