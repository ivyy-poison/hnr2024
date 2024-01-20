import { spawn } from 'child_process';
import { NextApiRequest, NextApiResponse } from 'next';

async function POST(req: NextApiRequest, res: NextApiResponse) {
  const { code, date, input } = req.body;
  interpretCode(code, date, input).then((result) => {
    res.status(200).send(result);
  }).catch((error) => {
    res.status(404).send(error);
  });
}

async function interpretCode(code: string, date: string, input: string): Promise<string> {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn('python3', ['backend/test.py', '123', code]);

    let scriptOutput = '';
    pythonProcess.stdout.on('data', (data) => {
      scriptOutput += data.toString();
    });

    let scriptError = '';
    pythonProcess.stderr.on('data', (data) => {
      scriptError += data.toString();
    });

    pythonProcess.on('close', (statusCode) => {
      if (statusCode !== 0 || scriptError) {
        console.error(`Python script failed with code ${statusCode} and error: ${scriptError}`);
        reject(`Python script failed with code ${statusCode} and error: ${scriptError}`);
      } else {
        console.log('Python script executed successfully:', scriptOutput);
        resolve(`Code: ${code}, input: ${input}, Date: ${date}, scriptOutput: ${scriptOutput}, scriptError: ${scriptError}`);
      }
    });
  });
}

function GET(request: NextApiRequest, response: NextApiResponse) {
  response.status(200).send("Hello World!");
}

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === "POST") {
    POST(req, res);
  } else {
    GET(req, res);
  }
}
