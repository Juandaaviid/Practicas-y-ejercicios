import numpy as np
import scipy.io.wavfile as wavfile
import scipy.signal

# Load the audio file
fs, audio = wavfile.read('morse.wav')

# Apply a low-pass filter to remove high-frequency noise
cutoff_freq = 1000
b, a = scipy.signal.butter(5, 2*cutoff_freq/fs, btype='low')
filtered_audio = scipy.signal.filtfilt(b, a, audio)

# Detect the dots and dashes
threshold = np.mean(filtered_audio)
deltas = np.diff(filtered_audio > threshold)
start = np.where(deltas == 1)[0]
end = np.where(deltas == -1)[0]

# Convert the dots and dashes to ASCII characters
morse_code = {'-.--.': '(', '-.--.-': ')', '.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
            '...--': '3', '-....': '6', '.----': '1', '....': 'H', '.--.-.': '@', '.-.': 'R',
            '-...': 'B', '--.': 'G', '-..-.': '/', '..---': '2', '-.-.': 'C', '-....-': '-',
            '-..': 'D', '.': 'E', '..-.': 'F', '.-.' : 'R', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
            '--..': 'Z', '-----': '0', '.----.': "'", '---...': ':', '-.-.-.': ';', '-...-': '=',
            '..--..': '?', '.--.-.': '@', '.-.-.-': '.', '-....-': '-', '-..-.': '/', '-.--.-': ')',
            '-.--.': '(', '...-..-': '$'}

message = ''
for i in range(len(start)):
    duration = end[i] - start[i]
    if duration < fs/10:
        message += ''
    elif duration < fs/3:
        message += '.'
    else:
        message += '-'
        
    if i < len(start)-1 and start[i+1]-end[i] > fs/3:
        message += ' '
        
decoded_message = ''
for code in message.split(' '):
    if code in morse_code:
        decoded_message += morse_code[code]
    else:
        decoded_message += ' '
        
print(decoded_message)
