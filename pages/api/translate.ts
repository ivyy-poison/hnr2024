import { spawn } from 'child_process';
import { NextApiRequest, NextApiResponse } from 'next';


// function POST(request: Request) {
//   return request.json().then(({ code, date }) => {
//     // Stub method to process the code and date
//     const output = interpretCode(code, date);
//     return new Response(output, { status: 200 });
//   }).catch((err) => {
//     return new Response(`something went wrong ${err}`, { status: 500 });
//   });
// }
function POST(req: NextApiRequest, res: NextApiResponse) {
  const { code, date } = req.body;
  const output = interpretCode(code, date);
  res.status(200).send(output);
}

function interpretCode(code: string, date: string) {
  
  // Run a Python script using spawn

  // const pythonProcess = spawn('python', ['../../backend/test.py']);

  // // Collect data from script
  // let scriptOutput = '';
  // pythonProcess.stdout.on('data', (data) => {
  //   scriptOutput += data.toString();
  // });

  // // Collect error/exception messages
  // let scriptError = '';
  // pythonProcess.stderr.on('data', (data) => {
  //   scriptError += data.toString();
  // });

  // // Handle script completion
  // pythonProcess.on('close', (code) => {
  //   if (code !== 0 || scriptError) {
  //     console.error(`Python script failed with code ${code} and error: ${scriptError}`);
  //     // res.status(500).json({ error: scriptError });
      
  //   } else {
  //     console.log('Python script executed successfully:', scriptOutput);
  //     // res.status(200).json({ result: scriptOutput });
  //   }
  // });

  return `Code: ${code}, Date: ${date}`;
}

function GET(request: NextApiRequest, response: NextApiResponse) {
  response.status(200).send("Hello World!");
}

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === "POST") {
    return POST(req, res);
  } else {
    return GET(req, res);
  }
}
