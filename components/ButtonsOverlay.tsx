import { Button, Card, Flex, Text, Title } from "@tremor/react";
import * as Tone from "tone";
import {tone_map} from "../pages/api/utils";

interface props {
    handleRun: () => void;
    codeSound: string
}

export function ButtonsOverlay({handleRun, codeSound}: props) {
    async function playNote() {
        const synth = new Tone.Synth().toDestination();
        await Tone.start(); // Required to start audio context in some browsers
        for (let i = 0; i < codeSound.length; ++i) {
            const now = Tone.now();
            synth.triggerAttackRelease(tone_map.get(codeSound.charAt(i))!, "8n", now + 0.25 * i);
        };
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