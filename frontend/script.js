document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData();
    formData.append('video', document.getElementById('videoFile').files[0]);
    
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    
    const result = await response.json();
    document.getElementById('result').innerText = `Result: ${result.result}`;
});