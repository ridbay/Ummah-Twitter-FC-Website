const https = require('https');

const folderId = '1KMVb7lrMoKbD7w0u86yI0bwiwEYwTcF-';
const url = `https://drive.google.com/drive/folders/${folderId}`;

https.get(url, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    // Regex to capture Google Drive IDs (usually 28 to 33 chars)
    const idRegex = /\["(1[a-zA-Z0-9_-]{27,32})"/g;
    let match;
    const ids = new Set();
    while ((match = idRegex.exec(data)) !== null) {
      if (match[1] !== folderId) {
        ids.add(match[1]);
      }
    }
    console.log(Array.from(ids));
  });
});
