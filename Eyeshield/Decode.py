#import modules
from pydub import AudioSegment
from pydub.utils import make_chunks
import librosa
import matplotlib.pyplot as plt
from dtw import dtw
import librosa.display
from numpy.linalg import norm


#get .wav file path
encryptedaudio = 'C:\\Users\\vansh\OneDrive\Desktop\py_project\Audio Encryption\\Outputsounds.wav'#str(input("Enter Path of Encrypted .wav sound file: ")) 
myaudio = AudioSegment.from_file(encryptedaudio , "wav") 

# length of spliting
chunk_length_ms = 2000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files
for i, chunk in enumerate(chunks):
    chunk_name = "chunk{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")

#Loading audio files
y1, sr1 = librosa.load('C:\\Users\\vansh\OneDrive\Desktop\py_project\Audio Encryption\\chunk0.wav') 
y2, sr2 = librosa.load('C:\\Users\\vansh\OneDrive\Desktop\py_project\Audio Encryption\\sounds\C.wav') 

#Showing multiple plots using subplot
plt.subplot(1, 2, 1) 
mfcc1 = librosa.feature.mfcc(y1,sr1)   #Computing MFCC values
librosa.display.specshow(mfcc1)

plt.subplot(1, 2, 2)
mfcc2 = librosa.feature.mfcc(y2, sr2)
librosa.display.specshow(mfcc2)

dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
print("The normalized distance between the two : ",dist)   # 0 for similar audios 

if int(dist) ==0:
	print("same audio")
else:
	print("different audio")