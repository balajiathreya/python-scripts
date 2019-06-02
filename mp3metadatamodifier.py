import mutagen
import os
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from mutagen.id3 import TALB,TPE1,TSOP,TPE2, TIT2,TCOM,TIT1,TSOT,TSO2,TSOC


## Modifies mp3/id3 metadata of mp3 files downloaded from Masstamilan.in and Masstamilan.org for cleaner look in iTunes/Apple Music
# https://help.mp3tag.de/main_tags.html
# https://www.programcreek.com/python/example/73822/mutagen.id3.APIC

path = "/Users/balajiathreya/Downloads/newmusic"


#renames folders

albumfolders = os.listdir(path)
for file_name in albumfolders:
	new_file_name = file_name.replace('- [Masstamilan.in]','').replace(' [Masstamilan.In]','').replace(' - Masstamilan.In - Masstamilan.In-','').replace(' [Masstamilan.In]-','').replace('-MassTamilan.org','')
	new_file_name = new_file_name.replace(' [Masstamilan.in]','').replace(' - Masstamilan.In-','').replace(' (Masstamilan.in)','').replace('-MassTamilan.com','').replace('-Masstamilan.In','').replace('-StarMusiQ.Com','')
	new_file_name = new_file_name.replace('-[Masstamilan.In]','').replace(' ','-')
	new_file_name = new_file_name.replace('-320kbps','').replace('-128kbps','') .replace('-160kbps','') .replace('_160kbps','') .replace('_128kbps','') .replace('_320kbps','') .replace(' ','-')
	new_file_name = new_file_name.replace('-(','(')
	print file_name + "--->" + new_file_name
	shutil.move(os.path.join(path, file_name), os.path.join(path, new_file_name))



#rename files

albumfolders = os.listdir(path)
for folder in albumfolders:
	if os.path.isdir(os.path.join(path, folder)):
		song_folder = os.path.join(path, folder)
		print 'song folder ' + song_folder
		#if song_folder == '/Users/balajiathreya/Downloads/music/Uyire':
		songs = os.listdir(song_folder)
		for song in songs:
			if 'DS_Store' not in song :
				new_song = song.replace('- [Masstamilan.in]','').replace(' [Masstamilan.In]','').replace(' - Masstamilan.In - Masstamilan.In-','').replace(' [Masstamilan.In]-','').replace('-MassTamilan.org','')
				new_song = new_song.replace(' [Masstamilan.in]','').replace(' - Masstamilan.In-','').replace(' (Masstamilan.in)','').replace('-MassTamilan.com','').replace('-Masstamilan.In','').replace('-StarMusiQ.Com','')
				new_song = new_song.replace('-[Masstamilan.In]','').replace(' ','-')
				new_song = new_song.replace('-(','(').replace(')-',')').replace('--','').replace('-.mp3','.mp3')
				print "mp3 is " + new_song
				os.rename(os.path.join(song_folder, song), os.path.join(song_folder, new_song))


#modify metadata 

