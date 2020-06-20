import requests
import json

response = requests.get('https://api.kawalcorona.com/indonesia')
data_corona = response.json()[0]
print("JUMLAH PASIEN----- \n")
print("\t Positif\t: "+data_corona['positif'])
print("\t Sembuh\t\t: "+data_corona['sembuh'])
print("\t Meninggal\t: "+data_corona['meninggal'])
print("\n By:")
print("AHMAD SYAIFULLOH NURDIANSYAH")
print("NPM : 170403010035")