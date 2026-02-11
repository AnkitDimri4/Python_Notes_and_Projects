import cv2 

video = cv2.VideoCapture('C:/Users/ANKIT DIMRI/.vscode/Complete Programming/Python program/Python tutedude/Open CV[DATA ANALYSIS, DJANGO, FLASK, REST API using DJANGO, WEB SCRAPING , OPEN CV,]/Modern.Love.S01E01.720p.HEVC.English.Vegamovies.NL.mkv') 
while video.isOpened():
    _,frame = video.read()
    frame = cv2.resize(frame,(800,720))
    cv2.imshow('Output',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
cv2.destroyAllWindows() 
