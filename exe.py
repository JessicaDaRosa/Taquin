import idea1 as png

taille = 3
cube = taille * taille
k = 7
taquin = png.newTaquin(png.newlist(taille),taille)
taquin =png.melanger(taquin,500)
racine = png.Noeud(taquin,None,"start",0)

#racine = png.Noeud(png.newTaquin([1, 7, 3, 0, 5, 2, 6, 4, 8], taille), None, "_", 0)

png.printTaquin(racine.taquin)

solution = png.search(racine,k)
mvms = list() 
for i in range(len(solution)):
#    png.printTaquin(solution[i].taquin)
    mvms.append(solution[i].mvm)
print(mvms, len(mvms))
