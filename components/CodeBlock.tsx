import { tokyoNight } from '@uiw/codemirror-theme-tokyo-night';
import CodeMirror from '@uiw/react-codemirror';
import { FC, useEffect, useState } from 'react';

interface Props {
  code: string;
  editable?: boolean;
  onChange?: (value: string) => void;
}

export const CodeBlock: FC<Props> = ({
  code,
  editable = false,
  onChange = () => {},
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
      onChange(code);
    }
  }

  return (
    <div className="relative">
      <CodeMirror
        editable={editable}
        value={code}
        minHeight="500px"
        theme={tokyoNight}
        onChange={(value) => onChange(value)}
        onKeyDown={handleKeyPress}
      />
    </div>
  );
};
