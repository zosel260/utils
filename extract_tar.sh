
for i in *.tar

do name="${i%.tar}"

mkdir "$name"

tar -xvf "$i" -C "$name"

done 
