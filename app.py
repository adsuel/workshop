from flask import Flask, render_template_string

app = Flask(__name__)

PONG_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pong in Python (Flask)</title>
    <style>
        body { background: #222; margin: 0; }
        canvas { display: block; margin: 0 auto; background: #111; }
    </style>
</head>
<body>
<canvas id="pong" width="600" height="400"></canvas>
<script>
const canvas = document.getElementById('pong');
const ctx = canvas.getContext('2d');
const paddleWidth = 10, paddleHeight = 80;
let leftY = 160, rightY = 160, ballX = 300, ballY = 200, ballVX = 4, ballVY = 2, leftScore = 0, rightScore = 0;
function draw() {
    ctx.clearRect(0,0,600,400);
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, leftY, paddleWidth, paddleHeight);
    ctx.fillRect(590, rightY, paddleWidth, paddleHeight);
    ctx.beginPath(); ctx.arc(ballX, ballY, 8, 0, Math.PI*2); ctx.fill();
    ctx.font = '32px Arial'; ctx.fillText(leftScore, 250, 40); ctx.fillText(rightScore, 330, 40);
}
function update() {
    ballX += ballVX; ballY += ballVY;
    if(ballY < 8 || ballY > 392) ballVY = -ballVY;
    if(ballX < 18 && ballY > leftY && ballY < leftY+paddleHeight) ballVX = -ballVX;
    if(ballX > 582 && ballY > rightY && ballY < rightY+paddleHeight) ballVX = -ballVX;
    if(ballX < 0) { rightScore++; reset(); }
    if(ballX > 600) { leftScore++; reset(); }
    if(rightY + paddleHeight/2 < ballY) rightY += 3; else rightY -= 3;
    rightY = Math.max(0, Math.min(320, rightY));
}
function reset() { ballX = 300; ballY = 200; ballVX = -ballVX; }
document.addEventListener('keydown', e => {
    if(e.key === 'ArrowUp') leftY -= 20;
    if(e.key === 'ArrowDown') leftY += 20;
    leftY = Math.max(0, Math.min(320, leftY));
});
function loop() { update(); draw(); requestAnimationFrame(loop); }
loop();
</script>
</body>
</html>
'''

@app.route('/')
def pong():
    return render_template_string(PONG_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)