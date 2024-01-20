import { CodeBlock } from '@/components/CodeBlock';
import Header from '@/components/Header';
import { TextBlock } from '@/components/TextBlock';
import { InputBlock } from '@/components/InputBlock';
import Head from 'next/head';
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {

  const [inputCode, setInputCode] = useState<string>('');
  const [outputCode, setOutputCode] = useState<string>('');
  const [userInput, setUserInput] = useState<string>('');
  const [date, setDate] = useState<Date>(new Date());

  function handleTranslate() {
    axios.post('/api/translate', {
      date: formatDate(date),
      code: inputCode,
      input: userInput
    })
    .then((response) => {
      console.log(response)
      setOutputCode(response.data);
    })
    .catch((error) => {
      console.error('Error translating code:', error);
    })
  }

  const formatDate = (date: Date) => {
    return date.toLocaleDateString('en-US', { year: 'numeric', month: '2-digit', day: '2-digit' });
}

  return (
    <>
      <Head>
        <title>HnR 2024</title>
        <meta
          name="description"
          content="Use AI to translate code from one language to another."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className="flex h-full min-h-screen flex-col items-center bg-[#0E1117] px-4 pb-20 text-neutral-200 sm:px-10">
        
        <Header date={date} setDate = {setDate} />
        <div className="mt-6 flex w-full max-w-[1200px] flex-col justify-between sm:flex-row sm:space-x-4">
          <div className="h-100 flex flex-col justify-center space-y-2 sm:w-2/4">
            <div className="text-center text-xl font-bold">Input</div>

              <CodeBlock
                code={inputCode}
                editable={true}
                onChange={(value) => {
                  setInputCode(value);
                }}
                onSubmit={handleTranslate}
              />

              <InputBlock text={userInput} onChange={setUserInput} onSubmit={handleTranslate} />
            
            
          </div>
          <div className="mt-8 flex h-full flex-col justify-center space-y-2 sm:mt-0 sm:w-2/4">
            <div className="text-center text-xl font-bold">Output</div>
              <TextBlock text={outputCode} />
          </div>
        </div>
      </div>
    </>
  );
}
