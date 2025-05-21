for f in $(ls pdf_image/pbm); do convert-im6.q16 pdf_image/pbm/${f} pdf_image/jpg/${f%.pbm}.jpg ; done
for f in $(ls pdf_image/ppm); do convert-im6.q16 pdf_image/ppm/${f} pdf_image/jpg/${f%.ppm}.jpg ; done
ls image | grep ".jpeg"

#check IP
hostame -I
#make a server
python -m python -m http.server
#access {IP}:{port} 
172.22.114.66:8000

#take control 
ssh username@IP


