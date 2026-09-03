export default function handler(req, res) {
  return res.status(200).json({
    total_visitors: 142,
    total_orders: 8,
    total_revenue_usd: 39.92,
    conversion_rate_pct: "5.6",
    recent_orders: [
      { id: "ord_108", customer: "khalid.b***@gmail.com", target_role: "Cloud Architect", amount_usd: 4.99, payment_method: "USDT (TRC20)", status: "PAID", timestamp: new Date(Date.now() - 900000).toISOString() },
      { id: "ord_107", customer: "daniil_dev***@yandex.ru", target_role: "Golang Backend", amount_usd: 4.99, payment_method: "Credit Card (Visa)", status: "PAID", timestamp: new Date(Date.now() - 3600000 * 2).toISOString() }
    ]
  });
}
