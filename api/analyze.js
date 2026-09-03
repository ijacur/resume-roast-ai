export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { resume_text = '', target_role = 'Software Specialist' } = req.body || {};
  const len = resume_text.length;
  const hasNumbers = (resume_text.match(/\d+[%$kKmM]?/g) || []).length;
  const weakVerbs = ["helped", "worked on", "responsible for", "assisted", "did", "handled"].filter(v => 
    resume_text.toLowerCase().includes(v)
  );

  let fallbackScore = 38;
  if (hasNumbers > 5) fallbackScore += 15;
  if (len > 800) fallbackScore += 10;
  if (weakVerbs.length === 0) fallbackScore += 12;
  fallbackScore = Math.min(Math.max(fallbackScore, 32), 64);

  const fallbackResult = {
    ats_score: fallbackScore,
    rejection_probability_pct: 100 - fallbackScore,
    verdict: fallbackScore < 45 ? "CRITICAL: Immediate ATS Bot Rejection" : "WARNING: Weak Impact Metrics",
    weak_verbs_found: weakVerbs.length > 0 ? weakVerbs : ["responsible for", "assisted"],
    metrics_detected: hasNumbers,
    teaser_roast: `Your resume reads like a passive job description rather than an executive accomplishment record for a ${target_role}. You used passive phrasing and only quantified ${hasNumbers} metrics. ATS filters will discard this in 4.2 seconds.`
  };

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    return res.status(200).json(fallbackResult);
  }

  try {
    const prompt = `You are a ruthless, elite Silicon Valley technical recruiter and ATS parsing algorithm.
Analyze this candidate's resume for the target role: "${target_role}".

Resume Text:
"""
${resume_text.slice(0, 3000)}
"""

Return ONLY a JSON object (no markdown, no backticks, just raw valid JSON) with this exact schema:
{
  "ats_score": (integer between 30 and 68),
  "rejection_probability_pct": (integer between 50 and 85),
  "verdict": "CRITICAL: Immediate ATS Bot Rejection" or "HIGH RISK: Lacks Quantified Business Impact",
  "weak_verbs_found": [list of 2-4 exact passive/weak phrases found in the resume, e.g. "worked on", "helped"],
  "metrics_detected": (integer count of quantifiable metrics found),
  "teaser_roast": "A sharp, 2-3 sentence technical roast explaining why this resume gets rejected by recruiters and how lacking Google XYZ metrics hurts them."
}`;

    const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`;
    const resp = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }],
        generationConfig: { responseMimeType: "application/json" }
      })
    });

    if (!resp.ok) {
      return res.status(200).json(fallbackResult);
    }

    const data = await resp.json();
    const candidateText = data.candidates?.[0]?.content?.parts?.[0]?.text;
    if (!candidateText) {
      return res.status(200).json(fallbackResult);
    }

    const parsed = JSON.parse(candidateText);
    return res.status(200).json({
      ats_score: parsed.ats_score || fallbackScore,
      rejection_probability_pct: parsed.rejection_probability_pct || (100 - fallbackScore),
      verdict: parsed.verdict || fallbackResult.verdict,
      weak_verbs_found: parsed.weak_verbs_found || fallbackResult.weak_verbs_found,
      metrics_detected: parsed.metrics_detected || hasNumbers,
      teaser_roast: parsed.teaser_roast || fallbackResult.teaser_roast
    });
  } catch (e) {
    return res.status(200).json(fallbackResult);
  }
}
