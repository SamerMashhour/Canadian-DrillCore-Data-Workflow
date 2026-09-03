from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def leave_one_group_out_splits(df: pd.DataFrame, group_col: str):
    """Yield deterministic whole-group train/test indices."""
    groups = list(dict.fromkeys(df[group_col].tolist()))
    for g in groups:
        test = df.index[df[group_col] == g].to_numpy()
        train = df.index[df[group_col] != g].to_numpy()
        yield g, train, test


def fixed_models(random_state=42):
    """Return the deliberately untuned baseline models used by the frozen v0.4 benchmark."""
    return {
        "dummy_prior": DummyClassifier(strategy="prior", random_state=random_state),
        "logistic_balanced": Pipeline([
            ("scale", StandardScaler()),
            ("model", LogisticRegression(
                C=1.0,
                class_weight="balanced",
                solver="lbfgs",
                max_iter=2000,
                random_state=random_state,
            )),
        ]),
        "random_forest_balanced": RandomForestClassifier(
            n_estimators=500,
            max_depth=4,
            min_samples_leaf=2,
            max_features="sqrt",
            class_weight="balanced",
            random_state=random_state,
            n_jobs=1,
        ),
    }


def evaluate_whole_group_baselines(df, feature_cols, label_col, group_col, random_state=42):
    """Evaluate fixed baselines using leave-one-whole-group-out validation."""
    results = []
    for model_name, model in fixed_models(random_state).items():
        fold_scores = []
        for held_out, train_idx, test_idx in leave_one_group_out_splits(df, group_col):
            X_train = df.loc[train_idx, feature_cols]
            y_train = df.loc[train_idx, label_col]
            X_test = df.loc[test_idx, feature_cols]
            y_test = df.loc[test_idx, label_col]
            model.fit(X_train, y_train)
            pred = model.predict(X_test)
            fold_scores.append({
                "held_out_group": held_out,
                "balanced_accuracy": balanced_accuracy_score(y_test, pred),
                "macro_f1": f1_score(y_test, pred, average="macro", zero_division=0),
            })
        results.append({
            "model": model_name,
            "mean_fold_balanced_accuracy": float(np.mean([x["balanced_accuracy"] for x in fold_scores])),
            "mean_fold_macro_f1": float(np.mean([x["macro_f1"] for x in fold_scores])),
            "folds": fold_scores,
        })
    return results
