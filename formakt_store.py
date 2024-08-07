from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pickle import *
def Lancer():
    add.show()
def load_image():
     file_dialog = QFileDialog()
     file_path, _ = file_dialog.getOpenFileName(add, 'Open Image', '.', 'Image Files (*.png *.jpg *.jpeg)')
     if file_path:
         add.hidden.setText(file_path)
         pixmap = QPixmap(file_path)
         add.imageLabel.setPixmap(pixmap.scaled(add.imageLabel.size(), aspectRatioMode=True))
def ajouter():
    produit={}
    produit['code']=add.code.text()
    produit['nom']=add.nom.text()
    produit['cat']=add.type.currentText()
    produit['prix']=add.prix.text()
    produit['image']=add.hidden.text()
    F=open('C:/Users/Manita/Desktop/ForStore/fichier/base.dat','ab')
    if produit['code']=='' or produit['nom']=='' or produit['prix']=='' or produit['image']=='':
        QMessageBox.critical(add,'Erreur','Veuillez saisie tout le information!!')
    else:
        dump(produit,F)
        QMessageBox.information(add,'Succes',"L'opération d'ajout est efféctuer avec succes")
    F.close()
def supprimer():
    add.code.clear()
    add.nom.clear()
    add.prix.clear()
    
    
def taille_fichier():
    F=open('C:/Users/Manita/Desktop/ForStore/fichier/base.dat','rb')
    n=0
    fin=False
    while fin ==False:
        try:
            e=load(F)
            n=n+1
        except:
            fin=True
    F.close()
    return n
    
def suivie_stock():
    stoke.show()
    F=open('C:/Users/Manita/Desktop/ForStore/fichier/base.dat','rb')
    n=taille_fichier()
    stoke.tw.setRowCount(n)
    i=0
    fin=False
    while fin==False:
        try:
            produit=load(F)
            stoke.tw.setItem(i,0,QTableWidgetItem(produit['code']))
            stoke.tw.setItem(i,1,QTableWidgetItem(produit['nom']))
            stoke.tw.setItem(i,2,QTableWidgetItem(produit['cat']))
            stoke.tw.setItem(i,3,QTableWidgetItem(produit['prix']))
          
            pixmap = QPixmap(produit['image'])
           
            item = QTableWidgetItem()
            item.setIcon(QIcon(pixmap))
            stoke.tw.setItem(i,4,item)
            i=i+1
        except:
            fin=True
    F.close()
def chercher():
    F=open('C:/Users/Manita/Desktop/ForStore/fichier/base.dat','rb')
    cher.code.clear()
    cher.name.clear()
    cher.prix.clear()
    cher.photo.clear()
    nom=cher.nom.text()
    typ = cher.cod.text()
    trouve=False
    fin=False
    while fin==False and trouve==False:
        try:
            produit=load(F)
            if nom in produit['nom'] or typ == produit['code']:
                trouve=True
                cher.code.setText('Le code produit :\n'+produit['code'])
                cher.name.setText('Le nom de produit :\n'+produit['nom'])
                cher.prix.setText('Le prix :'+produit['prix'])
                pixmap = QPixmap(produit['image'])
                cher.photo.setPixmap(pixmap.scaled(cher.photo.size(), aspectRatioMode=True))
        except:
            fin=True
    F.close()
def connect():
    R=open('C:/Users/Manita/Desktop/ForStore/fichier/nom.txt','a')
    R.write(sign.nom.text()+' '+sign.login.text()+' '+sign.pw.text()+'\n')
    if sign.pw.text()=='' or sign.login.text()=='' or sign.nom.text()=='':
        QMessageBox.critical(sign,'Erreur','Veuillez introduite tout les information')
    else:
        if sign.pw.text()=='formakt':
            home.show()
            home.titre.setText('Welcom '+sign.nom.text())
        else:
            QMessageBox.critical(sign,'Erreur','Invalide mot de pass')
    R.close()

    
app=QApplication([])
sign=loadUi('C:/Users/Manita/Desktop/ForStore/interface/connexion.ui')
home=loadUi('C:/Users/Manita/Desktop/ForStore/interface/home.ui')
add=loadUi('C:/Users/Manita/Desktop/ForStore/interface/ajouter.ui')
stoke=loadUi('C:/Users/Manita/Desktop/ForStore/interface/suivie.ui')
cher=loadUi('C:/Users/Manita/Desktop/ForStore/interface/search.ui')
sign.show()
sign.connect.clicked.connect(connect)
home.ajouteP.clicked.connect(Lancer)
home.stk.clicked.connect(suivie_stock)
home.search.clicked.connect(cher.show)
add.image.clicked.connect(load_image)
add.ajo.clicked.connect(ajouter)
add.dell.clicked.connect(supprimer)
cher.btn.clicked.connect(chercher)
app.exec_()

