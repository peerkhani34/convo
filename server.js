const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.urlencoded({ extended: true }));

app.post('/', (req, res) => {
  const cookies = req.body.cookies;
  // Token generation logic goes here (server-side)
  res.send(`Received cookies: ${cookies}`);
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});