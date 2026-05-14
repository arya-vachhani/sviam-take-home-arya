/**
 * Evaluation harness stub.
 *
 * TODO: Implement this.
 *
 * Run your classifier across all 18 sessions, compare against the 5 labeled
 * sessions, and report your chosen metrics.
 */

const { loadAllSessions, loadLabels } = require("./loader");
const { classifySession } = require("./classify");

async function evaluate() {
  const sessions = loadAllSessions();
  const labels = loadLabels();

  const results = [];
  for (const session of sessions) {
    const result = await classifySession(session);
    results.push(result);
  }

  // TODO: Compare results against labels.
  // TODO: Compute your chosen metrics.
  // TODO: Print a results table and metric summary.

  console.log("Session            | Predicted       | Confidence | Ground Truth");
  console.log("-------------------+-----------------+------------+-------------");
  for (const r of results) {
    const gt = labels[r.session_id] || "—";
    console.log(
      `${r.session_id.padEnd(18)} | ${r.label.padEnd(15)} | ${r.confidence.padEnd(10)} | ${gt}`
    );
  }
}

evaluate();
