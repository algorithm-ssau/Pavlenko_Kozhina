class ModelBuild(object):
    def __init__(self):
        self.char_dropout = 0.2
        self.char_embedding_dim = 24
        self.char_function_hidden_size = 500
        self.char_function_output_size = 200
        self.char_max_word_length = 32
        self.dense_dropout = 0.2
        self.dense_size = 128
        self.gram_dropout = 0.2
        self.gram_hidden_size = 30
        self.rnn_bidirectional = True
        self.rnn_dropout = 0.3
        self.rnn_hidden_size = 128
        self.rnn_input_size = 200
        self.rnn_n_layers = 2
        self.use_chars = True
        self.use_crf = False
        self.use_gram = True
        self.use_trained_char_embeddings = False
        self.use_word_embeddings = False
        self.word_embedding_dropout = 0.2
        self.word_max_count = 10000
        self.use_word_lm = False
        self.use_pos_lm = False
        self.char_model_config_path = None
        self.char_model_weights_path = None

        if self.use_word_lm:
            assert not self.use_word_embeddings


class TrainBuild(object):
    def __init__(self):
        self.dump_model_freq = 2
        self.epochs_num = 30
        self.external_batch_size = 5000
        self.batch_size = 256
        self.random_seed = 42
        self.rewrite_model = False
        self.sentence_len_groups = [[26, 50], [15, 25], [1, 14]]
        self.val_part = 0.05
        self.gram_dict_input = "information/gram_input.json"
        self.gram_dict_output = "information/gram_output.json"
        self.train_model_config_path = "information/model.json"
        self.train_model_weights_path = "information/model.h5"
        self.eval_model_config_path = "information/eval_model.json"
        self.eval_model_weights_path = "information/eval_model.h5"
        self.word_vocabulary = "information/vocabulary.txt"
        self.char_set_path = "information/char_set.txt"
        self.rewrite_model = True
