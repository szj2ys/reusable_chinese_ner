# -*- coding: utf-8 -*-
import argparse
import sys
import traceback

from configs import settings, dirs
import random
import numpy as np
import os
from engines.train import train
from engines.data import DataManager
from engines.configure import Configure
from engines.utils.logger import logger
from engines.predict import Predictor


def set_env(settings):
    random.seed(settings.seed)
    np.random.seed(settings.seed)
    os.environ['CUDA_VISIBLE_DEVICES'] = settings.CUDA_VISIBLE_DEVICES


def show_data_summary(logger):
    logger.info('++' * 20 + 'CONFIGURATION SUMMARY' + '++' * 20)
    logger.info(' Status:')
    logger.info('     mode                 : {}'.format(settings.MODE))
    logger.info(' ' + '++' * 20)
    logger.info('     use              bert: {}'.format(settings.USE_BERT))
    logger.info('     use            bilstm: {}'.format(settings.USE_BILSTM))
    logger.info('     finetune             : {}'.format(settings.FINETUNE))
    logger.info(' ' + '++' * 20)
    logger.info('Model Configuration:')
    logger.info('     embedding         dim: {}'.format(
        settings.embedding_dim))
    logger.info('     max  sequence  length: {}'.format(
        settings.max_sequence_length))
    logger.info('     hidden            dim: {}'.format(settings.hidden_dim))
    logger.info('     seed                 : {}'.format(settings.seed))
    logger.info(' ' + '++' * 20)
    logger.info(' Training Settings:')
    logger.info('     epoch                : {}'.format(settings.epoch))
    logger.info('     batch            size: {}'.format(settings.batch_size))
    logger.info('     dropout              : {}'.format(settings.dropout))
    logger.info('     learning         rate: {}'.format(
        settings.learning_rate))
    logger.info('     optimizer            : {}'.format(settings.optimizer))
    logger.info('     checkpoint       name: {}'.format(
        settings.checkpoint_name))
    logger.info('     max       checkpoints: {}'.format(
        settings.checkpoints_max_to_keep))
    logger.info('     print       per_batch: {}'.format(
        settings.print_per_batch))
    logger.info('     is     early     stop: {}'.format(
        settings.IS_EARLY_STOP))
    logger.info('     patient              : {}'.format(settings.PATIENT))
    logger.info('++' * 20 + 'CONFIGURATION SUMMARY END' + '++' * 20)
    sys.stdout.flush()


if __name__ == "__main__1":
    show_data_summary(logger)
    dataManager = DataManager(logger)
    if settings.MODE == 'train':
        logger.info('mode: train')
        train(dataManager, logger)
    elif settings.MODE == 'infer':
        logger.info('mode: predict_one')
        predictor = Predictor(dataManager, logger)
        predictor.predict_one('warm start')
        while True:
            logger.info('please input a sentence (enter [exit] to exit.)')
            sentence = input()
            if sentence == 'exit':
                break
            results = predictor.predict_one(sentence)
            print(results)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tuning with BiLSTM+CRF')
    parser.add_argument('--config_file',
                        default='system.config',
                        help='Configuration File')
    args = parser.parse_args()

    # fold_check(configs)
    show_data_summary(logger)
    set_env(settings)
    mode = settings.mode.lower()
    dataManager = DataManager(settings, logger)
    if mode == 'train':
        logger.info('mode: train')
        train(settings, dataManager, logger)
    elif mode == 'interactive_predict':
        logger.info('mode: predict_one')
        predictor = Predictor(settings, dataManager, logger)
        predictor.predict_one('warm start')
        while True:
            logger.info('please input a sentence (enter [exit] to exit.)')
            sentence = input()
            if sentence == 'exit':
                break
            results = predictor.predict_one(sentence)
            print(results)
