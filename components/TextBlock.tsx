interface Props {
  text: string;
  editable?: boolean;
  onChange?: (value: string) => void;
}

export const TextBlock: React.FC<Props> = ({
  text,
  editable = false,
  onChange = () => {},
}) => {
  return (
    <textarea
      className="h-[440px] w-full bg-[#1A1B26] text-sm focus:outline-none"
      style={{ resize: 'none', fontFamily: 'Source Code Pro, monospace' }}
      value={text}
      onChange={(e) => onChange(e.target.value)}
      disabled={!editable}
    />
  );
};
