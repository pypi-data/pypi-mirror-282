import sqlite3

def getAllChapters():
    dbcon = sqlite3.connect("fullquranDb.db")
    dbcur = dbcon.cursor()
    dbcur.execute("Select count(DISTINCT chapter) from quoran")
    chaptercount = dbcur.fetchone()
    dbcon.close()
    return list(chaptercount)[0]

def getAllVerse(chapter):
    chapter = int(chapter)
    dbcon = sqlite3.connect("fullquranDb.db")
    dbcur = dbcon.cursor()
    dbcur.execute("Select count(verse) from quoran where chapter = ?", (chapter,))
    versecount = dbcur.fetchone()
    dbcon.close()
    return list(versecount)[0]

def getEngContext(chapter,verse):
    chapter = int(chapter)
    verse = int(verse)
    dbcon = sqlite3.connect("fullquranDb.db")
    dbcur = dbcon.cursor()
    dbcur.execute("Select english_content from quoran where chapter = ? and verse = ?",(chapter,verse))
    context = dbcur.fetchone()
    dbcon.close()
    return list(context)[0]

def getArbContext(chapter,verse):
    chapter = int(chapter)
    verse = int(verse)
    dbcon = sqlite3.connect("fullquranDb.db")
    dbcur = dbcon.cursor()
    dbcur.execute("Select arabic_content from quoran where chapter = ? and verse = ?",(chapter,verse))
    context = dbcur.fetchone()
    dbcon.close()
    return list(context)[0]

