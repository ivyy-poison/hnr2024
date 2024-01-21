import { Button, Card, Flex, Text, Title } from "@tremor/react";
import * as Tone from "tone";
import {tone_map} from "../pages/api/utils";
import RunButton from "./RunButton";
import ListenButton from "./ListenButton";

interface props {
    handleRun: () => void;
    codeSound: string;
    isLoading?: boolean;
}

export function ButtonsOverlay({handleRun, codeSound, isLoading=false}: props) {
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
            <ListenButton codeSound={codeSound} />
            <RunButton handleRun={handleRun} isLoading={isLoading} />
        </Flex>
    )
}