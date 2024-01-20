import { Button, Card, Flex, Text, Title } from "@tremor/react";

export function ButtonsOverlay() {
    return (
        <Flex justifyContent="end" className="space-x-2 pt-10 mt-8">
            <Button size="md" variant="secondary">
                Listen
            </Button>

            <Button size="md" variant="primary">
                Run
            </Button>
        </Flex>
    )
}