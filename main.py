import os
from main_dir.model import LSTMAnalysis
from main_dir.config import ModelBuild, TrainBuild


file_names = ["train.txt"]

train_config = TrainBuild()
build_config = ModelBuild()
model = LSTMAnalysis()
model.prepare(train_config.gram_dict_input, train_config.gram_dict_output,
              train_config.word_vocabulary, train_config.char_set_path, file_names)

if os.path.exists(train_config.eval_model_config_path) and not train_config.rewrite_model:
    model.load_train(build_config, train_config.train_model_config_path, train_config.train_model_weights_path)
    print(model.eval_model.summary())
else:
    model.build(build_config)
model.train(file_names, train_config, build_config)
