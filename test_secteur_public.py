from secteur_public import SecteurPublic
import pytest
import pandas as pd
import re


@pytest.mark.parametrize(
    'kwargs, erreur, message_erreur',
    [
        ({'categorie': 12}, TypeError,
         "La catégorie doit être une chaîne de caractères."),
        ({'categorie': ['Dupont']}, TypeError,
         "La catégorie doit être une chaîne de caractères."),
        ({'categorie': "Pieton"}, TypeError,
         "La catégorie doit valoir foot, cycle ou car."),

    ]
)
def test_secteur_public_init_echec(pompe_e85_kwargs,  kwargs, erreur,
                                   message_erreur):
    pompe_e85_kwargs.update(kwargs)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        SecteurPublic(**pompe_e85_kwargs)
