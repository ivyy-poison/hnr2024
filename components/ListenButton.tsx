import { Button } from '@tremor/react'
import * as Tone from 'tone'
import { tone_map } from '../pages/api/utils'
import { SpeakerWaveIcon } from '@heroicons/react/24/solid'
import { useState } from 'react'

interface props {
    codeSound: string
}

export default function ListenButton({codeSound }: props) {
    const [isLoading, setLoading] = useState(false);
    const [synth, setSynth] = useState<Tone.Synth | null>(null);

    async function playNote() {
        console.log('playNote called', { isLoading });
        setLoading(true);
        const newSynth = new Tone.Synth().toDestination();
        setSynth(newSynth);
        await Tone.start(); // Required to start audio context in some browsers
        for (let i = 0; i < codeSound.length; ++i) {
            const now = Tone.now();
            newSynth.triggerAttackRelease(tone_map.get(codeSound.charAt(i))!, "8n", now + 0.25 * i);
        };
        // Wait for all notes to finish playing before setting isLoading to false
        setTimeout(() => {
            setLoading(false);
            console.log('playNote ended', { isLoading });
        }, codeSound.length * 250); // Adjust the delay based on the length of your notes
    }

    return (
        <Button size="md" icon={ SpeakerWaveIcon } variant="secondary" onClick={playNote} loading={isLoading}>
            Listen
        </Button>
    )
}