albumfolders = os.listdir(path)
for folder in albumfolders:
	if os.path.isdir(os.path.join(path, folder)):
		song_folder = os.path.join(path, folder)
		#print 'song folder ' + song_folder
		#if song_folder == '/Users/balajiathreya/Downloads/music/Punnagai-Mannan':
		print "processing " + song_folder
		songs = os.listdir(song_folder)
		for song in songs:
			if 'DS_Store' not in song :
				print "======"+os.path.join(song_folder, song)+"======"

				id3 = ID3(os.path.join(song_folder, song))

				# print "old id3"
				# print id3
				#COMMENT
				id3.setall("COMM", "")
				
				#LYRICS
				id3.setall("USLT", "")
				
				#workname
				id3.setall('TIT1', "")

				
				#PIC
				if id3.getall('APIC'):
					id3.delall('APIC')

				#ALBUM
				talb = id3.getall('TALB')
				if talb :
					c = str(talb[0]).replace(' - [Masstamilan.In]','').replace('-[Masstamilan.In]','').replace(' [Masstamilan.In]','').replace(' [Masstamilan.in]','').replace(' - Masstamilan.In','').replace('[Masstamilan.in]','').replace(' - MassTamilan.com','').replace(' - Masstamilan.in','').replace(' -Masstamilan.In','').replace('Masstamilan.In','').replace('masstamilan.in','').replace(' (masstamilan.in)','').replace(' - MassTamilan.org','').replace('-StarMusiQ.Com','')
					id3.add( TALB( encoding=3, text=c ) )
					
				
				#ARTIST
				tpe1 = id3.getall('TPE1')
				if tpe1 :
					a = str(tpe1[0]).replace(' - [Masstamilan.In]','').replace('-[Masstamilan.In]','').replace(' [Masstamilan.In]','').replace(' [Masstamilan.in]','').replace(' - Masstamilan.In','').replace('[Masstamilan.in]','').replace(' - MassTamilan.com','').replace(' - Masstamilan.in','').replace(' -Masstamilan.In','').replace('Masstamilan.In','').replace('masstamilan.in','').replace(' (masstamilan.in)','').replace(' - MassTamilan.org','').replace('-StarMusiQ.Com','')
					try:
						id3.add( TPE1( encoding=3, text=a ) )
						id3.add( TSOP( encoding=3, text=a ) )
					except :
						print "encoding error"
				
				#TITLE
				tit2 = id3.getall('TIT2')
				if tit2:
					b = str(tit2[0]).replace(' - [Masstamilan.In]','').replace('-[Masstamilan.In]','').replace(' [Masstamilan.In]','').replace(' [Masstamilan.in]','').replace(' - Masstamilan.In','').replace('[Masstamilan.in]','').replace(' - MassTamilan.com','').replace(' - Masstamilan.in','').replace(' -Masstamilan.In','').replace('Masstamilan.In','').replace('masstamilan.in','').replace(' (masstamilan.in)','').replace(' - MassTamilan.org','').replace('-StarMusiQ.Com','')
					try:
						id3.add( TIT2( encoding=3, text=a ) )
						id3.add( TSOT( encoding=3, text=a ) )
					except :
						print "encoding error"

				#ALBUMARTIST
				tpe2 = id3.getall('TPE2')
				if tpe2 : 
					x = str(tpe2[0]).replace(' - [Masstamilan.In]','').replace('-[Masstamilan.In]','').replace(' [Masstamilan.In]','').replace(' [Masstamilan.in]','').replace(' - Masstamilan.In','').replace('[Masstamilan.in]','').replace(' - MassTamilan.com','').replace(' - Masstamilan.in','').replace(' -Masstamilan.In','').replace('Masstamilan.In','').replace('masstamilan.in','').replace(' (masstamilan.in)','').replace(' - MassTamilan.org','').replace('-StarMusiQ.Com','')
					try:
						id3.add( TPE2( encoding=3, text=a ) )
						id3.add( TSO2( encoding=3, text=a ) )
					except :
						print "encoding error"

				# composer 
				tcom = id3.getall('TCOM')
				if tcom:
					try:
						id3.add( TCOM( encoding=3, text=a ) )
						id3.add( TSOC( encoding=3, text=a ) )
					except :
						print "encoding error"

				id3.save(v2_version=3)

				# print "new id3"
				# id3 = ID3(os.path.join(song_folder, song))
				# print id3

				mp3 = MP3(os.path.join(song_folder, song), ID3=EasyID3)
				print (mp3.pprint())
				
				mp3['copyright'] = ""
				mp3['genre'] = ""
				mp3['arranger'] = ""
				mp3['conductor'] = ""
				mp3['version'] = ''
				mp3['lyricist'] = ''
				mp3['encodedby'] = ''
				mp3['organization'] = ''
				mp3['isrc'] = ''
				mp3['bpm'] = ''
				mp3['website'] = ''
				mp3.save(v2_version=3)

				newmp3 = MP3(os.path.join(song_folder, song), ID3=EasyID3)
				print "new mp3"
				print (newmp3.pprint())


		 			
