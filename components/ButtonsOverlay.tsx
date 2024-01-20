import { Button, Card, Flex, Text, Title } from "@tremor/react";

interface props {
    handleRun: () => void;
}

export function ButtonsOverlay({handleRun}: props) {
    return (
        <Flex justifyContent="end" className="space-x-2 pt-10 mt-8">
            <Button size="md" variant="secondary">
                Listen
            </Button>

            <Button size="md" variant="primary" onClick={handleRun} >
                Run
            </Button>
        </Flex>
    )
}