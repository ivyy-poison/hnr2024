import { Button } from '@tremor/react'
import * as Tone from 'tone'
import { tone_map } from '../pages/api/utils'
import { SpeakerWaveIcon } from '@heroicons/react/24/solid'

interface props {
    codeSound: string
}

export default function ListenButton({codeSound }: props) {
    async function playNote() {
        const synth = new Tone.Synth().toDestination();
        await Tone.start(); // Required to start audio context in some browsers
        for (let i = 0; i < codeSound.length; ++i) {
            const now = Tone.now();
            synth.triggerAttackRelease(tone_map.get(codeSound.charAt(i))!, "8n", now + 0.25 * i);
        };
    }

    return (
        <Button size="md" icon={ SpeakerWaveIcon } variant="secondary" onClick={playNote}>
            Listen
        </Button>
        
    )
}