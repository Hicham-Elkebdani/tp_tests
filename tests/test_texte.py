import pytest
from app.texte import nettoyer_texte

@pytest.mark.parametrize("entree, attendu", [
    (" BONJOUR monde ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("PYTHON", "python")
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu

@pytest.mark.parametrize("valeur", [123, None])
def test_entree_invalide(valeur):
    with pytest.raises(TypeError):
        nettoyer_texte(valeur)

def test_nettoyage_idempotent():
    texte = "  BONJOUR   MONDE "
    resultat = nettoyer_texte(texte)
    assert nettoyer_texte(resultat) == resultat