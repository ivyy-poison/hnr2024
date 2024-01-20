import { Button, Card, Flex, Text, Title } from "@tremor/react";
import * as Tone from "tone";

interface props {
    handleRun: () => void;
}

export function ButtonsOverlay({handleRun}: props) {
    async function playNote() {
        const synth = new Tone.Synth().toDestination();
        await Tone.start(); // Required to start audio context in some browsers
        synth.triggerAttackRelease("C4", "8n"); // Play note C4 for an 8th note (half a second)
        synth.triggerAttackRelease("D4", "8n");
    }

    return (
        <Flex justifyContent="end" className="space-x-2 pt-10 mt-8">
            <Button size="md" variant="secondary" onClick={playNote}>
                Listen
            </Button>

            <Button size="md" variant="primary" onClick={handleRun} >
                Run
            </Button>
        </Flex>
    )
}