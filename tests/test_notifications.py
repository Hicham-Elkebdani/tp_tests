import pytest

from app.notifications import envoyer_notification


def test_service_notification_non_configure():
    with pytest.raises(RuntimeError, match="Service non configure"):
        envoyer_notification("Taux eleve")
