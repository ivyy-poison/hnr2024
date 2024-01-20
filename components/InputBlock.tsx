interface Props {
    text: string;
    onChange?: (value: string) => void;
    onSubmit?: () => void;
  }

export const InputBlock: React.FC<Props> = ({
    text,
    onChange = () => {},
    onSubmit = () => {},
  }) => {
    function handleKeyPress(event: React.KeyboardEvent) {
      if (event.ctrlKey && event.key === 'Enter') {
        onSubmit()
      }
    }
    return (
      <textarea
        className="h-[100px] w-full bg-[#1A1B26] text-sm focus:outline-none"
        style={{ resize: 'none', fontFamily: 'Source Code Pro, monospace' }}
        value={text}
        placeholder="Enter user input here ..."
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={handleKeyPress}
      />
    );
  };