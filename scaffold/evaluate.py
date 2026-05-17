"""
Evaluation harness.

Runs the classifier across all 18 sessions, compares against the 5 labeled
sessions, and reports metrics that prioritize the high cost of false accusations.
"""

from loader import load_all_sessions, load_labels
from classify import classify_session


def evaluate():
    sessions = load_all_sessions()
    labels = load_labels()

    results = []
    print("Classifying sessions... this may take a minute.")
    for i, session in enumerate(sessions):
        print(f"Processing {session['session_id']} ({i+1}/{len(sessions)})...")
        result = classify_session(session)
        results.append(result)

    # Compute metrics on labeled sessions only
    labeled_results = [r for r in results if r["session_id"] in labels]
    
    total_labeled = len(labeled_results)
    correct = 0
    false_accusations = 0  # organic labeled as cheating
    missed_cheaters = 0    # cheating labeled as organic
    
    for r in labeled_results:
        sid = r["session_id"]
        pred = r["label"]
        gt = labels[sid]
        
        if pred == gt:
            correct += 1
        else:
            if gt == "organic" and pred in ["pasted", "ai_generated"]:
                false_accusations += 1
            elif gt in ["pasted", "ai_generated"] and pred == "organic":
                missed_cheaters += 1

    accuracy = correct / total_labeled if total_labeled > 0 else 0
    
    organic_count = sum(1 for sid, gt in labels.items() if gt == "organic")
    cheater_count = total_labeled - organic_count
    
    false_accusation_rate = false_accusations / organic_count if organic_count > 0 else 0
    missed_cheater_rate = missed_cheaters / cheater_count if cheater_count > 0 else 0

    print("\n" + "="*80)
    print("EVALUATION METRICS (On Labeled Subset)")
    print("="*80)
    print(f"Overall Accuracy      : {accuracy*100:.1f}% ({correct}/{total_labeled})")
    print(f"False Accusation Rate : {false_accusation_rate*100:.1f}% ({false_accusations}/{organic_count} honest candidates flagged)")
    print(f"Missed Cheater Rate   : {missed_cheater_rate*100:.1f}% ({missed_cheaters}/{cheater_count} cheaters missed)")
    
    print("\nNote: Falsely accusing an honest candidate is far more damaging than missing a")
    print("cheater. The False Accusation Rate should ideally be 0%.\n")

    print("="*120)
    print(f"{'Session':<15} | {'Predicted':<15} | {'Confidence':<10} | {'Ground Truth':<15} | {'Reason'}")
    print("-" * 120)
    for r in results:
        gt = labels.get(r["session_id"], "—")
        pred = r['label']
        marker = ""
        if gt != "—":
            if pred == gt:
                marker = "✅ "
            elif gt == "organic" and pred in ["pasted", "ai_generated"]:
                marker = "🚨 " # False accusation
            else:
                marker = "❌ "
                
        reason = r['reason']
        if len(reason) > 50:
            reason = reason[:47] + "..."
            
        print(f"{r['session_id']:<15} | {marker}{pred:<13} | {r['confidence']:<10} | {gt:<15} | {reason}")


if __name__ == "__main__":
    evaluate()
