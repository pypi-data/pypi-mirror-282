from datasets import load_dataset

from bisheng_ragas import evaluate
from bisheng_ragas.metrics import answer_relevancy, context_precision, faithfulness
from bisheng_ragas.metrics.critique import harmfulness


def test_evaluate_e2e():
    ds = load_dataset("explodinggradients/fiqa", "ragas_eval")["baseline"]
    result = evaluate(
        ds.select(range(3)),
        metrics=[answer_relevancy, context_precision, faithfulness, harmfulness],
    )
    assert result is not None
