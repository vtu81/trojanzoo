# -*- coding: utf-8 -*-

from .attack import Attack
from .adv import *
from .poison import *
from .backdoor import *
from .other import *

class_dict = {
    'attack': 'Attack',

    'pgd': 'PGD',
    'inference': 'Inference',

    'poison': 'Poison',

    'badnet': 'BadNet',
    'trojannn': 'TrojanNN',
    'hidden_trigger': 'Hidden_Trigger',
    'latent_backdoor': 'Latent_Backdoor',
    'clean_label': 'Clean_Label',
    
    'unify': 'Unify',
}
