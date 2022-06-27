from main_dir.tag import tagged
from main_dir.predictor import MorphoAnalysis
import plotly.graph_objects as go
from collections import Counter

morph = MorphoAnalysis()

arrays = tagged(morph)

noun_agree, verb_agree, adj_agree, adv_agree, num_agree, pron_agree = [], [], [], [], [], []
noun_fail, verb_fail, adj_fail, adv_fail, num_fail, pron_fail = [], [], [], [], [], []

file = open("main_dir/test/agree.txt", "r", encoding="UTF-8")
for i in file:
    array = []
    del_n = i.split("\n")
    separator = del_n[0].split(":")
    array.append(separator[0])
    word = morph.predict(array)
    word1 = word[0].normal
    if separator[1] == "NOUN":
        noun_agree.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "VERB":
        verb_agree.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "ADJ":
        adj_agree.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "ADV":
        adv_agree.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "NUM":
        num_agree.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "PRON":
        pron_agree.append(word[0].normal + " " + str(separator[2]))
file.close()

file = open("main_dir/test/failed.txt", "r", encoding="UTF-8")
for i in file:
    array = []
    del_n = i.split("\n")
    separator = del_n[0].split(":")
    array.append(separator[0])
    word = morph.predict(array)
    word1 = word[0].normal
    if separator[1] == "NOUN":
        noun_fail.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "VERB":
        verb_fail.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "ADJ":
        adj_fail.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "ADV":
        adv_fail.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "NUM":
        num_fail.append(word[0].normal + " " + str(separator[2]))
    if separator[1] == "PRON":
        pron_fail.append(word[0].normal + " " + str(separator[2]))
file.close()

noun_agree = Counter(noun_agree).most_common()
verb_agree = Counter(verb_agree).most_common()
adj_agree = Counter(adj_agree).most_common()
adv_agree = Counter(adv_agree).most_common()
num_agree = Counter(num_agree).most_common()
pron_agree = Counter(pron_agree).most_common()
noun_fail = Counter(noun_fail).most_common()
verb_fail = Counter(verb_fail).most_common()
adj_fail = Counter(adj_fail).most_common()
adv_fail = Counter(adv_fail).most_common()
num_fail = Counter(num_fail).most_common()
pron_fail = Counter(pron_fail).most_common()


def add_space(morph):
    array = []
    for i in morph:
        array.append(str(i[0]) + " " + str(i[1]))
    return array


noun_agree = add_space(noun_agree)
verb_agree = add_space(verb_agree)
adj_agree = add_space(adj_agree)
adv_agree = add_space(adv_agree)
num_agree = add_space(num_agree)
pron_agree = add_space(pron_agree)
noun_fail = add_space(noun_fail)
verb_fail = add_space(verb_fail)
adj_fail = add_space(adj_fail)
adv_fail = add_space(adv_fail)
num_fail = add_space(num_fail)
pron_fail = add_space(pron_fail)

fig1 = go.Figure(data=[go.Table(header=dict(values=["NOUN", "VERB", "ADJ", "ADV", "NUM", "PRON"]),
                                cells=dict(values=[noun_agree, verb_agree, adj_agree, adv_agree, num_agree, pron_agree]))])
fig1.update_layout(title_text="Верный морфологический разбор")

fig1.show()

fig2 = go.Figure(data=[go.Table(header=dict(values=["NOUN", "VERB", "ADJ", "ADV", "NUM", "PRON"]),
                                cells=dict(values=[noun_fail, verb_fail, adj_fail, adv_fail, num_fail, pron_fail]))])
fig2.update_layout(title_text="Ошибка при морфологическом разборе")
fig2.show()

