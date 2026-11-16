import pytest
from unittest.mock import patch
from app.surveillance import surveiller

def test_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)

        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")

def test_taux_normal():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)

        assert resultat == "ok"
        notifier.assert_not_called()

def test_taux_limite():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)

        assert resultat == "ok"
        notifier.assert_not_called()

def test_erreur_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Service indisponible")

        with pytest.raises(RuntimeError):
            surveiller(0.15)
