#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "🚀 Starting Autonomous Paid Micro-SaaS on Bun..."

# Kill any existing process on 3333
lsof -ti:3333 | xargs kill -9 2>/dev/null

# Generate viral marketing content
python3 "$DIR/viral_traffic_bot.py"

# Start server in background with Bun
/Users/jasur/.bun/bin/bun "$DIR/server.js" &
SERVER_PID=$!
sleep 1

echo "✅ Server running on http://localhost:3333 (PID: $SERVER_PID)"
echo "🌐 Opening Customer App & Owner Revenue Dashboard..."

open "http://localhost:3333"
sleep 0.5
open "http://localhost:3333/owner"

echo "💰 Autonomous Cash Machine is LIVE!"
