const socket = io();

const orb = document.getElementById('ai-orb');
const stateText = document.getElementById('ai-state');
const subText = document.getElementById('ai-subtext');
const consoleLog = document.getElementById('console-log');

socket.on('connect', () => {
    document.getElementById('connection-status').textContent = "LINK ESTABLISHED";
    document.getElementById('connection-status').style.color = "var(--primary-neon)";
});

socket.on('disconnect', () => {
    document.getElementById('connection-status').textContent = "LINK LOST";
    document.getElementById('connection-status').style.color = "var(--danger-neon)";
    orb.className = 'orb offline';
    stateText.textContent = "OFFLINE";
    subText.textContent = "Server disconnected.";
});

function appendLog(type, text) {
    const p = document.createElement('p');
    p.className = type;
    p.textContent = `> ${text}`;
    consoleLog.appendChild(p);
    consoleLog.scrollTop = consoleLog.scrollHeight;
}

socket.on('sam_update', (data) => {
    const status = data.status;
    const msg = data.message;
    
    if (status === "IDLE") {
        orb.className = 'orb idle';
        stateText.textContent = "IDLE";
        stateText.style.color = "var(--primary-neon)";
        subText.textContent = msg;
        if(msg) appendLog('sys-msg', msg);
    } 
    else if (status === "LISTENING") {
        orb.className = 'orb listening';
        stateText.textContent = "LISTENING";
        stateText.style.color = "#00BFFF";
        subText.textContent = msg;
    }
    else if (status === "PROCESSING") {
        orb.className = 'orb thinking';
        stateText.textContent = "PROCESSING";
        stateText.style.color = "#9400D3";
        subText.textContent = "Parsing Intent...";
        appendLog('user-msg', msg);
    }
    else if (status === "THINKING") {
        orb.className = 'orb thinking';
        stateText.textContent = "NEURAL LINK";
        stateText.style.color = "#9400D3";
        subText.textContent = msg;
        appendLog('sys-msg', msg);
    }
    else if (status === "RESPONDING" || status === "SUCCESS") {
        orb.className = 'orb idle';
        stateText.textContent = "ACTIVE";
        stateText.style.color = "var(--primary-neon)";
        subText.textContent = "Executing...";
        appendLog('ai-msg', msg);
    }
    else if (status === "OFFLINE") {
        orb.className = 'orb offline';
        stateText.textContent = "OFFLINE";
        stateText.style.color = "#555";
        subText.textContent = msg;
        appendLog('sys-msg', msg);
    }
    else if (status === "ERROR") {
        orb.className = 'orb offline';
        stateText.textContent = "ERROR";
        stateText.style.color = "var(--danger-neon)";
        subText.textContent = msg;
        appendLog('sys-msg', `ERROR: ${msg}`);
    }
});
