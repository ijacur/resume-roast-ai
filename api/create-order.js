import fs from 'fs';
import path from 'path';

export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  let config = {
    crypto_usdt_address: "TQn9Y2khEsLJW1ChVWFMSMeSTow5KaxnSE (TRC20)",
    crypto_ton_address: "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N",
    stripe_checkout_url: ""
  };

  try {
    const p = path.join(process.cwd(), 'payment_config.json');
    if (fs.existsSync(p)) {
      config = JSON.parse(fs.readFileSync(p, 'utf8'));
    }
  } catch (e) {}

  const orderId = `ord_${Date.now().toString().slice(-6)}`;
  return res.status(200).json({
    order_id: orderId,
    amount_usd: 4.99,
    crypto_usdt_address: config.crypto_usdt_address || "TQn9Y2khEsLJW1ChVWFMSMeSTow5KaxnSE (TRC20)",
    crypto_ton_address: config.crypto_ton_address || "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N",
    stripe_checkout_url: config.stripe_checkout_url || `https://checkout.stripe.com/pay/mock_session_${orderId}`
  });
}
