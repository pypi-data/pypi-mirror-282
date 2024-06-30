#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : AppInsight                                                                          #
# Version    : 0.1.0                                                                               #
# Python     : 3.12.3                                                                              #
# Filename   : /profanity_check.py                                                                 #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john@variancexplained.com                                                           #
# URL        : https://github.com/variancexplained/explorify                                       #
# ------------------------------------------------------------------------------------------------ #
# Created    : Saturday June 29th 2024 01:12:31 pm                                                 #
# Modified   : Saturday June 29th 2024 01:23:28 pm                                                 #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2024 John James                                                                 #
# ================================================================================================ #
import pkg_resources
import numpy as np
import joblib

vectorizer = joblib.load(
    pkg_resources.resource_filename("profanity_check", "data/vectorizer.joblib")
)
model = joblib.load(
    pkg_resources.resource_filename("profanity_check", "data/model.joblib")
)


def _get_profane_prob(prob):
    return prob[1]


def predict(texts):
    return model.predict(vectorizer.transform(texts))


def predict_prob(texts):
    return np.apply_along_axis(
        _get_profane_prob, 1, model.predict_proba(vectorizer.transform(texts))
    )
