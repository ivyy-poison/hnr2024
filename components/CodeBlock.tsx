import { androidstudio } from '@uiw/codemirror-themes-all';
import CodeMirror from '@uiw/react-codemirror';
import { FC, useEffect, useState } from 'react';

interface Props {
  code: string;
  editable?: boolean;
  onChange?: (value: string) => void;
  onSubmit?: () => void;
}

export const CodeBlock: FC<Props> = ({
  code,
  editable = false,
  onChange = () => {},
  onSubmit = () => {}
}) => {
  const [copyText, setCopyText] = useState<string>('Copy');

  useEffect(() => {
    const timeout = setTimeout(() => {
      setCopyText('Copy');
    }, 2000);

    return () => clearTimeout(timeout);
  }, [copyText]);

  function handleKeyPress(event: React.KeyboardEvent) {
    if (event.ctrlKey && event.key === 'Enter') {
      onSubmit()
    }
  }

  return (
    <div className="relative text-sm my-4">
      <CodeMirror
        editable={editable}
        value={code}
        minHeight="500px"
        theme={androidstudio}
        onChange={(value) => onChange(value)}
        onKeyDown={handleKeyPress}
      />
    </div>
  );
};
