# -*- coding: utf-8 -*-

from ..defense import Parser_Defense


class Parser_Grad_Train(Parser_Defense):
    r"""Grad Train Parser

    Attributes:
        name (str): ``'defense'``
        defense (str): The specific defense name (lower-case).
    """
    name: str = 'defense'
    defense = 'grad_train'

    @classmethod
    def add_argument(cls, parser):
        super().add_argument(parser)

        parser.add_argument('--pgd_alpha', dest='pgd_alpha', type=float)
        parser.add_argument('--pgd_epsilon', dest='pgd_epsilon', type=float)
        parser.add_argument('--pgd_iteration', dest='pgd_iteration', type=int)
