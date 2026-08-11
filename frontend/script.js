const base = ''; // kosongin karena backend & frontend satu domain

async function connect() {
    const username = document.getElementById('username').value;
    if (!username) return alert('Isi dulu!');
    document.getElementById('status').innerText = '🔍 Nyari...';
    try {
        const res = await fetch('/connect', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username})
        });
        const data = await res.json();
        if (data.status === 'ok') {
            document.getElementById('status').innerText = '✅ Connected ke ' + username;
        } else {
            document.getElementById('status').innerText = '❌ ' + data.message;
        }
    } catch(e) {
        document.getElementById('status').innerText = '❌ Gagal konek!';
    }
}