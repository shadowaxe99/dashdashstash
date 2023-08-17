// App JavaScript code

import express from 'express';
import AIAgent from './ai_agent/ai_agent.js';

const app = express();

app.get('/', (req, res) => {
  const agent = new AIAgent();
  const response = agent.interactWithUser();
  res.send(response);
});

app.listen(3000, () => {
  console.log('App is listening on port 3000');
});