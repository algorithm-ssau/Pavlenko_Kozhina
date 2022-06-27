from typing import Dict
from main_dir.predictor import MorphoAnalysis
from main_dir.util.timer import timeit
from main_dir.test.evaluate import measure


@timeit
def tag(predictor: MorphoAnalysis, untagged_filename: str, tagged_filename: str):
    sentences = []
    with open(untagged_filename, "r", encoding='utf-8') as r:
        words = []
        for line in r:
            if line != "\n":
                records = line.strip().split("\t")
                word = records[1]
                words.append(word)
            else:
                sentences.append([word for word in words])
                words = []
    with open(tagged_filename, "w",  encoding='utf-8') as w:
        all_forms = predictor.predict_sentences(sentences)
        for forms in all_forms:
            for i, form in enumerate(forms):
                line = "{}\t{}\t{}\t{}\t{}\n".format(str(i + 1), form.word, form.normal, form.pos, form.tag)
                w.write(line)
            w.write("\n")


def tagged(predictor: MorphoAnalysis) -> Dict:
    tag(predictor, "main_dir/test/untagged.txt", "main_dir/test/output.txt")
    quality = dict()
    quality['Test'] = measure("main_dir/test/example.txt", "main_dir/test/output.txt", True, None)
    count_correct_pos = quality['Test'].correct_pos
    count_tags = quality['Test'].total_tags

    quality['All'] = dict()
    quality['All']['pos_accuracy'] = float(count_correct_pos) / count_tags
    return quality

