#!/usr/bin/env python

from datetime import date
from dataclasses import dataclass
from compass_lib.shot import SurveyShot


@dataclass
class SurveySection:
    cave_name: str
    survey_name: str
    date: date
    comment: str
    surveyors: list[str]
    declination: float
    format: str
    correction: tuple[float, float, float]
    shots: list[SurveyShot]
