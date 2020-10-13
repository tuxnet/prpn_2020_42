# Die Ziffern A, B, C und D werden von 0 bis 9 durchgetestet. 
# Um jede Kombination durchzutesten muessen 4 Schleifen fuer jede Ziffer 
# ineinander verschachtelt werden:
for a in range(0, 10):
	for b in range(0, 10):
		for c in range(0, 10):
			for d in range(0, 10):
				links = "%d%d%d%d" % (a,b,c,d) # Formatstring fuer linke Seite
                                               # der Gleichung
				rechts = "%d%d%d%d" % (d,c,b,a) # rechte Seite
				links = 4*float(links) # in Gleitkommazahl umgewandelt mal 4
				rechts = float(rechts) # rechte Seite in Gleitkommazahl umgew.
				if(a != 0 and d != 0): # a und d duerfen nicht gleich 0 sein
					if(links == rechts): # wenn die Gleichung erfuellt ist:
						print("A=%d, B=%d, C=%d, D=%d" %(a,b,c,d))
                        # werden die 4 Ziffern entsprechend auf dem Bildschirm
                        # ausgegeben. 

