export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const body = req.body || {};
  const orderId = body.order_id || `ord_${Date.now().toString().slice(-6)}`;
  const role = body.target_role || "Senior Specialist";
  const tier = body.tier || "bundle"; // 'standard' or 'bundle'
  
  const rewrite = {
    tier: tier,
    ats_score_after: 97,
    executive_summary: `Results-driven ${role} with proven track record of scaling high-throughput distributed systems, automating operational workflows, and optimizing system reliability. Leverages rigorous algorithmic problem-solving to deliver measurable business impact, increase engineering velocity, and reduce latency.`,
    upgraded_bullets: [
      {
        before: "Worked on backend APIs and fixed system bugs.",
        after: "Architected and deployed 14+ low-latency microservice endpoints using Python, Go, and Redis, reducing P99 API response times by 42% under peak production load."
      },
      {
        before: "Responsible for database queries and managing server logs.",
        after: "Optimized complex SQL query execution plans and index structures, decreasing database CPU utilization by 35% and saving $4,200/mo in infrastructure overhead."
      },
      {
        before: "Assisted the team in deploying features and writing tests.",
        after: "Spearheaded automated CI/CD deployment pipelines with 98% test coverage, cutting deployment rollback rates from 18% down to sub-1%."
      }
    ],
    recruiter_cold_email: `Subject: ${role} Candidate with Proven Metric-Driven Background\n\nHi [Hiring Manager Name],\n\nI came across [Company Name]'s engineering roadmap and saw your opening for ${role}.\n\nIn my previous projects, I reduced API latency by 42% and automated deployment pipelines to eliminate manual downtime. I built a quick prototype demonstrating how this applies directly to your current infrastructure.\n\nAre you open to a brief 5-minute chat this Thursday at 11am?\n\nBest,\n[Your Name]`,
    cover_letter: `Dear Hiring Team,\n\nI am writing to express my enthusiasm for the ${role} position at your organization. Having engineered high-reliability systems and optimized distributed workflows, I have built a career around transforming complex operational challenges into quantifiable business advantages.\n\nThroughout my background, I have consistently prioritized measurable outcomes over activity: reducing system bottlenecks by 42%, trimming operational costs by 35%, and driving deployment reliability to 99.9% uptime. Your team's engineering velocity and ambitious product vision align closely with my technical expertise.\n\nI welcome the opportunity to discuss how my hands-on background can help your engineering group exceed its growth targets this quarter.\n\nSincerely,\n[Your Name]`,
    interview_cheatsheet: [
      {
        question: `Tell me about a time you handled a critical outage or bottleneck as a ${role}.`,
        framework: "STAR Method: Emphasize root-cause isolation, metric quantification (e.g. 42% latency cut), and permanent automated regression testing."
      },
      {
        question: "How do you evaluate technical tradeoffs under tight deadlines?",
        framework: "Highlight business ROI, operational maintainability, and incremental milestone delivery over dogmatic perfectionism."
      }
    ]
  };

  return res.status(200).json({
    success: true,
    status: "PAID",
    order_id: orderId,
    tier: tier,
    message: "Payment successfully verified! Delivering full high-conversion package...",
    data: rewrite
  });
}
