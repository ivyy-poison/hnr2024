import { Button } from "@tremor/react";
import { PlayIcon } from "@heroicons/react/24/solid";


interface props {
    handleRun: () => void;
    isLoading?: boolean;
}


export default function RunButton({ handleRun, isLoading=false }: props) {

    return (
        <Button icon={PlayIcon} size="md" variant="primary" onClick={handleRun} loading={isLoading}>
            Run
        </Button>
    )
    
}