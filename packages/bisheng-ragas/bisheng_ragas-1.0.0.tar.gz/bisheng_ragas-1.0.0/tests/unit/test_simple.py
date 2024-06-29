from __future__ import annotations

import typing as t


def test_import():
    import bisheng_ragas
    from bisheng_ragas.testset.testset_generator import TestsetGenerator

    assert TestsetGenerator is not None
    assert bisheng_ragas is not None


def test_type_casting():
    t.cast(t.List[int], [1, 2, 3])


def test_import_metrics():
    from bisheng_ragas.metrics.critique import harmfulness

    assert harmfulness is not None
