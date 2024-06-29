import bisheng_ragas.metrics
import bisheng_ragas.metrics.critique

test_metrics = [
    "answer_correctness",
    "answer_relevancy",
    "answer_similarity",
    "context_recall",
    "context_precision",
    "context_relevancy",
    "faithfulness",
]

test_critique = [
    "harmfulness",
    "maliciousness",
    "coherence",
    "correctness",
    "conciseness",
]


def test_import_module():
    assert bisheng_ragas.metrics is not None, "module is not imported"

    for metric in test_metrics:
        assert hasattr(bisheng_ragas.metrics, metric)

    for metric in test_critique:
        assert hasattr(bisheng_ragas.metrics.critique, metric)
