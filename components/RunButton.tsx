import { Button } from "@tremor/react";
import { PlayIcon } from "@heroicons/react/24/solid";


interface props {
    handleRun: () => void;
}


export default function RunButton({ handleRun }: props) {

    return (
        <Button icon={PlayIcon} size="md" variant="primary" onClick={handleRun} >
            Run
        </Button>
    )
    
}