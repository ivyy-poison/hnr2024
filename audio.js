import { AudioContext } from "web-audio-api";

const audioContext = new AudioContext();

const oscillator = audioContext.createOscillator();

oscillator.connect(audioContext.destination);

oscillator.start(0);
