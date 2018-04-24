# import modules
import MySQLdb
from pydub import AudioSegment
	

sound_path= "C:\\Users\\vansh\OneDrive\Desktop\py_project\Audio Encryption\\"
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="root",     # password
                     db="eyeshield")   # name of the database
 

message = str(input("Enter the Your message: "))

# Create a Cursor object to execute queries.
cur = db.cursor()
 
output = []
#split message string into characters
for i in message:
	 # Select data from table using SQL query.
	 cur.execute("SELECT filename FROM data WHERE word = %s ",i)
	 # print the first and second columns      
	 db_output = cur.fetchone()
	 data = sound_path +"sounds\\"+ str(db_output[0])
	 output.append(data)

soundn = []
for i in range(0,len(output)):
	sound = AudioSegment.from_wav(output[i])
	soundn.append(sound)


combined_sound=soundn[0]
for i in range(1,len(soundn)):
	if i > len(soundn):
		break
	combined_sound = combined_sound+soundn[i]
combined_sound.export("Outputsounds.wav", format="wav")


#Get Data from user into Text Format



