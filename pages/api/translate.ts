import { spawn } from 'child_process';
import { NextApiRequest, NextApiResponse } from 'next';
import {readFile} from 'fs';

async function POST(req: NextApiRequest, res: NextApiResponse) {
  const { code, date, input } = req.body;
  return interpretCode(code, date, input).then((result) => {
    res.status(200).send(result);
  }).catch((error) => {
    res.status(404).send(error);
  });
}

async function interpretCode(code: string, date: string, input: string): Promise<string> {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn('python3', ['backend/execute.py', date, code, input]);

    let jsonFileLocation = '';
    pythonProcess.stdout.on('data', (data) => {
      jsonFileLocation += data.toString();
    });

    pythonProcess.on('close', (statusCode) => {
      readFile(jsonFileLocation.trimEnd(), 'utf-8', (err, data) => {
        if (err) {
          reject(err);
        } else {
          let json_data = JSON.parse(data);
          if (json_data["Status code"] == 1 || json_data["Status code"] == 2) {
            reject("Line error at line " + json_data["Line error"]);
          } else {
            resolve(json_data);
          }
        }

      })
    });
  });
}

function GET(request: NextApiRequest, response: NextApiResponse) {
  response.status(200).send("Hello World!");
}

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === "POST") {
    return POST(req, res);
  } else {
    return GET(req, res);
  }
}
