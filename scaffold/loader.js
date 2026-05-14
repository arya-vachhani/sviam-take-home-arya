/**
 * Session data loader.
 * Reads session JSON files from /data/sessions/.
 */

const fs = require("fs");
const path = require("path");

const DATA_DIR = path.join(__dirname, "..", "data", "sessions");
const LABELS_PATH = path.join(__dirname, "..", "data", "labels.json");

function loadSession(sessionId) {
  const filePath = path.join(DATA_DIR, `${sessionId}.json`);
  return JSON.parse(fs.readFileSync(filePath, "utf-8"));
}

function loadAllSessions() {
  const files = fs
    .readdirSync(DATA_DIR)
    .filter((f) => f.startsWith("session_") && f.endsWith(".json"))
    .sort();
  return files.map((f) => JSON.parse(fs.readFileSync(path.join(DATA_DIR, f), "utf-8")));
}

function loadLabels() {
  return JSON.parse(fs.readFileSync(LABELS_PATH, "utf-8"));
}

module.exports = { loadSession, loadAllSessions, loadLabels };

if (require.main === module) {
  const sessions = loadAllSessions();
  const labels = loadLabels();
  console.log(`Loaded ${sessions.length} sessions, ${Object.keys(labels).length} labels`);
  sessions.forEach((s) => {
    const label = labels[s.session_id] || "unlabeled";
    console.log(`  ${s.session_id}: ${s.problem_id} (${s.language}) — ${label}`);
  });
}
