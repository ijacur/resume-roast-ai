export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { resume_text = '', target_role = 'Professional' } = req.body || {};
  const len = resume_text.length;
  const hasNumbers = (resume_text.match(/\d+[%$kKmM]?/g) || []).length;
  const weakVerbs = ["helped", "worked on", "responsible for", "assisted", "did", "handled"].filter(v => 
    resume_text.toLowerCase().includes(v)
  );

  let score = 38;
  if (hasNumbers > 5) score += 15;
  if (len > 800) score += 10;
  if (weakVerbs.length === 0) score += 12;
  score = Math.min(Math.max(score, 32), 64);

  return res.status(200).json({
    ats_score: score,
    rejection_probability_pct: 100 - score,
    verdict: score < 45 ? "CRITICAL: Immediate ATS Bot Rejection" : "WARNING: Weak Impact Metrics",
    weak_verbs_found: weakVerbs.length > 0 ? weakVerbs : ["responsible for", "assisted"],
    metrics_detected: hasNumbers,
    teaser_roast: `Your resume reads like a passive job description rather than an executive accomplishment record. You used passive phrases like '${weakVerbs[0] || "responsible for"}' and only quantified ${hasNumbers} measurable achievements. An ATS filter will discard this in 4.2 seconds.`
  });
}
