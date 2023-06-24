# DL Create Video
-	Input files: PPTX-Datei, mehrere (wahrscheinlich mp4-dateien (LipSync Video))
-	Um ein Video erstellen zu können, muss die PPTX datei in Bilder konvertiert werden
-	Ein Bild für jede slide
-	Es soll möglich sein, unser Projekt auf allen Betriebssystemen auszuführen und zusätzlich sollte es open source sein, um keine Lizenzen oder ähnliches erwerben zu müssen.
-	Wenige Python Bibliotheken, die es ermöglichen PPTX Dateien in Bilder oder PDFS umzuwandeln
-	Führt zu Einschränkungen (wir möchten Python verwenden)
        - Bibliothek Aspose.slides -> Baut bei der kostenlosen Version Wasserzeichen in die Bilder ein
	    - Bibliothek comtypes.client -> nur auf Windows verfügbar
-	Keine andere Bibliothek gefunden, die eine All-In-One Lösung bietet
	    --> Nutzen die Bibliothek „subprocess“, um Commandline calls in den Docker Container auszuführen. In unserem Fall nutzen wir Libreoffice um die Konvertierung durchzuführen
        ```subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir" output_path, input_path]) ``` 
        - Wir konvertieren pptx -> pdf mit Hilfe von libreoffice 
        - Mit der neu erstellten PDF datei werden mit Hilfe der Bibliothek pdf2image für jede Seite in der PDF Datei ein eigenes Bild erstellt
        - Im Anschluss daran wird mit diesen Bildern ein Video erstellt. Hierfür nutzen wir die Bibliothek moviepy
            - Wir möchten, dass die Dauer, wie lange eine Slide im Video angezeigt wird, der Länge der zugehörigen mp4-datei entspricht, welche den passenden Text zu dieser Slide enthält.
                -> Hierzu müssen wir die Länge der mp4 datei bestimmen
            - Um es mehr wie eine realistische Powerpoint wirken zu lassen -> Die Slide 1 sec länger als die Audio anzeigen, somit entsteht eine kleine Pause beim wechseln der Slides
            


