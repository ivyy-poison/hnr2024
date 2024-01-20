export const config = {
  runtime: 'edge',
};

function POST(request: Request) {
  return request.json().then(({ code, date }) => {
    // Stub method to process the code and date
    const output = interpretCode(code, date);
    return new Response(output);
  }).catch((err) => {
    return new Response("something went wrong", { status: 500 });
  });
}

function interpretCode(code: string, date: string) {
  return code;
}

function GET(request: Request) {
  return new Response("Hello world!");
}

export default function handler(request: Request) {
  
  if (request.method === "POST") {
    return POST(request);
  } else {
    return GET(request);
  }
}