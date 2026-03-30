from sklearn.dummy import DummyClassifier


def build_baseline_model(strategy: str = "most_frequent") -> DummyClassifier:
    return DummyClassifier(strategy=strategy)
