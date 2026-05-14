"""
Evaluation harness stub.

TODO: Implement this.

Run your classifier across all 18 sessions, compare against the 5 labeled
sessions, and report your chosen metrics.
"""

from loader import load_all_sessions, load_labels
from classify import classify_session


def evaluate():
    sessions = load_all_sessions()
    labels = load_labels()

    results = []
    for session in sessions:
        result = classify_session(session)
        results.append(result)

    # TODO: Compare results against labels.
    # TODO: Compute your chosen metrics.
    # TODO: Print a results table and metric summary.

    print("Session            | Predicted       | Confidence | Ground Truth")
    print("-------------------+-----------------+------------+-------------")
    for r in results:
        gt = labels.get(r["session_id"], "—")
        print(f"{r['session_id']:18} | {r['label']:15} | {r['confidence']:10} | {gt}")


if __name__ == "__main__":
    evaluate()
