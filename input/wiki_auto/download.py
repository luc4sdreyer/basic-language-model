from datasets import load_dataset, concatenate_datasets

# references:
# https://huggingface.co/docs/datasets/process
# https://huggingface.co/datasets/wiki_auto

# load the dataset
dataset_parts = load_dataset('wiki_auto')

# combine parts
dataset = concatenate_datasets([dataset_parts["part_1"], dataset_parts["part_2"]])

# remove extra columns
sentence_ds_parts = dataset.map(
    lambda x: {"sentence": x["simple"]["simple_article_content"]["simple_sentence"]},
    remove_columns=["simple", "paragraph_alignment", "sentence_alignment", "example_id", "normal"])

# cast to ascii
sentence_ds_ascii = sentence_ds_parts.map(
    lambda x: {"article": " ".join([line.encode("ascii", "ignore") for line in x["sentence"]])},
    remove_columns=["sentence"])

# save
sentence_ds_ascii.to_json("./basic_english.json")

# split_ds = sentence_ds_ascii.train_test_split(test_size=0.1)
